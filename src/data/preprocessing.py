import pandas as pd

# Dataset Load
df = pd.read_csv("data/raw/dataset.csv")

print("="*60)
print("DATASET INFORMATION")
print("="*60)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nTarget Class Distribution:")
print(df["Result"].value_counts())

print("\nStatistical Summary:")
print(df.describe())

# Remove index column if present
if "index" in df.columns:
    df.drop(columns=["index"], inplace=True)

# Convert labels
# -1 = Legitimate (0)
#  1 = Phishing (1)

df["Result"] = df["Result"].replace({
    -1:0,
     1:1
})

print("\nUpdated Labels:")
print(df["Result"].value_counts())

# Save Clean Dataset

import os

...

os.makedirs("data/processed", exist_ok=True)

df.to_csv("data/processed/clean_dataset.csv", index=False)

print("Clean Dataset Saved Successfully.")
