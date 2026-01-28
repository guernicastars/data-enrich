import requests
import sys

# Configuration derived from the provided JDBC URL
HOST = "qgu31sw9py.germanywestcentral.azure.clickhouse.cloud"
PORT = "8443"
USER = "default"
PASSWORD = "PKR4cvT.xwH9k"
BASE_URL = f"https://{HOST}:{PORT}/"

HEADERS = {
    'X-ClickHouse-User': USER,
    'X-ClickHouse-Key': PASSWORD
}

def run_query(query):
    print(f"Running query: {query}")
    try:
        response = requests.post(BASE_URL, headers=HEADERS, data=query.encode('utf-8'))
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error executing query: {e}")
        if response is not None:
             print(f"Response details: {response.text}")
        return None

def main():
    print("--- Connecting to ClickHouse ---")
    
    # 1. List Databases
    databases_raw = run_query("SHOW DATABASES")
    if not databases_raw:
        return

    databases = [db for db in databases_raw.strip().split('\n') if db]
    print(f"\nFound {len(databases)} databases: {', '.join(databases)}")

    # 2. List Tables in non-system databases
    for db in databases:
        if db in ['INFORMATION_SCHEMA', 'information_schema', 'system', 'default']: # Skip system/default for brevity if desired, but default is usually interesting.
            continue
        
        print(f"\n--- Tables in database '{db}' ---")
        tables_raw = run_query(f"SHOW TABLES FROM {db}")
        if tables_raw:
            print(tables_raw.strip())
        else:
            print("(No tables found)")

    # Also check default just in case
    if 'default' in databases:
         print(f"\n--- Tables in database 'default' ---")
         tables_raw = run_query(f"SHOW TABLES FROM default")
         if tables_raw:
            print(tables_raw.strip())

if __name__ == "__main__":
    main()
