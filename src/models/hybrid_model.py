import os
import time
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import (
    RandomForestClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("data/processed/clean_dataset.csv")

X = df.drop("Result", axis=1)
y = df["Result"]

# -----------------------------
# Train Test Split
# -----------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Base Models
# -----------------------------

rf = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight="balanced"
)

xgb = XGBClassifier(
    random_state=42,
    eval_metric="logloss"
)

lgbm = LGBMClassifier(
    random_state=42
)

# -----------------------------
# Hybrid Voting Model
# -----------------------------

hybrid = VotingClassifier(

    estimators=[

        ("rf", rf),

        ("xgb", xgb),

        ("lgbm", lgbm)

    ],

    voting="soft"

)

# -----------------------------
# Training
# -----------------------------

start = time.time()

hybrid.fit(X_train, y_train)

training_time = time.time() - start

# -----------------------------
# Prediction
# -----------------------------

pred = hybrid.predict(X_test)

prob = hybrid.predict_proba(X_test)[:,1]

# -----------------------------
# Metrics
# -----------------------------

accuracy = accuracy_score(y_test,pred)

precision = precision_score(y_test,pred)

recall = recall_score(y_test,pred)

f1 = f1_score(y_test,pred)

auc = roc_auc_score(y_test,prob)

print("="*60)

print("HYBRID MODEL RESULTS")

print("="*60)

print(f"Accuracy : {accuracy:.4f}")

print(f"Precision: {precision:.4f}")

print(f"Recall   : {recall:.4f}")

print(f"F1 Score : {f1:.4f}")

print(f"ROC AUC  : {auc:.4f}")

print(f"Training Time : {training_time:.4f}")

print("\nClassification Report\n")

print(classification_report(y_test,pred))

print("\nConfusion Matrix\n")

print(confusion_matrix(y_test,pred))

# -----------------------------
# Save Model
# -----------------------------

os.makedirs("models/saved_models",exist_ok=True)

joblib.dump(

    hybrid,

    "models/saved_models/Hybrid_Model.pkl"

)

print("\nHybrid Model Saved Successfully.")

