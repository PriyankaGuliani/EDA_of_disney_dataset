"""
Created on Fri March 10 16:45:43 2023

@author: Priyanka Guliani

This function creates a helper data to test the sample script created for
the sample solution to the Python Programming for Data Science project.
"""
from my_functions import fill_null_values
from my_functions import clean_str
import pandas as pd


def test_fill_null_values():

    # Create helper data
    helper_data = {
        "Year": ["2018", "2019", "2020", "2021", "2022"],
        "Company 1": [3204, None, 1327, None, 2528],
        "Company 2": [1358, 2073, 3508, None, 5195],
        "Company 3": ["$5606", None, "$6608", "$4,809", "$5432"],
        "Company 4": ["8,828", "9,832", None, "9,945", "10,334"],
        "Company 5": [5028, 6433, 7122, None, 7924],
    }
    # Save the helper_data as a dataframe
    helper_data = pd.DataFrame.from_dict(helper_data)
    filled_data = fill_null_values(helper_data, "ffill")

    # write tests for the function
    assert (
        filled_data.isnull().values.any() is False
    ), "Output dataframe has null values"
    assert filled_data.shape == (
        5,
        6,
    ), "The shape of the output dataframe is not correct"
    assert (
        filled_data.dtypes["Year"] == "object"
    ), "The datatype of the year column is not object"
    assert (
        filled_data.dtypes["Company 1"] == "float64"
    ), "The datatype of the Company 1 column is not float"
    assert (
        filled_data.dtypes["Company 3"] == "object"
    ), "The datatype of the Company 3 column is not object"
    assert (
        filled_data["Company 2"][3] == 3508
    ), "The null value has not been filled with the previous value from the df"
    assert (
        filled_data["Company 3"][1] == "$5606"
    ), "The null value has not been filled with the previous value from the df"
    assert (
        filled_data["Company 4"][2] == "9,832"
    ), "The null value has not been filled with the previous value from the df"

    return


test_fill_null_values()


def test_clean_str():
    # Using the same helper data
    helper_data = {
        "Year": ["2018", "2019", "2020", "2021", "2022"],
        "Company 1": [3204, None, 1327, None, 2528],
        "Company 2": [1358, 2073, 3508, None, 5195],
        "Company 3": ["$5606", None, "$6608", "$4,809", "$5432"],
        "Company 4": ["8,828", "9,832", None, "9,945", "10,334"],
        "Company 5": [5028, 6433, 7122, None, 7924],
    }

    # Save the helper_data as a dataframe
    helper_data = pd.DataFrame.from_dict(helper_data)
    cleaned_data = clean_str(helper_data, "Company 3")

    assert cleaned_data["Company 3"].dtype == float
    assert cleaned_data["Company 3"][0] == 5606, "Column has not been cleaned"
    assert cleaned_data["Company 3"][3] == 4809, "Column has not been cleaned"
    assert cleaned_data["Company 4"][0] == "8,828", "The output is not correct"

    return


test_clean_str()
