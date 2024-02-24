import pandas as pd
import clean

raw_data = pd.read_csv("raw-dataset.csv")
features = ['temperature', 'humidity', 'ph', 'label']

cleaned_data = clean.clean(raw_data,features)

