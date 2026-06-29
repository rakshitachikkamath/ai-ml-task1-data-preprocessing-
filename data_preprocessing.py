import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because it has many missing values
df.drop("Cabin", axis=1, inplace=True)

# Encode categorical columns
encoder = LabelEncoder()

df["Sex"] = encoder.fit_transform(df["Sex"])
df["Embarked"] = encoder.fit_transform(df["Embarked"])

# Standardize numerical columns
scaler = StandardScaler()

df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])

# Boxplot before removing outliers
plt.figure(figsize=(6,4))
sns.boxplot(x=df["Fare"])
plt.title("Fare Boxplot")
plt.show()

# Remove outliers using IQR
Q1 = df["Fare"].quantile(0.25)
Q3 = df["Fare"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Fare"] >= Q1 - 1.5*IQR) &
        (df["Fare"] <= Q3 + 1.5*IQR)]

print("Final Shape:", df.shape)

# Save cleaned dataset
df.to_csv("Cleaned_Titanic.csv", index=False)

print("Preprocessing Completed Successfully!")