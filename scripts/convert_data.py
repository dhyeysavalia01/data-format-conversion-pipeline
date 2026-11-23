import json
import csv
from pathlib import Path
import pandas as pd

import pyarrow as pa 
import pyarrow.parquet as pq

# defining project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_FILE = BASE_DIR / 'data' / 'raw' / 'weather.json'
PROCESSED_DIR = BASE_DIR / 'data' / 'processed'
CSV_FILE = PROCESSED_DIR / 'weather.csv'
PARQUET_FILE = PROCESSED_DIR / 'weather.parquet'


# extract data from JSON
def extract_from_json():
    with open(RAW_FILE,'r') as f:
        data = json.load(f)
    
    print(f'✅ Data of length : {len(data)} extracted from JSON file')
    return data


# transform data
def transform_data(data):
    transformed_Data = []

    for x in data:
        transformed_Data.append({
            'city':x['city'],
            'temperature':float(x['temperature']),
            'humidity':float(x['humidity']),
            'wind_speed':float(x['wind_speed']),
            'timestamp':x['timestamp']
        })   
    print('✅ Transformation complete!')
    return transformed_Data

# write transformed data in CSV file
def load_csv(data):
    with open(CSV_FILE, 'w', newline="") as f:
        fieldnames = [
            "city",
            "temperature",
            "humidity",
            "wind_speed",
            "timestamp"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f'✅ CSV file created at {CSV_FILE}')

# write parquet file
def load_parquet(data):
    # python list to pyarrow table
    table = pa.Table.from_pylist(data)

    # save table to file
    pq.write_table(table, PARQUET_FILE, compression='snappy')
    # Compresses the file using Google's Snappy algorithm.
    print(f"✅ Parquet created: {PARQUET_FILE}")

# read parquet file
def read_parquet():
    table = pq.read_table(PARQUET_FILE)
    print('\nParquet data...')
    print(table.to_pandas())

    print('\nSchema...')
    print(table.schema)

# comparing file size
def compare_file_Size():
    csv_Size = CSV_FILE.stat().st_size
    parquet_size = PARQUET_FILE.stat().st_size

    print(f'\nCSV file size: {csv_Size} bytes')
    print(f'Parquet file size: {parquet_size} bytes')

    if csv_Size > 0:
        reduction = ((csv_Size - parquet_size) / csv_Size) * 100
        print('\nsize reduction:',reduction,'%')

def main():
    PROCESSED_DIR.mkdir( # make dir if it doesn't exist
        parents=True,
        exist_ok=True
    )

    data = extract_from_json()
    data = transform_data(data)
    
    load_csv(data)
    load_parquet(data)
    read_parquet()
    compare_file_Size()

if __name__ == "__main__":
    main()