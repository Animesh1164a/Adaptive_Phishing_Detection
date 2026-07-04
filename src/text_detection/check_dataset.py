import pandas as pd

df = pd.read_csv("data/raw/phishing_dataset_with_category.csv")

print(df.columns)

print("\nLabel Counts:")
print(df["label"].value_counts())

print("\nCategory Counts:")
print(df["category"].value_counts())

print("\nTotal Rows:", len(df))