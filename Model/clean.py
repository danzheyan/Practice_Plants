import pandas as pd

def clean(data, columns_to_keep=[]):

    data.dropna(inplace=True)
    data.drop_duplicates(inplace=True)

    new_data = data[columns_to_keep]

    return new_data

def scale():
    ...