"""
Utility functions for financial data analysis workflows.

This module contains general-purpose helper functions that support data validation,
column management, and preprocessing tasks across different stages of stock analysis projects.
"""

import pandas as pd

def ensure_column(df, column_name, generator_func, override=False):
    """
    Ensure that a specified column exists in the DataFrame, creating or overwriting it if necessary.

    If the column is missing or override is True, the column is generated using the provided generator function.

    Parameters
    ----------
    df : pandas.DataFrame
        The DataFrame to modify.
    column_name : str
        Name of the column to verify or create.
    generator_func : callable
        A zero-argument function that generates the column's values as a pandas Series.
    override : bool, optional
        Whether to forcibly recreate the column even if it already exists. Default is False.

    Returns
    -------
    pandas.DataFrame
        The modified DataFrame with the ensured column.
    """
    if override and column_name in df.columns:
        df.drop(columns=[column_name], inplace=True)

    if column_name not in df.columns:
        df[column_name] = generator_func()

    return df