"""
Technical indicator utilities for financial time series data.

This module provides functions to compute additional technical metrics such as
percentage change, and serves as a foundation for integrating more complex indicators
like RSI, MFI, and ADX in stock price analysis.
"""

import pandas as pd

def add_pct_change(df):
    """
    Add daily percentage change in closing price.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'Close' column.

    Returns
    -------
    pandas.DataFrame
        DataFrame with an added 'Pct_Change' column representing daily returns.
    """
    df['Pct_Change'] = df['Close'].pct_change()
    return df