import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler

df = pd.read_csv("titanic.csv")
df = df.drop(columns=["PassengerId", "Name", "Ticket", "Cabin"])

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

print("\nMissing values:\n", df.isnull().sum())

X = df.drop("Survived", axis=1)

X_train, X_test = train_test_split(
    X, test_size=0.2, random_state=42
)

def show_scaling(scaler, name):
    X_scaled = scaler.fit_transform(X_train)

    print(f"\n{name} Scaling")

    print("\nBefore (Age, Fare):")
    print(X_train[["Age", "Fare"]].head())

    print("\nAfter (Age, Fare):")
    scaled_df = pd.DataFrame(X_scaled, columns=X_train.columns)
    print(scaled_df[["Age", "Fare"]].head())

show_scaling(MinMaxScaler(), "Min-Max")
show_scaling(StandardScaler(), "Z-Score (Standard)")
show_scaling(RobustScaler(), "Robust")
show_scaling(MaxAbsScaler(), "MaxAbs")