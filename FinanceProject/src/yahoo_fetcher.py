"""
Data fetching utilities for retrieving stock price data from Yahoo Finance.

This module provides functions to download historical stock data, clean the structure
for analysis, and save it locally in various formats such as Parquet, CSV, or Excel.
"""

import pandas as pd
import os
import yfinance as yf

def fetch_and_save_ticker(ticker, start, end, out_path):
    """
    Fetch historical stock price data from Yahoo Finance, clean it, and save locally.

    Automatically detects the save format (Parquet, CSV, Excel) based on the output file extension.
    The resulting DataFrame is sorted by date and indexed with a simple range index.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol (e.g., "NVDA").
    start : str
        Start date for historical data in "YYYY-MM-DD" format.
    end : str
        End date for historical data in "YYYY-MM-DD" format.
    out_path : str
        Destination path to save the cleaned file, including the file extension.

    Returns
    -------
    pandas.DataFrame
        The cleaned and saved DataFrame containing stock price history.
    """
    df = yf.download(ticker, start=start, end=end)

    # Handle possible MultiIndex columns
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df.columns.name = None
    df = df.reset_index()
    df = df.sort_values(by='Date')
    df.index = range(1, len(df) + 1)

    # Infer save format from file extension
    ext = os.path.splitext(out_path)[-1].lower()

    if ext == ".parquet":
        df.to_parquet(out_path)
    elif ext == ".csv":
        df.to_csv(out_path, index=False)
    elif ext in [".xlsx", ".xls"]:
        df.to_excel(out_path, index=False)
    else:
        raise ValueError(f"Unsupported save format based on extension: {ext}")

    return df