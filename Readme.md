# Sentiment Analysis of Burmese Music Comments

## Project Overview

This project focuses on sentiment analysis of Burmese music comments using MyanBERTa and mBERT. The repository contains code, datasets, and models used in training and evaluating the sentiment analysis model.

## Folder Structure

### `code_google_colab`

This folder contains the code used to train the model and filter comments, as well as to create CSV files. The scripts follow a step-wise naming convention:

- `_s1`: Initial processing and filtering of comments.
- `_s2`: Model training.
- `_s3`: Model evaluation and testing.
- `comment_filtered.py`: Used in various steps, so no step suffix is added.

### `csv`

This folder contains datasets used for training and evaluation.

- `1st_model_comments/`: Stores three CSV files that were manually differentiated and used for training `model_1`. Though not crucial, they are kept as a record.
- `doublej_filtered_comments_with_id.csv`: Generated after running `_s1`.
- `filtered_data.csv`: Manually labeled dataset (positive, negative, neutral) based on `Rules.ipynb` and then this datasets is used in `_s2`.
- `Predicted1000.csv`:  Generated after running `_s3`. `Yellow` and `Red`  entries are manually highlighted as they contradict `Rules`.

### `models`

Contains trained sentiment analysis models:

- `model1/` (model trained on about 400 comments)
- `model2/` (model trained on about 5000 comments)

These models are uploaded to Google Drive and accessed via Google Colab for execution.

### `SA_webapp`

This folder includes two subfolders, each corresponding to a different trained model. The code structure remains the same, but both models are included for comparative purposes.

## Running the Web Application

To test the model using the web API in VS Code, follow these steps:

1. Open the respective main folder:
   - `SA_400_1/` (model1_app)
   - `SA_5000_2/` (model2_app)

2. Open a terminal and activate the virtual environment:
   ```sh
   source venv/bin/activate

3. To install the required dependencies, run the following command:
   ```sh
   pip install -r requirements.txt

4. Run FastAPI server:
   ```sh
   uvicorn backend.app:app --reload
   
5. After hosting backend to test with curl:
   ```sh  
    curl -X 'POST' \
    'http://localhost:8000/predict/' \
    -H 'Content-Type: application/json' \
    -d '{"text": "အရမ်း ကြိုက်တယ် အဲဒီသီချင်"}'
