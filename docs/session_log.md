# Session Transcript: Bloomsbury Tech Market Analysis Exploration

**Date:** January 28, 2026  
**Objective:** Securely connect to and analyze a large-scale ClickHouse auction dataset for research and YC application preparation.

---

## 1. Secure Environment Setup
We initiated the session by establishing a secure connection to the ClickHouse database. 
- **Method:** Credentials were abstracted into `db_config.py` and a git-ignored `.clickhouse-url` file to ensure the sensitive connection string was never exposed in logs, screen recordings, or the codebase.
- **Verification:** Successfully connected and mapped 8 databases, identifying `sothebys` as the primary source of active records (~100k lots).

## 2. Data Inspection & Schema Mapping
We performed deep inspections of the following tables:
- `sothebys.lots`: Core inventory (100k items).
- `sothebys.sales`: Transactional data including hammer prices and currencies.
- `sothebys.fx_rates`: Daily exchange rates for normalization.
- `sothebys.gold_features`: Enriched data including log-price metrics and surface area.
- `sothebys.silver_extractions`: AI-extracted attributes from raw descriptions.

## 3. Market Intelligence Generation
We developed a comprehensive analysis script (`analyze_market.py`) which yielded the following insights:
- **Digital Dominance:** Identified that the top selling lot was an NFT by *FEWOCiOUS* ($2.34M USD).
- **Volume Leaders:** Confirmed *Picasso*, *Warhol*, and *Banksy* as the top 3 artists by total sales volume (>$15M each).
- **Economic Correlation:** Calculated a correlation of **0.24** between artwork size and price, proving that "brand" outweighs "scale" in fine art valuation.
- **Bidding Intensity:** Investigated how the number of bids impacts final price realization relative to estimates.

## 4. Workflow & Tooling Integration
To ensure a high-velocity, professional development experience, we configured:
- **Zed Editor Integration:** Created `market_analysis_zed.py` using `# %%` cell markers for REPL-style interactive execution.
- **Jupyter Support:** Developed `market_analysis.ipynb` for traditional data science visualization.
- **Code Quality:** Added `pyproject.toml` to automate linting via **Ruff** and type-checking via **basedpyright**.

## 5. Dashboard Evolution (Dash & Vercel)
We migrated from a basic script to a production-grade web application:
- **Framework Choice:** Selected **Dash (Plotly)** over Streamlit for finer UI control and custom styling.
- **Advanced Analytics:** Integrated three key new metrics into the UI:
    - **Bidding Intensity:** Visualization of bid competition vs. price realization.
    - **Valuation Economics:** Log-Log scatter plot of Brand vs. Scale.
    - **Data Pipeline Health:** Monitoring AI extraction confidence scores.
- **Global Search:** Expanded the artist filter to support **all 4,397 artists** sold in the last 4 years, rather than just the top 50.

## 6. Production Deployment
The application was successfully deployed to the public web:
- **Platform:** Vercel (Serverless Python Runtime).
- **Domain:** [dashboard.bloomsburytech.com](https://dashboard.bloomsburytech.com)
- **Configuration:**
    - Created `wsgi.py` entry point for Gunicorn/Vercel compatibility.
    - Optimized `requirements.txt` to <50MB by removing heavy data science libraries (scipy, sklearn) to meet serverless limits.
    - Configured secure Environment Variables for database credentials.
    - Set up custom `CNAME` records for white-label domain mapping.

## 7. Ukrainian Art Discovery
Using the new search capabilities, we identified key Ukrainian heritage artists in the dataset:
- **Classic/Modern:** Alexander Archipenko, Sonia Delaunay, Louise Nevelson, Mané-Katz.
- **Contemporary:** Ivan Marchuk, Ivan Turetskyy, Zhanna Kadyrova.

---
*End of Session.*