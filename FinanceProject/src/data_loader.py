import pandas as pd
import os

def load_data(path, file_type=None, date_col='Date'):
    """
    Load financial data from a file and return a pandas DataFrame.

    Supports CSV, Parquet, and Excel formats. Automatically parses the date column
    and resets the index to a range index starting from 1.

    Parameters
    ----------
    path : str
        Path to the data file.
    file_type : str, optional
        File type extension (e.g., "csv", "parquet", "xlsx"). If None, inferred from file extension.
    date_col : str, optional
        Name of the date column to parse and sort by. Default is "Date".

    Returns
    -------
    pandas.DataFrame
        Loaded and cleaned DataFrame with the date as a column and a range index.
    """

    if file_type is None:
        file_type = os.path.splitext(path)[-1].lower().lstrip('.')

    loaders = {
        'csv': lambda p: pd.read_csv(p, parse_dates=[date_col]),
        'parquet': lambda p: pd.read_parquet(p),
        'xlsx': lambda p: pd.read_excel(p, parse_dates=[date_col]),
    }

    if file_type not in loaders:
        raise ValueError(f"Unsupported file type: {file_type}")

    df = loaders[file_type](path)

    if date_col in df.columns:
        df = df.sort_values(by=date_col).reset_index(drop=True)
    else:
        raise ValueError(f"Expected '{date_col}' column not found.")

    df.index += 1
    return df
