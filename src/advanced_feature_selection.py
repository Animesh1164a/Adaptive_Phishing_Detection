import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.feature_selection import (
    mutual_info_classif,
    SelectKBest,
    chi2
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

df = pd.read_csv("data/processed/clean_dataset.csv")

X = df.drop("Result", axis=1)
y = df["Result"]

os.makedirs("reports/tables", exist_ok=True)
os.makedirs("reports/graphs", exist_ok=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

mi = mutual_info_classif(
    X_train,
    y_train,
    random_state=42
)

mi_df = pd.DataFrame({

    "Feature":X.columns,

    "Mutual_Information":mi

}).sort_values(
    by="Mutual_Information",
    ascending=False
)

X_positive = X_train.copy()

for col in X_positive.columns:
    X_positive[col] = X_positive[col] - X_positive[col].min()

chi_selector = SelectKBest(
    score_func=chi2,
    k="all"
)

chi_selector.fit(
    X_positive,
    y_train
)

chi_df = pd.DataFrame({

    "Feature":X.columns,

    "ChiSquare":chi_selector.scores_

}).sort_values(
    by="ChiSquare",
    ascending=False
)

rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

rf.fit(
    X_train,
    y_train
)

rf_df = pd.DataFrame({

    "Feature":X.columns,

    "RF_Importance":rf.feature_importances_

}).sort_values(
    by="RF_Importance",
    ascending=False
)

perm = permutation_importance(

    rf,

    X_test,

    y_test,

    random_state=42,

    n_repeats=10

)

perm_df = pd.DataFrame({

    "Feature":X.columns,

    "Permutation":perm.importances_mean

}).sort_values(
    by="Permutation",
    ascending=False
)

final_df = mi_df.merge(
    chi_df,
    on="Feature"
)

final_df = final_df.merge(
    rf_df,
    on="Feature"
)

final_df = final_df.merge(
    perm_df,
    on="Feature"
)

final_df.to_csv(

    "reports/tables/advanced_feature_ranking.csv",

    index=False

)

print(final_df)


plt.figure(figsize=(12,8))

plt.barh(
    rf_df["Feature"],
    rf_df["RF_Importance"]
)

plt.title("Random Forest Feature Importance")

plt.tight_layout()

plt.savefig(
    "reports/graphs/rf_feature_importance.png"
)

plt.show()

