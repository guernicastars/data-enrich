import requests
import sys
import os
import urllib3

# Add parent directory to path to find db_config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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

def inspect_table(db, table):
    print(f"\n--- Inspecting {db}.{table} ---")
    
    # 1. Get Row Count
    count = run_query(f"SELECT count() FROM {db}.{table}")
    if count:
        print(f"Total Rows: {count.strip()}")

    # 2. Describe Schema (name and type)
    print("\nSchema:")
    schema_raw = run_query(f"DESCRIBE {db}.{table}")
    if schema_raw:
        # Simple parsing for display
        lines = schema_raw.strip().split('\n')
        print(f"{'Column':<30} {'Type':<20}")
        print("-" * 50)
        for line in lines:
            parts = line.split('\t')
            if len(parts) >= 2:
                print(f"{parts[0]:<30} {parts[1]:<20}")

    # 3. Sample Data
    print("\nSample Data (First 3 rows):")
    # Using FORMAT JSONEachRow for readable output
    sample = run_query(f"SELECT * FROM {db}.{table} LIMIT 3 FORMAT JSONEachRow")
    if sample:
        print(sample.strip())
    else:
        print("(No data found)")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        inspect_table(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python3 inspect_data.py <database> <table>")

