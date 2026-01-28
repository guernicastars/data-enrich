import dash
from dash import dcc, html, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import requests
import sys
import os
from io import StringIO
import urllib3

# Suppress SSL warnings
urllib3.disable_warnings()

# Add parent directory to path to find db_config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db_config import BASE_URL, HEADERS

# Initialize Dash app with Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.title = "Bloomsbury Market Intelligence"
server = app.server

def run_query_df(query):
    """Runs a ClickHouse query and returns the result as a Pandas DataFrame."""
    try:
        full_query = query + " FORMAT CSVWithNames"
        response = requests.post(BASE_URL, headers=HEADERS, data=full_query.encode('utf-8'))
        response.raise_for_status()
        return pd.read_csv(StringIO(response.text), na_values=['\\N'])
    except Exception as e:
        print(f"Database Error: {e}")
        return pd.DataFrame()

# --- Initial Data Load (Top Artists) ---
def get_top_artists():
    query = """
    SELECT creator, count() as c 
    FROM sothebys.lots 
    WHERE creator != '' 
    GROUP BY creator 
    ORDER BY c DESC 
    LIMIT 50
    """
    df = run_query_df(query)
    if not df.empty:
        return df['creator'].tolist()
    return []

artist_options = get_top_artists()
default_artists = [a for a in ['Pablo Picasso', 'Andy Warhol', 'Banksy'] if a in artist_options]

# --- Layout ---
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Bloomsbury Tech: Market Intelligence", className="text-center text-primary mb-4"), width=12)
    ], className="mt-4"),

    dbc.Row([
        dbc.Col([
            html.Label("Select Artists:"),
            dcc.Dropdown(
                id='artist-dropdown',
                options=artist_options,
                value=default_artists,
                multi=True,
                className="mb-4"
            )
        ], width=12)
    ]),

    # KPI Row
    dbc.Row(id='kpi-row', className="mb-4"),

    # Charts Row
    dbc.Row([
        dbc.Col(dcc.Graph(id='price-trend-chart'), width=12)
    ]),

    # Data Table Row
    dbc.Row([
        dbc.Col([
            html.H4("Top 10 Most Expensive Lots", className="mt-4 mb-3"),
            dash_table.DataTable(
                id='top-lots-table',
                style_table={'overflowX': 'auto'},
                style_cell={'textAlign': 'left', 'padding': '10px'},
                style_header={'backgroundColor': 'rgb(230, 230, 230)', 'fontWeight': 'bold'}
            )
        ], width=12)
    ], className="mb-5"),

    # --- New Insights Sections ---
    html.Hr(),
    dbc.Row([
        dbc.Col(html.H3("Advanced Market Dynamics", className="text-center text-secondary mb-4"), width=12)
    ]),

    dbc.Row([
        # Bidding Intensity Chart
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Bidding Intensity vs. Price Realization"),
                dbc.CardBody([
                    dcc.Graph(id='bidding-chart'),
                    html.Small("Shows how bid competition drives prices above/below the mid-estimate.", className="text-muted")
                ])
            ], className="mb-4")
        ], width=6),

        # Economics Correlation Chart
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("Valuation Economics: Size vs. Price (Log-Log)"),
                dbc.CardBody([
                    dcc.Graph(id='correlation-chart'),
                    html.Small("Analyzes the 'Brand vs. Scale' effect using pre-computed log metrics.", className="text-muted")
                ])
            ], className="mb-4")
        ], width=6),
    ]),

    # AI Stats Section
    html.Hr(),
    dbc.Row([
        dbc.Col(html.H3("Data Pipeline Health (AI Extraction)", className="text-center text-secondary mb-4"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id='ai-stats-chart'), width=12)
    ], className="mb-5")

], fluid=True)

# --- Callbacks ---
@callback(
    [Output('kpi-row', 'children'),
     Output('price-trend-chart', 'figure'),
     Output('top-lots-table', 'data'),
     Output('top-lots-table', 'columns'),
     Output('bidding-chart', 'figure'),
     Output('correlation-chart', 'figure'),
     Output('ai-stats-chart', 'figure')],
    [Input('artist-dropdown', 'value')]
)
def update_dashboard(selected_artists):
    if not selected_artists:
        return [], {}, [], [], {}, {}, {}

    # Construct SQL list
    # Escape single quotes in each artist name individually to prevent SQL errors
    # e.g., "O'Keefe" becomes "O''Keefe"
    escaped_artists = [a.replace("'", "''") for a in selected_artists]
    artists_sql = "'" + "', '".join(escaped_artists) + "'"

    # 1. KPI Query
    kpi_query = f"""
    SELECT 
        count() as total_lots,
        sum(hammer_price * if(s.currency = 'USD', 1.0, fx.rate_to_usd)) as total_volume_usd,
        avg(hammer_price * if(s.currency = 'USD', 1.0, fx.rate_to_usd)) as avg_price_usd,
        max(hammer_price * if(s.currency = 'USD', 1.0, fx.rate_to_usd)) as max_price_usd
    FROM sothebys.sales s
    JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
    JOIN sothebys.auctions a ON l.auction_uuid = a.auction_uuid
    LEFT JOIN sothebys.fx_rates fx ON toDate(a.date_closed) = fx.rate_date AND s.currency = fx.currency
    WHERE l.creator IN ({artists_sql})
      AND s.is_sold = 1
      AND (s.currency = 'USD' OR fx.rate_to_usd > 0)
    """
    df_kpi = run_query_df(kpi_query)
    
    # 2. Trend Query
    trend_query = f"""
    SELECT 
        l.creator,
        toDate(a.date_closed) as sale_date,
        (s.hammer_price * if(s.currency = 'USD', 1.0, fx.rate_to_usd)) as price_usd,
        l.title as title
    FROM sothebys.sales s
    JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
    JOIN sothebys.auctions a ON l.auction_uuid = a.auction_uuid
    LEFT JOIN sothebys.fx_rates fx ON toDate(a.date_closed) = fx.rate_date AND s.currency = fx.currency
    WHERE l.creator IN ({artists_sql})
      AND s.is_sold = 1
      AND price_usd > 0
      AND (s.currency = 'USD' OR fx.rate_to_usd > 0)
    ORDER BY sale_date
    """
    df_trend = run_query_df(trend_query)

    # 3. Bidding Intensity Query
    bidding_query = f"""
    SELECT
        s.num_bids,
        avg(s.hammer_price / ((l.estimate_low + l.estimate_high) / 2)) as realization_ratio
    FROM sothebys.sales s
    JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
    WHERE l.creator IN ({artists_sql})
      AND s.is_sold = 1
      AND s.num_bids > 0
      AND l.estimate_low > 0
    GROUP BY s.num_bids
    HAVING count() > 2
    ORDER BY s.num_bids ASC
    """
    df_bidding = run_query_df(bidding_query)

    # 4. Correlation Query (Price vs Size)
    corr_query = f"""
    SELECT
        g.log_surface_area,
        g.log_hammer_price,
        l.creator
    FROM sothebys.gold_features g
    JOIN sothebys.lots l ON g.lot_uuid = l.lot_uuid
    WHERE l.creator IN ({artists_sql})
      AND g.log_hammer_price > 0 
      AND g.log_surface_area > 0
    LIMIT 1000
    """
    df_corr = run_query_df(corr_query)

    # 5. AI Stats Query (Global context, but good to see relative to filtered)
    # Note: We keep this global for now as it's a pipeline metric
    ai_query = """
    SELECT
        creation_source,
        count() as count,
        avg(artist_name_confidence) as avg_conf
    FROM sothebys.silver_extractions
    GROUP BY creation_source
    """
    df_ai = run_query_df(ai_query)

    # --- Build KPIs ---
    kpi_cards = []
    if not df_kpi.empty:
        # Numeric coercion
        cols = ['total_lots', 'total_volume_usd', 'avg_price_usd', 'max_price_usd']
        for col in cols:
            df_kpi[col] = pd.to_numeric(df_kpi[col], errors='coerce').fillna(0)

        metrics = [
            ("Total Lots Sold", f"{df_kpi['total_lots'][0]:,.0f}"),
            ("Total Volume (USD)", f"${df_kpi['total_volume_usd'][0]:,.0f}"),
            ("Avg Price (USD)", f"${df_kpi['avg_price_usd'][0]:,.0f}"),
            ("Record Sale (USD)", f"${df_kpi['max_price_usd'][0]:,.0f}")
        ]
        
        for label, value in metrics:
            card = dbc.Col(dbc.Card([
                dbc.CardBody([
                    html.H5(label, className="card-title text-muted"),
                    html.H3(value, className="card-text")
                ])
            ], className="shadow-sm"), width=3)
            kpi_cards.append(card)

    # --- Build Trend Chart ---
    fig_trend = {}
    if not df_trend.empty:
        fig_trend = px.scatter(
            df_trend, 
            x="sale_date", 
            y="price_usd", 
            color="creator",
            hover_data=["title"],
            log_y=True,
            title="Hammer Price (USD) vs. Sale Date (Log Scale)",
            labels={"price_usd": "Price (USD)", "sale_date": "Date", "creator": "Artist"},
            template="plotly_white"
        )
        fig_trend.update_layout(transition_duration=500)

    # --- Build Bidding Chart ---
    fig_bidding = {}
    if not df_bidding.empty:
        df_bidding['realization_ratio'] = pd.to_numeric(df_bidding['realization_ratio'])
        fig_bidding = px.line(
            df_bidding,
            x="num_bids",
            y="realization_ratio",
            title="Avg Price Realization vs. Number of Bids",
            labels={"num_bids": "Number of Bids", "realization_ratio": "Realization Ratio (Price / Est)"},
            markers=True,
            template="plotly_white"
        )
        fig_bidding.add_hline(y=1.0, line_dash="dash", line_color="red", annotation_text="Estimate Parity")

    # --- Build Correlation Chart ---
    fig_corr = {}
    if not df_corr.empty:
        fig_corr = px.scatter(
            df_corr,
            x="log_surface_area",
            y="log_hammer_price",
            color="creator",
            title="Log Price vs. Log Surface Area",
            template="plotly_white",
            opacity=0.6
        )

    # --- Build AI Stats Chart ---
    fig_ai = {}
    if not df_ai.empty:
        fig_ai = px.bar(
            df_ai,
            x="creation_source",
            y="count",
            color="avg_conf",
            title="AI Extraction Volume & Confidence by Source",
            labels={"count": "Records Extracted", "avg_conf": "Avg Confidence"},
            template="plotly_white"
        )

    # --- Build Table ---
    table_data = []
    table_cols = []
    if not df_trend.empty and 'title' in df_trend.columns:
        df_top = df_trend.sort_values(by="price_usd", ascending=False).head(10)
        # Format for display
        df_top['price_usd'] = df_top['price_usd'].apply(lambda x: f"${x:,.2f}")
        
        table_data = df_top[['creator', 'title', 'sale_date', 'price_usd']].to_dict('records')
        table_cols = [{"name": i, "id": i} for i in ['creator', 'title', 'sale_date', 'price_usd']]

    return kpi_cards, fig_trend, table_data, table_cols, fig_bidding, fig_corr, fig_ai

if __name__ == "__main__":
    # In production/docker, we need to bind to 0.0.0.0
    app.run(debug=False, host='0.0.0.0', port=8050)
