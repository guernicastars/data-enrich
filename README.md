# Bloomsbury Tech: Art Market Analysis Toolkit

**A secure, production-ready environment for analyzing high-value auction data.**

This repository contains the tools and scripts used to explore, enrich, and analyze a dataset of ~100,000 fine art lots and sales from Christie's and Sotheby's.

## 🚀 Features

*   **Secure Connection:** Connects to ClickHouse using a separate, git-ignored configuration file (`db_config.py`).
*   **Market Intelligence:** Pre-built scripts (`analyze_market.py`) to identify:
    *   Top 10 most expensive lots (normalized to USD).
    *   Top 10 artists by sales volume.
    *   Correlation between artwork size and price.
*   **Zed Editor Integration:** Includes `market_analysis_zed.py` formatted with `# %%` cells for interactive REPL-style analysis directly within Zed.
*   **Jupyter Support:** Standard `market_analysis.ipynb` for traditional data science workflows.
*   **Production Standards:** Configured with `pyproject.toml` for `ruff` (linting/formatting) and `basedpyright` (type checking).

## 🛠️ Setup

1.  **Install Dependencies:**
    ```bash
    pip install requests pandas ruff basedpyright
    ```

2.  **Configure Credentials:**
    Create a file named `db_config.py` in the root directory:
    ```python
    # db_config.py
    HOST = "your-clickhouse-host"
    PORT = "8443"
    USER = "default"
    PASSWORD = "your-password"
    BASE_URL = f"https://{HOST}:{PORT}/"

    HEADERS = {
        'X-ClickHouse-User': USER,
        'X-ClickHouse-Key': PASSWORD
    }
    ```

3.  **Run Analysis:**
    *   **CLI:** `python3 analyze_market.py`
    *   **Zed:** Open `market_analysis_zed.py` and press `Shift+Enter` to run cells.
    *   **Jupyter:** `jupyter notebook market_analysis.ipynb`

## 📊 Key Insights (Sample)

*   **Digital Disruption:** Digital artworks and NFTs are currently commanding the highest individual prices in this dataset.
*   **Blue Chip Volume:** Picasso, Warhol, and Banksy dominate total sales volume.
*   **Price/Size:** There is a weak positive correlation (0.24) between size and price, indicating that brand/artist is a far stronger value driver than scale.

## 📂 File Structure

*   `analyze_market.py`: Main reporting script.
*   `market_analysis_zed.py`: Interactive script for Zed Editor.
*   `market_analysis.ipynb`: Jupyter Notebook version.
*   `inspect_data.py`: Utility to peek at table schemas and sample rows.
*   `explore_clickhouse.py`: Connection connectivity test.
*   `pyproject.toml`: Configuration for Python tooling (Ruff, Pyright).

---
*Prepared for YC Application Session.*
