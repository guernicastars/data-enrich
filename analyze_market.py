import requests
import sys
import urllib3
from db_config import BASE_URL, HEADERS

urllib3.disable_warnings()

def run_query(query):
    try:
        response = requests.post(BASE_URL, headers=HEADERS, data=query.encode('utf-8'))
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def analyze_market():
    print("--- 1. Top 10 Most Expensive Lots (USD) ---")
    query_top_sales = """
    SELECT DISTINCT
        substring(l.title, 1, 50) as title_short,
        l.creator,
        s.hammer_price,
        s.currency,
        round(s.hammer_price * fx.rate_to_usd, 2) as price_usd,
        toDate(a.date_closed) as sale_date
    FROM sothebys.sales s
    JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
    JOIN sothebys.auctions a ON l.auction_uuid = a.auction_uuid
    LEFT JOIN sothebys.fx_rates fx ON toDate(a.date_closed) = fx.rate_date AND s.currency = fx.currency
    WHERE s.is_sold = 1 AND s.hammer_price > 0 AND fx.rate_to_usd > 0
    ORDER BY price_usd DESC
    LIMIT 10
    FORMAT Pretty
    """
    print(run_query(query_top_sales))

    print("\n--- 2. Top 10 Artists by Total Sales Volume (USD) ---")
    query_top_artists = """
    SELECT
        l.creator,
        count() as lots_sold,
        round(sum(s.hammer_price * fx.rate_to_usd), 0) as total_volume_usd
    FROM sothebys.sales s
    JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
    JOIN sothebys.auctions a ON l.auction_uuid = a.auction_uuid
    LEFT JOIN sothebys.fx_rates fx ON toDate(a.date_closed) = fx.rate_date AND s.currency = fx.currency
    WHERE s.is_sold = 1 AND s.hammer_price > 0 AND fx.rate_to_usd > 0 AND l.creator != ''
    GROUP BY l.creator
    ORDER BY total_volume_usd DESC
    LIMIT 10
    FORMAT Pretty
    """
    print(run_query(query_top_artists))

    print("\n--- 3. Price vs Size Correlation (Log-Log) ---")
    query_corr = """
    SELECT
        corr(log_hammer_price, log_surface_area) as correlation_coefficient,
        count() as sample_size
    FROM sothebys.gold_features
    WHERE log_hammer_price IS NOT NULL AND log_surface_area IS NOT NULL
    FORMAT Pretty
    """
    print(run_query(query_corr))

if __name__ == "__main__":
    analyze_market()
