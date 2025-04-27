"""
Visualization utilities for financial data analysis.

This module contains modular plotting functions for visualizing stock prices,
technical indicators, and trading signals.
"""

import matplotlib.pyplot as plt

# --- One-off plots ---

def plot_moving_averages(df, windows=[30, 90, 180]):
    """
    Plot multiple moving averages of the stock.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    windows : list of int, optional
        List of window sizes for which to compute moving averages. Default is [30, 90, 180].

    Returns
    -------
    None
    """
    ax = df[['Close'] + [f"MA_{w}" for w in windows]].plot(figsize=(12, 6))
    ax.set_title("Moving Averages")
    return ax

# --- Individual plot elements ---

def plot_close_price(ax=None, df=None):
    """
    Plot the stock's closing price.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df['Date'], df['Close'], label="Closing Price", color='dodgerblue', alpha=0.6, zorder=2)

def plot_bollinger_bands(window, ax=None, df=None):
    """
    Plot Bollinger Bands on the stock price chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    window : int
        Window size used to compute the bollinger bands (e.g., 30 days).

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.fill_between(df['Date'], df[f"Upper_BB_{window}"], df[f"Lower_BB_{window}"],
                    label=f"{window}-day Bollinger Bands", color="orange", alpha=0.2, zorder=2)

def plot_moving_average(window, ax=None, df=None):
    """
    Plot the stock's moving average.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    window : int
        Window size used to compute the moving average (e.g., 30 days).

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(df['Date'], df[f"MA_{window}"], label=f"{window}-day MA", color="green", linestyle="--", alpha=1, zorder=3)

def plot_peaks_and_valleys(peaks_idx, valleys_idx, ax=None, df=None):
    """
    Plot Peaks and Valleys on the stock price chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    peaks_idx : list of int
        List containing indexes locating peaks.
    valleys_idx : list of int
        List containing indexes locating valleys.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.scatter(df['Date'].iloc[peaks_idx], df['Close'].iloc[peaks_idx],
               label="Resistance (Peaks)", color="red", marker="^", alpha=1, zorder=4)
    ax.scatter(df['Date'].iloc[valleys_idx], df['Close'].iloc[valleys_idx],
               label="Support (Valleys)", color="darkred", marker="v", alpha=1, zorder=4)

def plot_adx(window, ax=None, df=None):
    """
    Plot the stock's Average Directional Index (ADX).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    window : int
        Window size used to compute the ADX (e.g., 30 days).

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(df['Date'], df[f"ADX_{window}"], label="ADX", color="limegreen", alpha=0.6, zorder=5)

def plot_di_crosses(window, bullish_idx, bearish_idx, ax=None, df=None):
    """
    Plot Directional Indexes (+/-) on the stock price chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    window : int
        Window size used to compute the directional indeces (e.g., 30 days).
    bullish_idx : list of int
        List containing indexes locating bullish trends.
    bearish_idx : list of int
        List containing indexes locating bearish trends.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(df['Date'].iloc[bullish_idx], df[f"PLUS_DI_{window}"].iloc[bullish_idx],
               label="+DI", color="darkturquoise", marker="*", alpha=0.8, zorder=3)
    ax.scatter(df['Date'].iloc[bearish_idx], df[f"MINUS_DI_{window}"].iloc[bearish_idx],
               label="-DI", color="darkcyan", marker="*", alpha=0.8, zorder=3)

def plot_candlestick_patterns(ax=None, df=None):
    """
    Plot Candlestick Patterns on the stock price chart.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    for pattern, color in [('Doji_Significant', 'dimgrey'),
                           ('Engulfing_Significant', 'blue'),
                           ('Hammer_Significant', 'magenta')]:
        ax.scatter(df['Date'][df[pattern] > 0], df['Close'][df[pattern] > 0],
                   label=f"{pattern.split('_')[0]} Marker", color=color, marker="o", s=50, zorder=2)

def plot_rsi_crosses(overbought_idx, oversold_idx, ax=None, df=None):
    """
    Plot the stock's Relative Strength Index (RSI).
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    overbought_idx : list of int
        List containing indexes locating overbought crosses.
    oversold_idx : list of int
        List containing indexes locating oversold crosses.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(df['Date'][overbought_idx], df['Close'][overbought_idx],
               label="RSI Overbought Cross", color="orange", marker="P", zorder=3)
    ax.scatter(df['Date'][oversold_idx], df['Close'][oversold_idx],
               label="RSI Oversold Cross", color="hotpink", marker="P", zorder=3)

def plot_mfi_crosses(overbought_idx, oversold_idx, ax=None, df=None):
    """
    Plot the stock's Money Flow Index.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to plot on.
    df : pandas.DataFrame
        DataFrame containing necessary columns.
    overbought_idx : list of int
        List containing indexes locating overbought crosses.
    oversold_idx : list of int
        List containing indexes locating oversold crosses.

    Returns
    -------
    None
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    ax.scatter(df['Date'][overbought_idx], df['Close'][overbought_idx],
               label="MFI Overbought Cross", color="royalblue", marker="X", zorder=3)
    ax.scatter(df['Date'][oversold_idx], df['Close'][oversold_idx],
               label="MFI Oversold Cross", color="cornflowerblue", marker="X", zorder=3)

# --- Master Wrapper Function ---

def plot_financial_indicators(
    df,
    indicators=None,
    window_bb=None,
    window_dx=None,
    peaks_idx=None,
    valleys_idx=None,
    bullish_idx=None,
    bearish_idx=None,
    rsi_overbought_idx=None,
    rsi_oversold_idx=None,
    mfi_overbought_idx=None,
    mfi_oversold_idx=None,
    title="Stock Price with Financial Indicators"
):
    """
    Plot selected financial indicators on a stock price chart.

    Parameters
    ----------
    df : pandas.DataFrame
        Stock price data including indicators.
    indicators : list of str, optional
        List of indicators to plot. Choices:
        ['close', 'bollinger', 'moving_average', 'peaks_valleys', 'adx',
         'di_crosses', 'candlestick_patterns', 'rsi_crosses', 'mfi_crosses']
    window_bb : int, optional
        Window size used for Bollinger Bands and Moving Average.
    window_dx : int, optional
        Window size used for ADX and DI crosses.
    peaks_idx, valleys_idx, bullish_idx, bearish_idx, etc. : index arrays
        Precomputed indexes for peak/valley points and cross signals.
    title : str, optional
        Title of the plot.

    Returns
    -------
    None
    """
    if indicators is None:
        indicators = ['close']

    fig, ax = plt.subplots(figsize=(12, 6))

    if 'close' in indicators:
        plot_close_price(ax, df)
    if 'bollinger' in indicators and window_bb is not None:
        plot_bollinger_bands(ax, df, window_bb)
    if 'moving_average' in indicators and window_bb is not None:
        plot_moving_average(ax, df, window_bb)
    if 'peaks_valleys' in indicators and peaks_idx is not None and valleys_idx is not None:
        plot_peaks_and_valleys(ax, df, peaks_idx, valleys_idx)
    if 'adx' in indicators and window_dx is not None:
        plot_adx(ax, df, window_dx)
    if 'di_crosses' in indicators and bullish_idx is not None and bearish_idx is not None:
        plot_di_crosses(ax, df, window_dx, bullish_idx, bearish_idx)
    if 'candlestick_patterns' in indicators:
        plot_candlestick_patterns(ax, df)
    if 'rsi_crosses' in indicators and rsi_overbought_idx is not None and rsi_oversold_idx is not None:
        plot_rsi_crosses(ax, df, rsi_overbought_idx, rsi_oversold_idx)
    if 'mfi_crosses' in indicators and mfi_overbought_idx is not None and mfi_oversold_idx is not None:
        plot_mfi_crosses(ax, df, mfi_overbought_idx, mfi_oversold_idx)

    ax.set_ylabel("Price (USD)", color="black")
    ax.set_xlabel("Date", color="black")
    ax.tick_params(axis='y', labelcolor="black")
    ax.legend(loc="upper left")
    ax.set_title(title)
    plt.show()