# Database Configuration
HOST = "qgu31sw9py.germanywestcentral.azure.clickhouse.cloud"
PORT = "8443"
USER = "default"
PASSWORD = "PKR4cvT.xwH9k"
BASE_URL = f"https://{HOST}:{PORT}/"

HEADERS = {
    'X-ClickHouse-User': USER,
    'X-ClickHouse-Key': PASSWORD
}
