"""
Feature engineering utilities for stock price prediction.

This module provides functions to create technical indicators and rolling statistics
such as moving averages, Bollinger Bands, and rolling minimum/maximum prices
for financial time series data.
"""

import pandas as pd
import numpy as np

def add_moving_averages(df, windows=[30, 90, 180]):
    """
    Add simple moving average columns for specified window sizes.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'Close' column.
    windows : list of int, optional
        List of window sizes for which to compute moving averages. Default is [30, 90, 180].

    Returns
    -------
    pandas.DataFrame
        DataFrame with additional 'MA_{window}' columns.
    """
    for window in windows:
        df[f"MA_{window}"] = df['Close'].rolling(window).mean()
    return df

def add_rolling_min_max(df, window=120):
    """
    Add rolling minimum and maximum price columns over a specified window.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'Close' column.
    window : int, optional
        Size of the rolling window. Default is 120.

    Returns
    -------
    pandas.DataFrame
        DataFrame with 'Rolling_Min' and 'Rolling_Max' columns added.
    """
    df['Rolling_Min'] = df['Close'].rolling(window).min()
    df['Rolling_Max'] = df['Close'].rolling(window).max()
    return df

def add_bollinger_bands(df, window=20):
    """
    Add Bollinger Bands columns based on a rolling mean and standard deviation.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing a 'Close' column.
    window : int, optional
        Window size for calculating the rolling mean and standard deviation. Default is 20.

    Returns
    -------
    pandas.DataFrame
        DataFrame with 'BB_upper' and 'BB_lower' columns added.
    """
    ma = df['Close'].rolling(window).mean()
    std = df['Close'].rolling(window).std()
    df['BB_upper'] = ma + (2 * std)
    df['BB_lower'] = ma - (2 * std)
    return df