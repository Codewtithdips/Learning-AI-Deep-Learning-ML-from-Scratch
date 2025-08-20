#Create a 3x3 random matrix, normalize it, and compute its determinant.

import numpy as np

A = np.random.rand(3,3)

A_min = A.min()
A_max = A.max()

A_norm = (A - A_min) / (A_max  - A_min)

#print(A_norm)

det = np.linalg.det(A_norm)

#print(det)


import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 samples from standard normal distribution (mean=0, std=1)
samples = np.random.normal(loc=0, scale=1, size=1000)

# Plot histogram
plt.hist(samples, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Histogram of 1000 Normal Distribution Samples")
plt.xlabel("Value")
plt.ylabel("Frequency Density")

plt.show()

#print(samples)


#Linear Regression with Gradient Descent

import numpy as np
import matplotlib.pyplot as plt

# 1. Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)   # 100 samples, single feature
y = 4 + 3 * X + np.random.randn(100, 1)  # y = 4 + 3X + noise

# 2. Initialize parameters
w = np.random.randn(1)  # weight
b = np.random.randn(1)  # bias
lr = 0.1                # learning rate
epochs = 1000           # number of iterations

# 3. Training loop (Gradient Descent)
for i in range(epochs):
    # Predictions
    y_pred = w * X + b
    
    # Compute loss (MSE)
    loss = np.mean((y_pred - y) ** 2)
    
    # Compute gradients
    dw = (2/len(X)) * np.sum((y_pred - y) * X)
    db = (2/len(X)) * np.sum(y_pred - y)
    
    # Update parameters
    w -= lr * dw
    b -= lr * db
    
    # Print loss every 100 iterations
    if i % 100 == 0:
        print(f"Epoch {i}, Loss: {loss:.4f}, w: {w[0]:.4f}, b: {b[0]:.4f}")

# Final parameters
print(f"\nTrained Model: y = {w[0]:.2f}x + {b[0]:.2f}")

# 4. Plot results
plt.scatter(X, y, color="blue", label="Data")
plt.plot(X, w*X + b, color="red", label="Regression Line")
plt.legend()
plt.show()


#Build a simple neural network forward pass with NumPy.
import numpy as np

# Input: 5 samples, each with 3 features
X = np.random.randn(5, 3)

# Layer 1 (Hidden layer)
W1 = np.random.randn(3, 4)   # weights (3 inputs → 4 hidden units)
b1 = np.random.randn(1, 4)   # bias

# Layer 2 (Output layer)
W2 = np.random.randn(4, 2)   # weights (4 hidden → 2 outputs)
b2 = np.random.randn(1, 2)   # bias

# --- Forward Pass ---
# Hidden layer (Linear + ReLU)
Z1 = X @ W1 + b1        # Linear transform
A1 = np.maximum(0, Z1)  # ReLU activation

# Output layer (Linear + Softmax)
Z2 = A1 @ W2 + b2

# Softmax activation
exp_Z2 = np.exp(Z2 - np.max(Z2, axis=1, keepdims=True))  # stability trick
A2 = exp_Z2 / np.sum(exp_Z2, axis=1, keepdims=True)

print("Input (X):\n", X)
print("\nHidden layer activations (A1):\n", A1)
print("\nOutput probabilities (A2):\n", A2)
