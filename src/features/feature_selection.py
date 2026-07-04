import os
import pandas as pd
from sklearn.feature_selection import mutual_info_classif

# Create folder
os.makedirs("reports/tables", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("data/processed/clean_dataset.csv")

# Features and Target
X = df.drop("Result", axis=1)
y = df["Result"]

# Mutual Information
mi = mutual_info_classif(X, y, random_state=42)

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": mi
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("="*60)
print("Top Features")
print("="*60)

print(importance)

importance.to_csv(
    "reports/tables/feature_importance.csv",
    index=False
)

print("\nFeature importance saved successfully.")