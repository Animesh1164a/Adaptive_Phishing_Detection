import os
import pandas as pd
import matplotlib.pyplot as plt

# Create folders automatically
os.makedirs("reports/graphs", exist_ok=True)
os.makedirs("reports/tables", exist_ok=True)

# Load Dataset
df = pd.read_csv("data/processed/clean_dataset.csv")

print("="*60)
print("DATASET OVERVIEW")
print("="*60)

print(df.head())

print("\nShape :", df.shape)

print("\nColumns :")
print(df.columns.tolist())

# Save statistical summary
summary = df.describe().T
summary.to_csv("reports/tables/statistical_summary.csv")

print("\nStatistical summary saved.")

plt.figure(figsize=(6,5))

df["Result"].value_counts().plot(
    kind="bar"
)

plt.title("Class Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Samples")

plt.tight_layout()

plt.savefig("reports/graphs/class_distribution.png")

plt.show()


import seaborn as sns

plt.figure(figsize=(16,12))

sns.heatmap(
    df.corr(),
    cmap="coolwarm",
    center=0
)

plt.title("Feature Correlation Heatmap")

plt.tight_layout()

plt.savefig("reports/graphs/correlation_heatmap.png")

plt.show()


plt.figure(figsize=(6,6))

df["Result"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Phishing vs Legitimate")

plt.savefig("reports/graphs/class_piechart.png")

plt.show()


plt.figure(figsize=(18,8))

df.boxplot(rot=90)

plt.tight_layout()

plt.savefig("reports/graphs/boxplot.png")

plt.show()


df.hist(
    figsize=(18,18)
)

plt.tight_layout()

plt.savefig("reports/graphs/all_histograms.png")

plt.show()

