import requests
import sys
import json
import datetime
from db_config import BASE_URL, HEADERS

TARGET_DBS = [
    'sothebys',
    'christies',
    'auction_19th_century_american_and_western_art',
    'collector_connoisseur_the_max_n_berry_collections_american_art_d'
]

def run_query(query):
    try:
        response = requests.post(BASE_URL, headers=HEADERS, data=query.encode('utf-8'))
        response.raise_for_status()
        return response.text
    except Exception:
        return None

def get_tables(db):
    raw = run_query(f"SHOW TABLES FROM {db}")
    if raw:
        return [t for t in raw.strip().split('\n') if t]
    return []

def get_columns(db, table):
    query = f"SELECT name, type FROM system.columns WHERE database = '{db}' AND table = '{table}' FORMAT JSON"
    res = run_query(query)
    if res:
        try:
            return json.loads(res)['data']
        except:
            pass
    return []

def analyze_table(db, table, file_handle):
    count_res = run_query(f"SELECT count() FROM {db}.{table}")
    row_count = int(count_res.strip()) if count_res else 0

    print(f"Analyzing {db}.{table} ({row_count} rows)...")
    
    file_handle.write(f"## Table: `{db}.{table}`\n\n")
    file_handle.write(f"**Row Count:** {row_count:,}\n\n")

    if row_count == 0:
        file_handle.write("*Table is empty.*" + "\n\n---\n\n")
        return

    columns = get_columns(db, table)
    
    file_handle.write("| Column | Type | Fill Rate | Unique Vals | Min | Max |\n")
    file_handle.write("| :--- | :--- | :--- | :--- | :--- | :--- |\n")

    for col in columns:
        col_name = col['name']
        col_type = col['type']
        
        min_max_sql = "NULL, NULL"
        if 'Int' in col_type or 'Float' in col_type or 'Date' in col_type:
            min_max_sql = f"min({col_name}), max({col_name})"

        query_stats = f"SELECT count({col_name}) as populated, uniq({col_name}) as distinct_count, {min_max_sql} FROM {db}.{table} FORMAT JSON"
        
        stats_raw = run_query(query_stats)
        if stats_raw:
            try:
                stats = json.loads(stats_raw)['data'][0]
                populated = stats['populated']
                distinct = stats['distinct_count']
                val_min = stats.get(f"min({col_name})")
                val_max = stats.get(f"max({col_name})")
                
                fill_rate = f"{(populated / row_count) * 100:.1f}%"
                
                str_min = str(val_min) if val_min is not None else "-"
                str_max = str(val_max) if val_max is not None else "-"
                
                if len(str_min) > 20: str_min = str_min[:17] + "..."
                if len(str_max) > 20: str_max = str_max[:17] + "..."

                file_handle.write(f"| `{col_name}` | {col_type} | {fill_rate} | {distinct:,} | {str_min} | {str_max} |\n")
            except Exception:
                file_handle.write(f"| `{col_name}` | {col_type} | Error | - | - | - |\n")
        else:
             file_handle.write(f"| `{col_name}` | {col_type} | - | - | - | - |\n")

    file_handle.write("\n---\n\n")

def main():
    with open("DATA_DICTIONARY.md", "w") as f:
        f.write("# Bloomsbury Tech Data Dictionary\n\n")
        f.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        for db in TARGET_DBS:
            raw_tables = run_query(f"SHOW TABLES FROM {db}")
            if not raw_tables:
                continue
            tables = [t for t in raw_tables.strip().split('\n') if t]
            
            f.write(f"# Database: `{db}`\n\n")
            for table in tables:
                analyze_table(db, table, f)

    print("\nAnalysis Complete. Results saved to DATA_DICTIONARY.md")

if __name__ == "__main__":
    main()