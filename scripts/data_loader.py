# backend/services/data_loader.py

import polars as pl
from sqlalchemy.orm import Session
from datetime import datetime
from backend.Models.models import InventoryItem, Session  # Ensure correct import path

def validate_and_transform_row(row):
    # Handles 'NULL' values and converts date strings to datetime objects if not 'NULL'
    for date_col in ['date_production_start', 'date_received_into_inventory', 'date_shipped_from_inventory']:
        if row[date_col] == 'NULL':
            row[date_col] = None
        else:
            try:
                row[date_col] = datetime.strptime(row[date_col], '%Y-%m-%d %H:%M:%S')
            except ValueError:
                row[date_col] = None

    # Ensure quantity is a float
    try:
        row['quantity'] = float(row['quantity'])
    except ValueError:
        row['quantity'] = 0.0  # Default to 0 if conversion fails

    return row

def load_data_to_db(csv_file_path):
    df = pl.read_csv(csv_file_path)
    df_pandas = df.to_pandas()

    session = Session()

    for index, row in df_pandas.iterrows():
        validated_row = validate_and_transform_row(row)
        item = InventoryItem(
            item_id=validated_row['item_id'],
            quantity=validated_row['quantity'],
            date_production_start=validated_row['date_production_start'],
            date_received_into_inventory=validated_row['date_received_into_inventory'],
            date_shipped_from_inventory=validated_row['date_shipped_from_inventory']
        )
        session.add(item)
    session.commit()
    session.close()

# Example usage
# load_data_to_db('/path/to/your/data.csv')

load_data_to_db('../RawData/test-project-data.csv')
