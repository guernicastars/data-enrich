# %% [markdown]
# # Bloomsbury Tech Market Analysis (Zed REPL Mode)

import requests
import pandas as pd
import urllib3
from io import StringIO
import sys
import os

# Add parent directory to path to find db_config
sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('.'))
from db_config import BASE_URL, HEADERS


urllib3.disable_warnings()


def run_query_df(query):
    try:
        # Use CSVWithNames format for easy pandas parsing
        full_query = query + " FORMAT CSVWithNames"
        response = requests.post(
            BASE_URL, headers=HEADERS, data=full_query.encode("utf-8")
        )
        response.raise_for_status()
        return pd.read_csv(StringIO(response.text))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# %%
# 1. Top 10 Most Expensive Lots (USD)
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
"""

df_top_sales = run_query_df(query_top_sales)
df_top_sales

# %%
# 2. Top 10 Artists by Total Sales Volume (USD)
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
"""

df_top_artists = run_query_df(query_top_artists)
df_top_artists

# %%
# 3. Price vs Size Correlation (Log-Log)
query_corr = """
SELECT
    corr(log_hammer_price, log_surface_area) as correlation_coefficient,
    count() as sample_size
FROM sothebys.gold_features
WHERE log_hammer_price IS NOT NULL AND log_surface_area IS NOT NULL
"""

df_corr = run_query_df(query_corr)
df_corr

# %%
# 4. Research: Bidding Intensity vs. Price Realization
# Does more bidding lead to higher prices relative to the mid-estimate?
query_bidding = """
SELECT
    s.num_bids,
    avg(s.hammer_price / ((l.estimate_low + l.estimate_high) / 2)) as avg_realization_ratio,
    count() as sample_size
FROM sothebys.sales s
JOIN sothebys.lots l ON s.lot_uuid = l.lot_uuid
WHERE s.is_sold = 1
  AND s.num_bids > 0
  AND l.estimate_low > 0
  AND l.estimate_high > 0
GROUP BY s.num_bids
HAVING sample_size > 5
ORDER BY s.num_bids ASC
"""

df_bidding = run_query_df(query_bidding)
df_bidding

# %%
# 5. AI Intelligence: LLM Extraction Performance
# Analyzing the confidence scores and sources of our enriched data.
query_ai_perf = """
SELECT
    creation_source,
    count() as count,
    avg(artist_name_confidence) as avg_artist_conf,
    avg(dimensions_confidence) as avg_dim_conf,
    avg(medium_confidence) as avg_medium_conf
FROM sothebys.silver_extractions
GROUP BY creation_source
"""

df_ai_perf = run_query_df(query_ai_perf)
df_ai_perf
