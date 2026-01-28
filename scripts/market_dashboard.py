import streamlit as st
import pandas as pd
import plotly.express as px
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

# Set page configuration
st.set_page_config(page_title="Bloomsbury Market Intelligence", layout="wide")

# Database connection function
@st.cache_data(ttl=3600)
def run_query_df(query):
    """Runs a ClickHouse query and returns the result as a Pandas DataFrame."""
    try:
        # Use CSVWithNames format for easy pandas parsing
        full_query = query + " FORMAT CSVWithNames"
        response = requests.post(BASE_URL, headers=HEADERS, data=full_query.encode('utf-8'))
        response.raise_for_status()
        # ClickHouse CSV uses \N for NULLs
        return pd.read_csv(StringIO(response.text), na_values=['\\N'])
    except requests.exceptions.RequestException as e:
        st.error(f"Database Error: {e}")
        return pd.DataFrame()

# Main Dashboard
def main():
    st.title("Bloomsbury Tech: Market Intelligence Dashboard")
    st.markdown("### Real-time Auction Data Analysis")

    # --- Sidebar Filters ---
    st.sidebar.header("Filters")
    
    # 1. Get Top Artists for Dropdown
    artist_query = """
    SELECT creator, count() as c 
    FROM sothebys.lots 
    WHERE creator != '' 
    GROUP BY creator 
    ORDER BY c DESC 
    LIMIT 50
    """
    df_artists = run_query_df(artist_query)
    
    if not df_artists.empty:
        default_artists = ['Pablo Picasso', 'Andy Warhol', 'Banksy']
        # Ensure defaults exist in the list
        valid_defaults = [a for a in default_artists if a in df_artists['creator'].values]
        
        selected_artists = st.sidebar.multiselect(
            "Select Artists",
            options=df_artists['creator'].tolist(),
            default=valid_defaults
        )
    else:
        st.warning("Could not load artist list.")
        selected_artists = []

    # --- Main KPI Section ---
    if selected_artists:
        # Construct SQL list for IN clause
        artists_sql = "'" + "', '".join(selected_artists).replace("'", "''") + "'"
        
        # Use conditional logic for FX rate: if currency is USD, rate is 1.0, otherwise use table rate.
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
        
        if not df_kpi.empty:
            # Ensure numeric types to avoid formatting errors
            cols = ['total_lots', 'total_volume_usd', 'avg_price_usd', 'max_price_usd']
            for col in cols:
                df_kpi[col] = pd.to_numeric(df_kpi[col], errors='coerce').fillna(0)

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Lots Sold", f"{df_kpi['total_lots'][0]:,.0f}")
            col2.metric("Total Volume (USD)", f"${df_kpi['total_volume_usd'][0]:,.0f}")
            col3.metric("Avg Hammer Price (USD)", f"${df_kpi['avg_price_usd'][0]:,.0f}")
            col4.metric("Record Sale (USD)", f"${df_kpi['max_price_usd'][0]:,.0f}")

        # --- Price Trend Chart ---
        st.subheader("Price Trends Over Time")
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
          AND (s.currency = 'USD' OR fx.rate_to_usd > 0)
          AND price_usd > 0
        ORDER BY sale_date
        """
        
        df_trend = run_query_df(trend_query)
        
        if not df_trend.empty:
            fig = px.scatter(
                df_trend, 
                x="sale_date", 
                y="price_usd", 
                color="creator",
                hover_data=["title"],
                log_y=True,
                title="Hammer Price (USD) vs. Sale Date (Log Scale)",
                labels={"price_usd": "Price (USD)", "sale_date": "Date", "creator": "Artist"}
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No sales data found for the selected artists.")

        # --- Top Lots Table ---
        st.subheader("Top 10 Most Expensive Lots")
        if not df_trend.empty and 'title' in df_trend.columns:
            df_trend_sorted = df_trend.sort_values(by="price_usd", ascending=False).head(10)
            st.dataframe(
                df_trend_sorted[['creator', 'title', 'sale_date', 'price_usd']].style.format({"price_usd": "${:,.2f}"}),
                use_container_width=True
            )
        else:
            st.write("No lot data available to display.")

    else:
        st.info("Please select at least one artist from the sidebar to view insights.")

if __name__ == "__main__":
    main()
