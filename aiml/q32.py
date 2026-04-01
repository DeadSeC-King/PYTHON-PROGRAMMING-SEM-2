"""
KNN Regression on Housing Dataset
----------------------------------
Predicts house PRICE using numeric features:
  area, bedrooms, bathrooms, stories, parking
"""

import numpy as np
import pandas as pd
from collections import Counter

# ── 1. Load & Preprocess ────────────────────────────────────────────────────
df = pd.read_csv("Housing.csv")

FEATURES = ["area", "bedrooms", "bathrooms", "stories", "parking"]
TARGET   = "price"

X = df[FEATURES].values.astype(float)
y = df[TARGET].values.astype(float)

# Normalise features (z-score) so no single feature dominates distance
X_mean = X.mean(axis=0)
X_std  = X.std(axis=0)
X_norm = (X - X_mean) / X_std

# ── 2. Train / Test Split ────────────────────────────────────────────────────
np.random.seed(42)
idx        = np.random.permutation(len(X_norm))
split      = int(0.8 * len(idx))
train_idx  = idx[:split]
test_idx   = idx[split:]

X_train, y_train = X_norm[train_idx], y[train_idx]
X_test,  y_test  = X_norm[test_idx],  y[test_idx]

# ── 3. KNN from Scratch ──────────────────────────────────────────────────────
def euclidean(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

def knn_predict_price(X_train, y_train, x_query, k=5):
    """Returns the mean price of the k nearest neighbours."""
    distances = np.array([euclidean(x_query, x) for x in X_train])
    k_idx     = np.argsort(distances)[:k]
    return y_train[k_idx].mean()

# ── 4. Evaluate ───────────────────────────────────────────────────────────────
def rmse(actual, predicted):
    return np.sqrt(np.mean((actual - predicted) ** 2))

def mae(actual, predicted):
    return np.mean(np.abs(actual - predicted))

for k in [3, 5, 7]:
    preds = np.array([knn_predict_price(X_train, y_train, x, k=k) for x in X_test])
    print(f"k={k}  |  RMSE: ₹{rmse(y_test, preds):>12,.0f}  |  MAE: ₹{mae(y_test, preds):>12,.0f}")

# ── 5. Sample Predictions ─────────────────────────────────────────────────────
print("\n── Sample Predictions (k=5) ───────────────────────────────────────────")
print(f"{'Actual Price':>15}  {'Predicted Price':>15}  {'Error %':>8}")
print("-" * 45)
k = 5
preds = np.array([knn_predict_price(X_train, y_train, x, k=k) for x in X_test])
for actual, pred in zip(y_test[:8], preds[:8]):
    err_pct = abs(actual - pred) / actual * 100
    print(f"₹{actual:>14,.0f}  ₹{pred:>14,.0f}  {err_pct:>7.1f}%")