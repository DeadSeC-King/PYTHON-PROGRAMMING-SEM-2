import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# ── 1. Load Data ──────────────────────────────────────────────────────────────
df = pd.read_csv('house_prices_dataset.csv')
print("Dataset Shape:", df.shape)
print("\nFirst 5 Rows:")
print(df.head())
print("\nData Types:")
print(df.dtypes)
print("\nMissing Values:")
print(df.isnull().sum())

# ── 2. Clean Data ─────────────────────────────────────────────────────────────
df = df.dropna()
df = df.drop_duplicates()
print("\nShape after cleaning:", df.shape)

# ── 3. Select Features & Target ───────────────────────────────────────────────
X = df[['square_feet', 'num_rooms', 'age', 'distance_to_city(km)']]
y = df['price']

# ── 4. Split Data (80% train, 20% test) ───────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples : {X_train.shape[0]}")
print(f"Testing  samples : {X_test.shape[0]}")

# ── 5. Train Model ────────────────────────────────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── 6. Predictions ────────────────────────────────────────────────────────────
y_pred = model.predict(X_test)

# ── 7. Evaluation Metrics ─────────────────────────────────────────────────────
mse  = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2   = r2_score(y_test, y_pred)

print("\n" + "="*45)
print("        MODEL EVALUATION RESULTS")
print("="*45)
print(f"  MSE  : {mse:,.2f}")
print(f"  RMSE : {rmse:,.2f}")
print(f"  R²   : {r2:.4f}")
print("="*45)

# ── 8. Model Coefficients ─────────────────────────────────────────────────────
print("\nModel Intercept :", round(model.intercept_, 2))
print("\nFeature Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"  {feature:<25} : {coef:,.4f}")