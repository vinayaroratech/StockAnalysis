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
parser = argparse.ArgumentParser(description="Analyze stock symbol frequency from CSV.")
parser.add_argument("--days_back", type=int, default=settings["default_days_back"])
parser.add_argument("--count_threshold", type=int, default=settings["default_count_threshold"])
parser.add_argument("--symbol_filter", type=str, default=None)
parser.add_argument("--details", action="store_true")
args = parser.parse_args()

# Setup logging
log_level = getattr(logging, settings.get("log_level", "INFO").upper(), logging.INFO)
logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

try:
    df = utils.load_stock_data(file_path, date_column)
    df = utils.filter_by_date(df, date_column, args.days_back)

    if args.symbol_filter:
        df = utils.filter_by_symbol(df, symbol_column, args.symbol_filter)

    if args.details:
        if df.empty:
            print(f"No records found for symbol '{args.symbol_filter}' in the last {args.days_back} days.")
        else:
            print(f"\nDetailed records for symbol '{args.symbol_filter}' (last {args.days_back} days):\n")
            print(df.sort_values(by=date_column, ascending=False).to_string(index=False))
    else:
        summary = utils.summarize_symbols(df, symbol_column, date_column, args.count_threshold)
        if summary.empty:
            print("No symbols matched the criteria.")
        else:
            print(f"\nStock Symbol Counts with Most Recent Dates (last {args.days_back} days, count >= {args.count_threshold}):\n")
            print(summary.to_string(index=False))

except Exception as e:
    logging.error(f"An error occurred: {e}")
