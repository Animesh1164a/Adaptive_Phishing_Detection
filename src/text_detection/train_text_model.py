import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    classification_report,
    confusion_matrix
)

print("="*60)
print("Loading SMS Spam Dataset")
print("="*60)

df = pd.read_csv(
    "data/raw/sms_spam_dataset.csv",
    encoding="latin1"
)

# Keep only required columns
df = df[["v1","v2"]]

df.columns = ["label","text"]

# Convert labels
df["label"] = df["label"].map({
    "ham":0,
    "spam":1
})

print(df.head())

print("\nLabel Distribution")
print(df["label"].value_counts())

# ----------------------------

X = df["text"]

y = df["label"]

X_train,X_test,y_train,y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

# ----------------------------

vectorizer = TfidfVectorizer(

    stop_words="english",

    max_features=5000

)

X_train = vectorizer.fit_transform(X_train)

X_test = vectorizer.transform(X_test)

# ----------------------------

models = {

    "Logistic Regression": LogisticRegression(max_iter=1000),

    "Naive Bayes": MultinomialNB()

}

best_model = None

best_accuracy = 0

# ----------------------------

for name,model in models.items():

    print("\n"+"="*60)

    print(name)

    print("="*60)

    model.fit(X_train,y_train)

    pred = model.predict(X_test)

    prob = model.predict_proba(X_test)[:,1]

    acc = accuracy_score(y_test,pred)

    print("Accuracy :",acc)

    print("Precision:",precision_score(y_test,pred))

    print("Recall   :",recall_score(y_test,pred))

    print("F1 Score :",f1_score(y_test,pred))

    print("ROC AUC  :",roc_auc_score(y_test,prob))

    print()

    print(classification_report(y_test,pred))

    print(confusion_matrix(y_test,pred))

    if acc>best_accuracy:

        best_accuracy=acc

        best_model=model

# ----------------------------

os.makedirs(

    "models/saved_models",

    exist_ok=True

)

joblib.dump(

    best_model,

    "models/saved_models/Text_Model.pkl"

)

joblib.dump(

    vectorizer,

    "models/saved_models/tfidf_vectorizer.pkl"

)

print("\nBest Text Model Saved Successfully")