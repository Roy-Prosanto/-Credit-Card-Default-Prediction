# -Credit-Card-Default-Prediction
The objective of the Credit Card Default Prediction project is to develop a robust predictive model that can accurately identify the likelihood of a customer defaulting on their credit card payments. This helps financial institutions minimize risk, improve customer targeting, and manage credit effectively.
1. Data Collection and Preprocessing
Dataset Source: The dataset is sourced from Kaggle (default-of-credit-card-clients-dataset).
Initial Steps:
Loaded the dataset into a pandas DataFrame.
Inspected for missing values, duplicates, and unique values.
Data Cleaning: Dropped irrelevant columns like ID.
Exploratory Data Analysis (EDA):
Analyzed correlations using a heatmap to identify relationships between features.
Visualized payment history, bill amounts, and credit limits.
Used box plots and distribution plots to assess numerical data.![download](https://github.com/user-attachments/assets/10113843-26b8-481c-8cff-428cfa3d0342)

2. Feature Engineering
Separated the dataset into features (X) and the target variable (y), where y represents whether a customer defaults (default.payment.next.month).
Split the data into training and test sets (train_x, test_x, train_y, test_y) with an 80-20 ratio.
Scaled the features using StandardScaler to normalize data for model training.


4. Model Building and Evaluation
Model: Logistic Regression was used as the primary classifier.
Training: The model was trained on the preprocessed data.
Evaluation Metrics:
Classification report including precision, recall, F1-score.
Accuracy score to measure the overall performance.
5. Insights and Feature Importance
Feature Importance: Extracted from the logistic regression model to identify significant predictors of default.
Key Visualizations:
Plots illustrating distributions, payment behavior, and trends in default by demographic features (e.g., age, sex).
