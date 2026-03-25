import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("Housing.csv")

# ---------- Encoding ----------

# yes/no → binary
binary_cols = ['mainroad', 'guestroom', 'basement', 
               'hotwaterheating', 'airconditioning', 'prefarea']

for col in binary_cols:
    df[col] = df[col].map({'yes': 1, 'no': 0})

# One-hot encoding (IMPORTANT FIX)
df = pd.get_dummies(df, columns=['furnishingstatus'], drop_first=True)

# ---------- Features ----------
X = df.drop('price', axis=1)
y = df['price']

# ---------- Split 60/20/20 ----------
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.4, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

# ---------- Model ----------
model = RandomForestRegressor(
    n_estimators=500,      # more trees = better stability
    max_depth=None,        # allow full growth
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)

model.fit(X_train, y_train)

# ---------- Prediction ----------
y_pred = model.predict(X_test)

# ---------- Metrics ----------
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MSE:", mse)
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)