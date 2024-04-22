# Spotify User Behavior Analysis Project

The project utilizes the Spotify User Behavior Dataset sourced from Kaggle, comprising 520 samples and 20 features, primarily categorical or nominal. This dataset offers valuable insights into Spotify users' behavior patterns and preferences within the platform.

## Project Overview

### 1. Data Import and Database Setup
- Utilizes `config.py`, `main.py`, and `database.ini` to import CSV data into a PostgreSQL database.
- Configures connection settings using psycopg2, enabling SQL access and Python analysis.

### 2. Exploratory Data Analysis (EDA) and Model Training
- In the `Spotify_User_classification.ipynb` notebook:
  - Conducts EDA to unveil user preferences like favorite music genre, listening slots, and mood.
  - Trains a subscription willingness classification model with meticulous data preprocessing, label encoding, and handling of missing values.
  - Achieves up to 85% accuracy in predicting users' premium plan subscription willingness.
  - Visualizes significant features impacting classification using Lasso and Chi-Square feature selection methods.

### 3. User Behavioral Clustering
- Implements behavioral clustering to group users based on their attitude towards premium plans.
- Analyzes Spotify usage habits (e.g., when, where, why, and what they listen to) and correlates them with subscription willingness.
- Answers questions like "How do users with subscription willingness differ in behavior from those without?"

This project offers a comprehensive exploration of Spotify user behavior, empowering researchers, analysts, and data scientists to delve into user interactions and engagement metrics within the platform.

