# Gold Price Prediction using Machine Learning

A beginner-friendly Machine Learning project that predicts **gold prices** based on financial market indicators.
This project includes a trained ML model and a simple **Flask web interface** where users can enter values and get predictions instantly.


## Project Overview

Gold prices are influenced by multiple global factors such as stock markets, oil prices, currency exchange rates, and other precious metals.
This project uses historical data to train a Machine Learning model that learns patterns and estimates future gold prices.

Users can interact with the model through a simple web frontend.

## How It Works (Simple Flow)

User Inputs → Flask App → ML Model → Predicted Gold Price

1. User enters financial values in the frontend.
2. Flask sends the data to the trained model.
3. The model predicts the gold price.
4. Result is displayed on the webpage.

## Input Features Explained

* **SPX** – Stock market index value.
* **Oil Price (USO)** – Oil market indicator (inflation impact).
* **Silver Price (SLV)** – Precious metal trend indicator.
* **EUR/USD** – Currency exchange rate affecting gold pricing.

These inputs help the model understand market conditions.


## Tech Stack

* Python
* Machine Learning (Scikit-learn)
* Pandas & NumPy
* Matplotlib / Seaborn
* Flask (Backend)
* HTML + CSS (Frontend)


## Project Structure

gold-price-prediction/
│
├── app.py                 # Flask application
├── gold_model.pkl         # Trained ML model
├── goldprice.ipynb        # Model training notebook
├── templates/
│    └── index.html        # Frontend UI
└── README.md


## How to Run the Project (Beginner Steps)

### 1️. Clone the repository

git clone https://github.com/YOUR-USERNAME/Gold-Price-Prediction.git
cd Gold-Price-Prediction


### 2️. Install required libraries

pip install -r requirements.txt

### 3️. Run the Flask app

python app.py

### 4️. Open in browser

http://127.0.0.1:5000

## Features

 Machine Learning price prediction
 Simple beginner-friendly UI
 Real-time prediction using Flask
 Clean project structure


## Future Improvements

* Add charts for visualization
* Deploy online using Render or Railway
* Improve UI design
* Add live market data API

## Author

Hemasri M
