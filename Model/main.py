import pandas as pd
import process

raw_data = pd.read_csv("raw-dataset.csv")
features = ["temperature", "humidity", "ph"]

cleaned_data = process.clean(raw_data, features)
scaled_data = process.scale(cleaned_data)

