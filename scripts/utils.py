import json
import pandas as pd
from datetime import datetime, timedelta

def load_settings(path="config/settings.json"):
    with open(path, "r") as f:
        return json.load(f)

def load_stock_data(file_path, date_column):
    return pd.read_csv(file_path, parse_dates=[date_column], dayfirst=True)

def filter_by_date(df, date_column, days_back):
    cutoff_date = datetime.today() - timedelta(days=days_back)
    return df[df[date_column] >= cutoff_date]

def filter_by_symbol(df, symbol_column, symbol):
    return df[df[symbol_column].str.upper() == symbol.upper()]

def summarize_symbols(df, symbol_column, date_column, count_threshold):
    summary = (
        df.groupby(symbol_column)
        .agg(count=(symbol_column, 'size'), most_recent_date=(date_column, 'max'))
        .reset_index()
    )
    return summary[summary['count'] >= count_threshold].sort_values(
        by=['count', 'most_recent_date'], ascending=[False, False]
    )
