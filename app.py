import os
import joblib
import gdown
import streamlit as st

os.makedirs("models", exist_ok=True)

classifier_path = "models/classifier.pkl"
regressor_path = "models/regressor.pkl"

# Download classifier using its File ID
if not os.path.exists(classifier_path):
    gdown.download(
        id="1aD3GQ7uWyaeN5x9j4p2cpV1F8nuwenyr",
        output=classifier_path,
        quiet=False,
    )

# Download regressor using its File ID
if not os.path.exists(regressor_path):
    gdown.download(
        id="1iWT2Oot62sfbJxbCTJCbxPMCh_kgh9hf",
        output=regressor_path,
        quiet=False,
    )

classifier = joblib.load(classifier_path)
regressor = joblib.load(regressor_path)