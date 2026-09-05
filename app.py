import os
import joblib
import gdown
import streamlit as st

os.makedirs("models", exist_ok=True)

classifier_path = "models/classifier.pkl"
regressor_path = "models/regressor.pkl"

# Download classifier using direct URL and fuzzy matching
if not os.path.exists(classifier_path):
    url_clf = "https://drive.google.com/file/d/1aD3GQ7uWyaeN5x9j4p2cpV1F8nuwenyr/view?usp=sharing"
    gdown.download(url_clf, classifier_path, quiet=False, fuzzy=True)

# Download regressor using direct URL and fuzzy matching
if not os.path.exists(regressor_path):
    url_reg = "https://drive.google.com/file/d/1iWT2Oot62sfbJxbCtJCbxPMCh_kgh9hf/view?usp=share_link"
    gdown.download(url_reg, regressor_path, quiet=False, fuzzy=True)

classifier = joblib.load(classifier_path)
regressor = joblib.load(regressor_path)