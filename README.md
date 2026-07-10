# 🎬 Movie Rating Prediction using Machine Learning

A Flask-based Machine Learning web application that predicts the IMDb rating of a movie based on its features such as Genre, Director, Actors, Release Year, Duration, and Number of Votes.

---

## 📌 Project Overview

Movie ratings are influenced by several factors, including genre, cast, director, audience engagement, and runtime. This project uses historical movie data to train a Machine Learning model capable of predicting a movie's rating.

The application provides an easy-to-use web interface where users can enter movie details and receive an estimated IMDb rating instantly.

---

## 🚀 Features

- 🎬 Predict movie ratings using Machine Learning
- 📊 Data preprocessing and feature engineering
- 📈 Exploratory Data Analysis (EDA)
- 🤖 Random Forest Regression model
- 🌐 Flask web application
- 🎨 Modern responsive user interface
- 💾 Model saved using Joblib
- ⚡ Instant prediction results

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Flask

### Machine Learning
- Random Forest Regressor

### Frontend
- HTML
- CSS
- JavaScript

---

## 📂 Project Structure

```
Movie_Rating_Prediction/
│
├── app.py
├── movie_rating_model.pkl
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── dataset/
│   └── IMDb Movies India.csv
│
└── notebook/
    └── Movie_Rating_Prediction.ipynb
```

---

## 📊 Dataset

The dataset contains historical information about Indian movies, including:

- Movie Name
- Year
- Genre
- Director
- Actor 1
- Actor 2
- Actor 3
- Duration
- Number of Votes
- IMDb Rating

---

## 🔍 Data Preprocessing

The following preprocessing steps were performed:

- Handling missing values
- Cleaning Year column
- Cleaning Duration column
- Cleaning Votes column
- Feature selection
- One-Hot Encoding for categorical features
- Train-Test Split

---

## 📈 Exploratory Data Analysis

The project includes various visualizations such as:

- Rating Distribution
- Genre Distribution
- Director Analysis
- Actor Analysis
- Votes Distribution
- Duration Distribution
- Correlation Heatmap
- Rating vs Votes
- Rating vs Duration

---

## 🤖 Machine Learning Model

Algorithm Used:

- Random Forest Regressor

Pipeline Includes:

- Simple Imputer
- One-Hot Encoder
- Column Transformer
- Random Forest Regression

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| Mean Absolute Error (MAE) | 0.80 |
| Root Mean Squared Error (RMSE) | 1.08 |
| R² Score | 0.37 |

> **Note:** The model performance may vary depending on the dataset split and preprocessing techniques.

---

## 💻 Web Application

Users can enter:

- Genre
- Director
- Actor 1
- Actor 2
- Actor 3
- Release Year
- Duration
- Votes

The application predicts the estimated IMDb rating of the movie.

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/movie-rating-prediction.git
```

Move into the project directory

```bash
cd movie-rating-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Flask application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000/
```

---

## 📷 Application Preview

Add screenshots of:

- Home Page
- Prediction Form
- Prediction Result

---

## 🌟 Future Improvements

- Improve model accuracy
- Compare multiple regression algorithms
- Add dropdown lists for movie features
- Deploy using Docker
- Integrate with an online movie database API
- Add movie poster support
- Improve UI with interactive visualizations

---

## 👨‍💻 Author

**Krishna Rajoo**

Data Science Student

---

## 📜 License

This project is created for educational and learning purposes.