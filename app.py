import os
import joblib
import requests
import streamlit as st

os.makedirs("models", exist_ok=True)

classifier_path = "models/classifier.pkl"
regressor_path = "models/regressor.pkl"


def download_from_gdrive(file_id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(
        URL, params={"id": file_id, "confirm": "t"}, stream=True
    )

    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)


if not os.path.exists(classifier_path):
    download_from_gdrive("1aD3GQ7uWyaeN5x9j4p2cpV1F8nuwenyr", classifier_path)

if not os.path.exists(regressor_path):
    download_from_gdrive("1iWT2Oot62sfbJxbCtJCbxPMCh_kgh9hf", regressor_path)

classifier = joblib.load(classifier_path)
regressor = joblib.load(regressor_path)