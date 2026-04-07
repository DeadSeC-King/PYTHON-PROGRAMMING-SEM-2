"""
K-Means Clustering on Housing Dataset
---------------------------------------
Segments houses into clusters using:
  price, area, bedrooms, bathrooms, stories, parking
"""

import numpy as np
import pandas as pd

# ── 1. Load & Preprocess ────────────────────────────────────────────────────
df = pd.read_csv("Housing.csv")

FEATURES = ["price", "area", "bedrooms", "bathrooms", "stories", "parking"]
X = df[FEATURES].values.astype(float)

# Normalise (z-score) — essential for K-Means
X_mean = X.mean(axis=0)
X_std  = X.std(axis=0)
X_norm = (X - X_mean) / X_std

# ── 2. K-Means from Scratch ──────────────────────────────────────────────────
def kmeans(X, k, max_iters=100, tol=1e-4, seed=42):
    np.random.seed(seed)

    # Random initialisation: pick k data points as starting centroids
    init_idx  = np.random.choice(len(X), k, replace=False)
    centroids = X[init_idx].copy()

    labels = np.zeros(len(X), dtype=int)

    for iteration in range(max_iters):
        # Assignment step: each point → nearest centroid
        dists  = np.linalg.norm(X[:, None] - centroids[None, :], axis=2)  # (N, k)
        new_labels = np.argmin(dists, axis=1)

        # Update step: move centroids to cluster mean
        new_centroids = np.array([
            X[new_labels == c].mean(axis=0) if (new_labels == c).any() else centroids[c]
            for c in range(k)
        ])

        shift = np.linalg.norm(new_centroids - centroids)
        centroids = new_centroids
        labels    = new_labels

        if shift < tol:
            print(f"Converged at iteration {iteration + 1}")
            break

    # Inertia (WCSS)
    inertia = sum(
        np.sum((X[labels == c] - centroids[c]) ** 2)
        for c in range(k)
    )
    return labels, centroids, inertia

# ── 3. Run for k = 3 clusters ────────────────────────────────────────────────
K = 3
labels, centroids, inertia = kmeans(X_norm, k=K)
df["cluster"] = labels

# ── 4. Cluster Profiles (in original scale) ───────────────────────────────────
print(f"\n── K-Means Clustering  (k={K}) ─────────────────────────────────────────")
print(f"Inertia (WCSS): {inertia:,.2f}\n")

for c in range(K):
    subset = df[df["cluster"] == c]
    print(f"Cluster {c}  ({len(subset)} houses)")
    print(f"  Avg Price     : ₹{subset['price'].mean():>12,.0f}")
    print(f"  Avg Area      : {subset['area'].mean():>8.0f} sqft")
    print(f"  Avg Bedrooms  : {subset['bedrooms'].mean():>8.1f}")
    print(f"  Avg Bathrooms : {subset['bathrooms'].mean():>8.1f}")
    print(f"  Avg Stories   : {subset['stories'].mean():>8.1f}")
    print(f"  Avg Parking   : {subset['parking'].mean():>8.1f}")
    print()

