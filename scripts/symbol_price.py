import argparse
import logging
import sys
import os
import requests
from bs4 import BeautifulSoup
# Add parent directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import utils

def fetch_stock_data(symbol, settings):
    """Fetch stock data from the web using the stock symbol."""
    url = settings.get("stock_data_url").format(symbol=symbol)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract stock data (adjust selectors based on the website structure)
        stock_data = {
            "Price": soup.find("fin-streamer", {"data-field": "regularMarketPrice"}).text,
            "Low": soup.find("td", {"data-test": "DAYS_RANGE-value"}).text.split(" - ")[0],
            "High": soup.find("td", {"data-test": "DAYS_RANGE-value"}).text.split(" - ")[1],
            "Open": soup.find("td", {"data-test": "OPEN-value"}).text,
            "Previous Close": soup.find("td", {"data-test": "PREV_CLOSE-value"}).text,
            "Change": soup.find("fin-streamer", {"data-field": "regularMarketChange"}).text,
            "Change (%)": soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"}).text,
            "52w Low": soup.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.split(" - ")[0],
            "52w High": soup.find("td", {"data-test": "FIFTY_TWO_WK_RANGE-value"}).text.split(" - ")[1],
        }
        
        return stock_data
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except AttributeError:
        print("Error parsing data. The website structure may have changed.")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch stock details for a specific symbol.")
    parser.add_argument("--symbol", required=True, help="Stock symbol to fetch details for.")
    args = parser.parse_args()
    
    # Load settings
    settings = utils.load_settings()

    # Setup logging
    log_level = getattr(logging, settings.get("log_level", "INFO").upper(), logging.INFO)
    logging.basicConfig(level=log_level, format="%(asctime)s - %(levelname)s - %(message)s")

    
    # Fetch stock data
    stock_data = fetch_stock_data(args.symbol, settings)
    if stock_data:
        print(f"Stock data for {args.symbol}:")
        for key, value in stock_data.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
