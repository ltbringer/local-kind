import pickle
import json
from typing import Dict, List, Union

from starlette.requests import Request
from ray import serve

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier


@serve.deployment
class Sklearn20NewsGroupsClf:
    def __init__(
        self,
        model: DecisionTreeClassifier,
        vectorizer: TfidfVectorizer,
        target_names: List[str],
    ):
        self.model = model
        self.vectorizer = vectorizer
        self.target_names = target_names

    async def __call__(self, request: Request) -> Dict[str, Union[str, float]]:
        data = await request.json()
        x_test = self.vectorizer.transform([data["text"]])
        preds = self.model.predict_proba(x_test)
        return {
            "class": self.target_names[preds.argmax()],
            "confidence": preds.max(),
        }


def load_artifacts() -> (
    Dict[str, Union[DecisionTreeClassifier, TfidfVectorizer, List[str]]]
):
    with open("./artifacts/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    with open("./artifacts/classifier.pkl", "rb") as f:
        model = pickle.load(f)
    with open("./artifacts/target_names.json", "r") as f:
        target_names = json.load(f)
    return {"model": model, "vectorizer": vectorizer, "target_names": target_names}


app = Sklearn20NewsGroupsClf.bind(**load_artifacts())
serve.run(app, route_prefix="/")
