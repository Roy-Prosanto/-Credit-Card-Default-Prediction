# -*- coding: utf-8 -*-
"""Credit Card Default Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1y0pd0rocURyKYSwwM6JtlfEH_N1eYN9W
"""

# Commented out IPython magic to ensure Python compatibility.
import os
import kagglehub
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,classification_report

# Download latest version
path = kagglehub.dataset_download("uciml/default-of-credit-card-clients-dataset")

print("Path to dataset files:", path)

# List files in the downloaded directory
print("Files in the directory:", os.listdir(path))

plt.style.use("ggplot")
# %matplotlib inline

df=pd.read_csv(path+"/UCI_Credit_Card.csv")
df.head()

df.describe()

df.isnull().sum() # isnull means is your data has  any misssingvalu  or not

df.duplicated().sum()

df.nunique() # how many unique (distinct)

# EDA  part start
correlation_matrix = df.corr()
plt.figure(figsize=(20, 15 ))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

pyment_history_colums =  ['PAY_0', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']
for col in pyment_history_colums:
  sns.countplot(x=col, hue= "default.payment.next.month", data=df)
  plt.xticks(rotation=90)
  plt.title(f'Payment History Column: {col}')
  plt.show()

for i in range (1,7):
  plt.figure(figsize=(20,10))
  plt.subplot(1,2,1)
  sns.histplot(df [f'BILL_AMT{i}'],bins=30,kde=True)
  plt.title(f'Bill amount{i}')
  plt.xlabel('Bill Amount')
  plt.ylabel('Count')


  plt.subplot(1,2,2)
  sns.histplot(df [f'BILL_AMT{i}'],bins=30,kde=True)
  plt.title(f'pyment amount{i}')
  plt.xlabel('pyment Amount')
  plt.ylabel('Count')

  plt.tight_layout()
  plt.show()

sns.boxenplot(x='default.payment.next.month',y='LIMIT_BAL',data=df)
plt.title('Age Balance vs Default Payment')
plt.show()

plt.figure(figsize=(20,10))
plt.title('Amount of credit limite')
sns.distplot(df['LIMIT_BAL'],bins=200,kde=True)
plt.show()

class_0 = df.loc[df['default.payment.next.month'] == 0]
class_1 = df.loc[df['default.payment.next.month'] == 1]
plt.figure(figsize=(20,10))
plt.title('Amount of credit limite')
sns.distplot(class_0['LIMIT_BAL'],bins=200,kde=True)
sns.distplot(class_1['LIMIT_BAL'],bins=200,kde=True)
plt.show()

df = df.drop(['ID'], axis=1)
df.head()

sns.countplot(x='SEX', hue='default.payment.next.month', data=df)
plt.title('Sex vs Default Payment')
plt.show()

sns.histplot(df["AGE"],bins=30 ,kde =True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(20,10))
sns.boxenplot(data=df)
plt.show()

"""### MLA using"""

# Assuming 'default payment next month' is the actual column name:
y = df["default.payment.next.month"]  # Target variable
x = df.drop("default.payment.next.month", axis=1)  # Features

# Corrected the typo from 'trian_x' to 'train_x'
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)

df.shape

train_x.shape

train_y.shape

"""### Building the ML"""

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


model.fit(train_x, train_y)
y_prediction = model.predict(test_x)
print(classification_report(test_y, y_prediction))

y_prediction

accuracy_score(test_y, y_prediction)

repot = classification_report(test_y, y_prediction)
repot

# Calculate and display feature importance
features_importance = pd.Series(model.coef_[0], index=X.columns)
features_importance = features_importance.abs().sort_values(ascending=False)

import pandas as pd
from sklearn.linear_model import LogisticRegression

# Assuming 'train_x' and 'test_x' were created from a DataFrame called 'X'
# If not, replace 'X' with the actual DataFrame containing your features
features_importance = pd.Series(model.coef_[0], index=train_x.columns)
# or test_x.columns if they have the same columns as original X

features_importance = features_importance.abs().sort_values(ascending=False)
print(features_importance)