import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def clean(data: pd.DataFrame, columns_to_keep=[]) -> pd.DataFrame:
    # Removing Duplicates and Null Values
    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    # Removing Outliers using IQR
    numeric_data = data.select_dtypes(include="number")

    Q1 = numeric_data.quantile(0.25)
    Q3 = numeric_data.quantile(0.75)
    IQR = Q3 - Q1

    clean_data = numeric_data[~((numeric_data < (Q1 - 1.5 * IQR)) | (numeric_data > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Selecting Columns of interest
    new_data = clean_data[columns_to_keep]

    return new_data


def scale(data):
    ...
