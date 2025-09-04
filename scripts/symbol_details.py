import argparse
import logging
import sys
import os

# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import utils

# Load settings
settings = utils.load_settings()
file_path = settings["data_file_path"]
date_column = settings["date_column"]
symbol_column = settings["symbol_column"]

# Parse CLI arguments
parser = argparse.ArgumentParser(description="Show detailed records for a specific stock symbol.")
parser.add_argument("--symbol", type=str, required=True)
parser.add_argument("--days_back", type=int, default=settings["default_days_back"])
args = parser.parse_args()

# Setup logging
log_level = getattr(logging, settings.get("log_level", "INFO").upper(), logging.INFO)
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    df = utils.load_stock_data(file_path, date_column)
    df = utils.filter_by_date(df, date_column, args.days_back)
    df = utils.filter_by_symbol(df, symbol_column, args.symbol)

    if df.empty:
        print(f"No records found for symbol '{args.symbol}' in the last {args.days_back} days.")
    else:
        print(f"\nDetailed records for symbol '{args.symbol}' (last {args.days_back} days):\n")
        print(df.sort_values(by=date_column, ascending=False).to_string(index=False))

except Exception as e:
    logging.error(f"An error occurred: {e}")
