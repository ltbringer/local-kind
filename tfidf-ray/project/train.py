import pickle
import json
from pathlib import Path

import requests
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier

print("Fetch datasets")
train = fetch_20newsgroups(subset="train", shuffle=True, random_state=42)
test = fetch_20newsgroups(subset="test", shuffle=True, random_state=42)

print("Vectorize data")
corpus = train.data
vectorizer = TfidfVectorizer()
x_train = vectorizer.fit_transform(corpus)

# decision tree classifier to predict the category of a post
# train the classifier
print("Train classifier")
clf = DecisionTreeClassifier()
clf.fit(x_train, train.target)

Path("artifacts").mkdir(exist_ok=True, parents=True)

print("Save artifacts")
with open("../artifacts/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

with open("../artifacts/classifier.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("../artifacts/target_names.json", "w") as f:
    json.dump(train.target_names, f)
