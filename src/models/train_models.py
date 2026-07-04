import os
import time
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# ----------------------------
# Load Dataset
# ----------------------------

df = pd.read_csv("data/processed/clean_dataset.csv")

X = df.drop("Result", axis=1)
y = df["Result"]

# ----------------------------
# Train Test Split
# ----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ----------------------------
# Models
# ----------------------------

models = {

    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=300,
            random_state=42,
            class_weight="balanced"
        ),

    "XGBoost":
        XGBClassifier(
            random_state=42,
            eval_metric="logloss"
        ),

    "LightGBM":
        LGBMClassifier(
            random_state=42
        )
}

# ----------------------------
# Train Models
# ----------------------------

results = []

os.makedirs("models/saved_models", exist_ok=True)
os.makedirs("models/metrics", exist_ok=True)

for name, model in models.items():

    print("="*60)
    print(name)
    print("="*60)

    start = time.time()

    model.fit(X_train, y_train)

    training_time = time.time() - start

    pred = model.predict(X_test)

    prob = model.predict_proba(X_test)[:,1]

    accuracy = accuracy_score(y_test, pred)

    precision = precision_score(y_test, pred)

    recall = recall_score(y_test, pred)

    f1 = f1_score(y_test, pred)

    auc = roc_auc_score(y_test, prob)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC AUC  : {auc:.4f}")
    print(f"Training Time : {training_time:.4f} sec")

    filename = name.replace(" ", "_") + ".pkl"

    joblib.dump(
        model,
        f"models/saved_models/{filename}"
    )

    results.append({
        "Model":name,
        "Accuracy":accuracy,
        "Precision":precision,
        "Recall":recall,
        "F1":f1,
        "ROC_AUC":auc,
        "Training_Time":training_time
    })

# ----------------------------
# Save Comparison
# ----------------------------

results = pd.DataFrame(results)

results.to_csv(
    "models/metrics/model_comparison.csv",
    index=False
)

print("\nAll Models Trained Successfully.")

