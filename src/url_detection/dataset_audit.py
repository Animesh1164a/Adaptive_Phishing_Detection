import pandas as pd

df = pd.read_csv("data/raw/PhiUSIIL_Phishing_URL_Dataset.csv")

print("="*60)
print("Dataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nMissing Values")
print(df.isnull().sum().sort_values(ascending=False).head(20))

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nLabel Distribution")
print(df["label"].value_counts())

print("\nCorrelation with Label")
corr = df.select_dtypes(include=["number"]).corr()["label"].sort_values(ascending=False)

print(corr)

