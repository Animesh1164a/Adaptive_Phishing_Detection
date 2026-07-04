import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, StackingClassifier

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# =============================================

print("="*60)
print("Loading Runtime Dataset")
print("="*60)

df = pd.read_csv(
    "data/raw/PhiUSIIL_Phishing_URL_Dataset.csv"
)

# =============================================
# Columns that cannot be generated at runtime
# =============================================

drop_columns = [

    "FILENAME",
    "URL",
    "Domain",
    "TLD",
    "Title",

    "LineOfCode",
    "LargestLineLength",

    "DomainTitleMatchScore",
    "URLTitleMatchScore",

    "HasSocialNet",
    "HasCopyrightInfo",

    "NoOfSelfRef",
    "NoOfEmptyRef",
    "NoOfExternalRef"

]

existing = [c for c in drop_columns if c in df.columns]

df.drop(columns=existing, inplace=True)

df.fillna(0, inplace=True)

print("\nDataset Shape :", df.shape)

# =============================================

X = df.drop("label", axis=1)

y = df["label"]

# =============================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# =============================================

rf = RandomForestClassifier(

    n_estimators=200,

    random_state=42,

    n_jobs=-1

)

xgb = XGBClassifier(

    random_state=42,

    eval_metric="logloss",

    n_jobs=-1

)

lgb = LGBMClassifier(

    random_state=42,

    n_jobs=-1

)

# =============================================

model = StackingClassifier(

    estimators=[

        ("rf", rf),

        ("xgb", xgb),

        ("lgb", lgb)

    ],

    final_estimator=LogisticRegression(),

    stack_method="predict_proba",

    cv=3,

    n_jobs=-1

)

# =============================================

print("\nTraining Runtime Model...\n")

model.fit(X_train, y_train)

# =============================================

pred = model.predict(X_test)

prob = model.predict_proba(X_test)[:,1]

# =============================================

print("="*60)
print("RUNTIME MODEL RESULTS")
print("="*60)

print("Accuracy :", accuracy_score(y_test,pred))
print("Precision:", precision_score(y_test,pred))
print("Recall   :", recall_score(y_test,pred))
print("F1 Score :", f1_score(y_test,pred))
print("ROC AUC  :", roc_auc_score(y_test,prob))

print("\n")

print(classification_report(y_test,pred))

print(confusion_matrix(y_test,pred))

# =============================================

os.makedirs(

    "models/saved_models",

    exist_ok=True

)

joblib.dump(

    model,

    "models/saved_models/Runtime_URL_Model.pkl"

)

joblib.dump(

    list(X.columns),

    "models/saved_models/runtime_features.pkl"

)

print("\nRuntime Model Saved Successfully")

print("Feature Count :", len(X.columns))

