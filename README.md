# 📊 Stock Analysis Project

This project provides a command-line toolset for analyzing stock symbol activity from a CSV file. It supports filtering by date, counting symbol occurrences, and viewing detailed records for specific symbols.

---

## 📁 Project Structure

```
stock_analysis/
├── config/
│   └── settings.json          # Centralized configuration
├── data/
│   └── Latest Stocks.csv      # Your stock data file
├── scripts/
│   ├── analyze_symbols.py     # Summary analysis with optional symbol filtering
│   ├── symbol_details.py      # Detailed view for a specific symbol
│   ├── utils.py               # Shared helper functions
│   └── __init__.py            # Package initialization
└── README.md                  # Project documentation
```

---

## 📦 Setup

1. Install dependencies (if required):

   ```bash
   pip install pandas
   ```

2. Add your stock data to:

   ```
   data/Latest Stocks.csv
   ```

---

## 📄 Usage

### 🔍 Analyze Symbols

Run the `analyze_symbols.py` script to summarize stock activity:

```bash
python scripts/analyze_symbols.py --days_back 30 --count_threshold 2
```

### 🔎 View Symbol Details

Run the `symbol_details.py` script to view detailed information for a specific symbol:

```bash
python scripts/symbol_details.py --symbol TRENT
```

---

## ⚙️ Configuration

Modify the `config/settings.json` file to customize the behavior of the scripts. Example:

```json
{
  "data_file_path": "data/Latest Stocks.csv",
  "default_days_back": 30,
  "default_count_threshold": 2,
  "log_level": "INFO",
  "output_directory": "output",
  "date_column": "date",
  "symbol_column": "symbol"
}
```

---

## 📂 Data Format

The `Latest Stocks.csv` file should follow this structure:

| date       | symbol      | ... |
|------------|-------------|-----|
| 2025-07-01 | TRENT       | ... |
| 2025-07-02 | VOLTAMP     | ... |
| ...        | ...         | ... |

Ensure the `date` column is in a recognizable date format.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Let me know if you'd like this saved as a file or converted into a PDF!
