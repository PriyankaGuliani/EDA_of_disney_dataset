"""
Created on Fri March 10 15:55:19 2023

@author: Priyanka Guliani

"""

import pandas as pd


def fill_null_values(df, method="bfill"):
    """
    Clean a column in a DataFrame by filling null values with the value
    from the next or previous column using the specified method.

    Parameters
    ---------
    df : pandas.DataFrame
        The DataFrame to fill missing values in.
    method : string
        The fill method to use. Default is 'bfill' (backward-fill).

    Returns
    --------
    pandas.DataFrame
        A new DataFrame with missing values filled using the specified method.

    Raises
    --------
    TypeError
        If the input `df` is not a Pandas DataFrame.
    ValueError
        If the input `method` is not a valid option for filling null values.

    Examples
    --------
    >>> fill_null_values(helper_data, "ffill")
        Year	Company 1	Company 2	Company 3	Company 4	Company 5
    0	2018	3204.0	1358.0	$5606	8,828	5028.0
    1	2019	3204.0	2073.0	$5606	9,832	6433.0

    """
    # Checks if a dataframe is the type of object
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a Pandas DataFrame")

    # Checks if a valid method of filling in the null
    # values in passed into the argument
    if method not in ["bfill", "ffill", "nearest"]:
        raise ValueError("Invalid method specified")

    # Fill null values with the value from the next or previous column
    df = df.fillna(method=method)

    # return the modified DataFrame
    return df


def clean_str(df, col_name):
    """
    Clean a column of a pandas DataFrame containing string representations
    of numbers. This function removes any non-numeric characters from the
    specified column and converts it to a float.

    Parameters
    ---------
    df : pandas.DataFrame
        The DataFrame containing the column to clean.
    col_name : string
        The name of the column to clean.

    Returns
    ---------
    pandas.DataFrame
        The DataFrame with the specified column cleaned and converted to float.

    Raises
    --------
    ValueError
        If the specified column does not exist in the dataframe.

    Examples
    --------
    >>> clean_str(helper_data, Company 3)
        Year	Company 1	Company 2	Company 3
    0	2018	3204.0	1358.0	5606.0
    1	2019	NaN	2073.0	NaN

    """
    # check if the column name entered is correct
    if col_name not in df.columns:
        raise ValueError(f"Column '{col_name}' does not exist in DataFrame")

    df[col_name] = df[col_name].replace("[^0-9.]", "", regex=True)
    df[col_name] = df[col_name].astype(float)

    # return the modified DataFrame.
    return df
