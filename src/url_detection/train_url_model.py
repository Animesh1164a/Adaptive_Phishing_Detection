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
    confusion_matrix,
    classification_report
)

from sklearn.linear_model import LogisticRegression

from sklearn.ensemble import (
    RandomForestClassifier,
    StackingClassifier
)

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# ====================================

print("Loading Dataset...")

df = pd.read_csv(
    "data/raw/PhiUSIIL_Phishing_URL_Dataset.csv"
)

# ====================================

drop_columns = [

    "FILENAME",

    "URL",

    "Domain",

    "TLD",

    "Title"

]

df.drop(columns=drop_columns,inplace=True)

# ====================================

print(df.shape)

print(df.isnull().sum().sum())

# ====================================

df = df.fillna(0)

# ====================================

X = df.drop("label",axis=1)

y = df["label"]

# ====================================

X_train,X_test,y_train,y_test=train_test_split(

    X,

    y,

    test_size=0.20,

    stratify=y,

    random_state=42

)

# ====================================

rf=RandomForestClassifier(

    n_estimators=300,

    random_state=42

)

xgb=XGBClassifier(

    random_state=42,

    eval_metric="logloss"

)

lgb=LGBMClassifier(

    random_state=42

)

# ====================================

model=StackingClassifier(

    estimators=[

        ("rf",rf),

        ("xgb",xgb),

        ("lgb",lgb)

    ],

    final_estimator=LogisticRegression(),

    stack_method="predict_proba",

    cv=5,

    n_jobs=-1

)

# ====================================

print("Training Model...")

model.fit(

    X_train,

    y_train

)

# ====================================

pred=model.predict(X_test)

prob=model.predict_proba(X_test)[:,1]

# ====================================

print("="*60)

print("URL MODEL RESULTS")

print("="*60)

print(

"Accuracy :",

accuracy_score(y_test,pred)

)

print(

"Precision:",

precision_score(y_test,pred)

)

print(

"Recall:",

recall_score(y_test,pred)

)

print(

"F1:",

f1_score(y_test,pred)

)

print(

"ROC:",

roc_auc_score(y_test,prob)

)

print()

print(

classification_report(

    y_test,

    pred

)

)

print(

confusion_matrix(

    y_test,

    pred

)

)

# ====================================

os.makedirs(

"models/saved_models",

exist_ok=True

)

joblib.dump(

model,

"models/saved_models/URL_Model.pkl"

)

print("Model Saved Successfully")