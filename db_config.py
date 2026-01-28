import os

# Database Configuration
# Priority: Environment Variables (for Vercel/Prod) > Hardcoded Defaults (for Local)
HOST = os.getenv("CLICKHOUSE_HOST", "qgu31sw9py.germanywestcentral.azure.clickhouse.cloud")
PORT = os.getenv("CLICKHOUSE_PORT", "8443")
USER = os.getenv("CLICKHOUSE_USER", "default")
PASSWORD = os.getenv("CLICKHOUSE_PASSWORD", "PKR4cvT.xwH9k")
BASE_URL = f"https://{HOST}:{PORT}/"

HEADERS = {
    'X-ClickHouse-User': USER,
    'X-ClickHouse-Key': PASSWORD
}
