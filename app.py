import os
import joblib
import requests
import streamlit as st

os.makedirs("models", exist_ok=True)

classifier_path = "models/classifier.pkl"
regressor_path = "models/regressor.pkl"


def download_from_gdrive(file_id, destination):
    # Remove corrupted/partial downloads if they exist
    if os.path.exists(destination):
        os.remove(destination)

    URL = "https://docs.google.com/uc?export=download&confirm=t"
    session = requests.Session()
    response = session.get(URL, params={"id": file_id}, stream=True)

    # Check for confirmation token if GDrive presents virus scan warning
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            response = session.get(
                URL,
                params={"id": file_id, "confirm": value},
                stream=True,
            )
            break

    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)


# Force download if model is missing or invalid HTML file size (< 100 KB)
if not os.path.exists(classifier_path) or os.path.getsize(classifier_path) < 100000:
    download_from_gdrive("1aD3GQ7uWyaeN5x9j4p2cpV1F8nuwenyr", classifier_path)

if not os.path.exists(regressor_path) or os.path.getsize(regressor_path) < 100000:
    download_from_gdrive("1iWT2Oot62sfbJxbCtJCbxPMCh_kgh9hf", regressor_path)

classifier = joblib.load(classifier_path)
regressor = joblib.load(regressor_path)