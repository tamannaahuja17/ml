# -*- coding: utf-8 -*-
"""Copy of Eshaan ML Prac File

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10FaQ_0snriw281B46FhfgCxo6Cz3V3TZ

## Name - Eshaan R James
## Roll No - 16031
## ML Practical File
"""

!pip install pandoc
import pandoc

"""### 1. Naive Bayes Classification

#### Using Sklearn
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train model
model = GaussianNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy (sklearn Naive Bayes):", accuracy_score(y_test, y_pred))

"""### 2. Simple Linear Regression

#### Using sklearn
"""

# importing required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


#loading dataset
house_df = pd.read_csv("/content/drive/MyDrive/House_Price - Sheet1.csv") # practice This and Manual One
print(house_df.head())

print("Columns in Datast: ", house_df.columns)

# Area vs Price Plot

plt.figure(figsize = (12, 6))
plt.scatter(house_df['Area '], house_df['Prices '])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price')
plt.show()

# Df splitting

X = house_df['Area '].values.reshape(-1, 1)
y = house_df['Prices '].values.reshape(-1, 1)

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

uni_lin_reg = LinearRegression()
uni_lin_reg.fit(X_train, y_train)

# Model Parameters
print(f"""
Regression Intercept (bias): {uni_lin_reg.intercept_}
Regression Coefficient (weight): {uni_lin_reg.coef_}""")

# Testing

price = 100*uni_lin_reg.coef_ + uni_lin_reg.intercept_
print("Predicted price: ", price)

"""#### Manual Implementation"""

# importing required modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

#loading dataset
house_df = pd.read_csv("/content/drive/MyDrive/House_Price - Sheet1.csv")
print(house_df.head())

print("Columns in Datast: ", house_df.columns)

# Area vs Price Plot

plt.figure(figsize = (12, 6))
plt.scatter(house_df['Area '], house_df['Prices '])
plt.xlabel('Area')
plt.ylabel('Price')
plt.title('Area vs Price')
plt.show()

# Df splitting

X = house_df['Area ']
y = house_df['Prices ']

# Model Building

n = len(X)
x_mean = np.mean(X)
y_mean = np.mean(y)

# Determining parameters
m = np.sum((X - x_mean) * (y - y_mean)) / np.sum((X - x_mean)**2) #least square method
c = y_mean - m * x_mean

# Model Parameters
print(f"""
Regression Intercept (bias): {c}
Regression Coefficient (weight): {m}""")

# Testing

price = 100*m + c
print("Predicted price: ", price)

"""Gradient Descent"""

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 2.5, 3.5, 4.0, 4.5])

# Hyperparameters
w0 = 0.5
w1 = 0.5
learning_rate = 0.007
epochs = 100

m = len(x)
loss_history = []

# Gradient Descent
for epoch in range(epochs):
    # Predicted values using polynomial model
    y_pred = w0 + w1*x

    # Compute the gradients
    dw0 = -(1/m) * np.sum(y - y_pred)
    dw1 = -(1/m) * np.sum((y - y_pred) * x)

    # Update weights
    w0 -= learning_rate * dw0
    w1 -= learning_rate * dw1
    loss = np.mean((y - y_pred) ** 2)  # Mean Squared Error
    loss_history.append(loss)

    if epoch % 10 == 0:
        print(f'Epoch {epoch}: Loss = {loss:.3f}, w0 = {w0:.3f}, w1 = {w1:.3f}')

# Final weights after training
print(f'Final weights: w0 = {w0:.3f}, w1 = {w1:.3f}')

# Plot
plt.figure(figsize=(10, 6))
plt.plot(loss_history, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs Epoch')
plt.legend()
plt.grid()
plt.show()

"""### 3. Multiple Linear Regression

#### Using Sklearn
"""

from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
diabetes = load_diabetes()
x  = diabetes.data
y = diabetes.target
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Model Building
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R2 Score: {r2_score(y_test, y_pred)}")
# Print the params
print(f"Coefficients: {model.coef_}")
print(f"Intercept: {model.intercept_}")

"""#### Manual"""

import numpy as np
import pandas as pd
import seaborn as sns
# Multivarite Linear Regression using the normal equation.
x=np.array([[1,100,3],[1,300,7],[1,500,4]]) # features
y=np.array([300,700,600]) # target

# estimating parameters
xt=x.T
xtx=xt@x
xinv=np.linalg.inv(xtx)
xty=xt@y
b=xinv@xty # using the normal equation

print(f"""
Intercept: {b[0]}
Coefficient of 1st feature: {b[1]}
Coefficient of 2nd feature: {b[2]}""")

x_new = [1, 450, 8]
y_pred = x_new@b
print("Predicted value ", y_pred)

"""Gradient Descent

"""

import numpy as np
import matplotlib.pyplot as plt

# Data (let's assume we have 2 features, x1 and x2)
X = np.array([[1, 1, 3],
              [1, 2, 6],
              [1, 3, 9],
              [1, 4, 12],
              [1, 5, 15]])  # First column is bias term (all 1s), next columns are features
y = np.array([2, 2.5, 3.5, 4.0, 4.5])

# Hyperparameters
w = np.array([0.5, 0.5, 0.5])  # Initial weights for bias, w1, w2 (for two features)
learning_rate = 0.01
epochs = 1000

m = len(X)
loss_history = []

# Gradient Descent
for epoch in range(epochs):
    # Predicted values using the model
    y_pred = X @ w  # X is (m x n) and w is (n x 1), result is (m x 1)

    # Compute the gradients
    dw = -(1/m) * X.T @ (y - y_pred)

    # Update weights
    w -= learning_rate * dw
    loss = np.mean((y - y_pred) ** 2)  # Mean Squared Error
    loss_history.append(loss)

    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss = {loss:.3f}, w = {w}')

# Final weights after training
print(f'Final weights: w = {w}')

# Plot the loss history
plt.figure(figsize=(10, 6))
plt.plot(loss_history, label='Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss vs Epoch')
plt.legend()
plt.grid()
plt.show()

"""### 4. Polynomial Regression

#### Using Sklearn
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Load diabetes dataset
diabetes = datasets.load_diabetes()
X = diabetes.data[:, 2:3]
y = diabetes.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Polynomial features
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train linear regression
model = LinearRegression()
model.fit(X_train_poly, y_train)

# Predictions
y_pred = model.predict(X_test_poly)


r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"R² Score: {r2:.4f}")
print(f"Mean Squared Error: {mse:.2f}")

# Plot (for 1 feature)
plt.scatter(X_test, y_test, color='black', label='Actual')
x_range = np.linspace(X_test.min(), X_test.max(), 100).reshape(-1, 1)
x_range_poly = poly.transform(x_range)
y_range_pred = model.predict(x_range_poly)
plt.plot(x_range, y_range_pred, color='blue', label='Polynomial Regression')
plt.xlabel('BMI (feature)')
plt.ylabel('Target')
plt.title('Polynomial Regression on Diabetes Data')
plt.legend()
plt.grid(True)
plt.show()

"""### 5. Lasso and Ridge Regression

#### Lasso Using Sklearn
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)

# Predict
y_pred = lasso.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output
print("Lasso Coefficients:", lasso.coef_)
print("Intercept:", lasso.intercept_)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

"""#### Ridge using SKlearn"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
ridge = Ridge(alpha=1.0)
ridge.fit(X_train, y_train)

# Predictions
y_pred = ridge.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Output
print("Ridge Coefficients:", ridge.coef_)
print("Intercept:", ridge.intercept_)
print(f"Mean Squared Error: {mse:.2f}")
print(f"R² Score: {r2:.2f}")

"""### 6. Logistic Regression

#### Using Sklearn
"""

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target


threshold = y.mean()
y_binary = (y > threshold).astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression(max_iter=1000)  # Increase max_iter if needed
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Below Mean", "Above Mean"], yticklabels=["Below Mean", "Above Mean"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

"""#### Manual using Gradient Descent"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn import datasets
from sklearn.model_selection import train_test_split

diabetes = datasets.load_diabetes()
X = diabetes.data
y = diabetes.target
threshold = y.mean()
y=(y>threshold).astype(int) #converting y into binary output taking mean as thrshold.


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



m, n = X_train.shape
w = np.random.randn(n)*0.2 # or w=np.zero() + 0.2
b=0
alpha=0.9
epochs=10001

def sigmoid(z):
  return 1/(1+np.exp(-z))

def binary_cross_entropy(y_true, y_pred):
  ep = 1e-7 # to avoid log(0) error
  return -np.mean(y_true*np.log(y_pred+ep) + (1-y_true)*np.log(1-y_pred+ep))

losses = []

for epoch in range(epochs):
  z = X_train@w + b
  predictions = sigmoid(z)
  error = predictions - y_train

  # GRADIENT
  dw = (1/m) * X_train.T@error
  db = (1/m) * np.sum(error)

  # update parameters

  w -= alpha * dw
  b -= alpha * db

  # calculate loss
  loss = binary_cross_entropy(y_train, predictions)
  losses.append(loss)

  # print loss every 100 epochs
  if epoch % 1000 == 0:
    print(f"Epoch {epoch}: Loss = {loss:.4f}")

# predict the test set
z_test = np.dot(X_test, w) + b
y_pred_test = sigmoid(z_test)
y_pred_class=(y_pred_test>0.5).astype(int)

# Accuracy
accuracy = np.mean(y_pred_class == y_test)
print(f"Accuracy: {accuracy*100:.4f}")

# Plot loss curve
plt.plot(losses)
plt.xlabel('Epochs')
plt.ylabel('Binary Cross-Entropy Loss')
plt.title('Training Loss Curve')
plt.show()

"""### 7. Artificial Neural Network

#### USing Sklearn
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling is important for neural networks
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train the ANN model
model = MLPClassifier(hidden_layer_sizes=(10,), activation='relu', solver='adam',
                      max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

"""#### Manual"""

#Artificial Neural Network

from joblib.numpy_pickle_utils import xrange
from numpy import *

class NeuralNet(object):
    def __init__(self):
        # Generate random numbers
        random.seed(1)

        # Assign random weights to a 3 x 1 matrix,
        self.synaptic_weights = 2 * random.random((3, 1)) - 1

    # The Sigmoid function
    def __sigmoid(self, x):
        return 1 / (1 + exp(-x))

    # The derivative of the Sigmoid function.
    # This is the gradient of the Sigmoid curve.
    def __sigmoid_derivative(self, x):
        return x * (1 - x)

    # Train the neural network and adjust the weights each time.
    def train(self, inputs, outputs, training_iterations):
        for iteration in xrange(training_iterations):
            # Pass the training set through the network.
            output = self.learn(inputs)

            # Calculate the error
            error = outputs - output

            # Adjust the weights by a factor
            factor = dot(inputs.T, error * self.__sigmoid_derivative(output))
            self.synaptic_weights += factor

        # The neural network thinks.

    def learn(self, inputs):
        return self.__sigmoid(dot(inputs, self.synaptic_weights))


if __name__ == "__main__":
    # Initialize
    neural_network = NeuralNet()

    # The training set.
    inputs = array([[0, 1, 1], [1, 0, 0], [1, 0, 1]])
    outputs = array([[1, 0, 1]]).T

    # Train the neural network
    neural_network.train(inputs, outputs, 10000)

    # Test the neural network with a test example.
    print(neural_network.learn(array([1, 0, 1])))

"""### 8. K-NN Classification

#### Using Sklearn
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Building
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# Predict on test data
y_pred = knn.predict(X_test)

# Evaluate
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%\n")
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

"""#### Manual"""

# Importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dataset preparation
iris_df = datasets.load_iris()
x = iris_df.data
y = iris_df.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Finding feature mean and Std
feature_means = np.mean(x_train, axis=0)
feature_stds = np.std(x_train, axis=0)

# Z-score normalisation
X_train_normalized = (x_train - feature_means) / feature_stds
X_test_normalized = (x_test - feature_means) / feature_stds

# Imlement knn for 3 features
def knn_predict(X_train, Y_train, X_test, k=3):
    predictions = []

    for test_sample in x_test:
      # Euclidean dstace
      distances = np.sqrt(np.sum((x_train - test_sample)**2, axis=1))

      # Get indices of K nearest neighbours
      nearest_indices = np.argsort(distances)[:k]

      # Get lbels of nearest neigbhours
      nearest_labels = y_train[nearest_indices]

      # Predict  most common label
      unique, counts = np.unique(nearest_labels, return_counts=True)
      predicted_label = unique[np.argmax(counts)]

      predictions.append(predicted_label)

    return np.array(predictions)

knn_predict(x_train, y_train, x_test)

"""###9. Decision Tree Classification

#### Using Sklearn
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = datasets.load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

Dtreeclf = DecisionTreeClassifier(max_features=1, criterion = "gini")
Dtreeclf.fit(X_train, y_train)

y_pred = Dtreeclf.predict(X_test)

print(f"Accuracy = {accuracy_score( y_test, y_pred)}")

# Plot Decision Tree
plt.figure(figsize=(12, 8))
plot_tree(Dtreeclf,
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          filled=True,
          rounded=True)
plt.title("Decision Tree - Iris Dataset")
plt.show()

"""###10. SVM Classification

####Using Sklearn
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# Define pipeline with scaling and SVM
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42))
])

# Train the model
pipeline.fit(X_train, y_train)

# Make predictions
y_pred = pipeline.predict(X_test)

# Evaluation
print(f"Test Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Plot confusion matrix
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('SVM Confusion Matrix on Iris Dataset')
plt.tight_layout()
plt.show()

"""###11. K-Means Clustering

#### Using Sklearn
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load the Iris dataset
iris = load_iris()
X = iris.data

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Reduce dimensions for visualization using PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
centroids_pca = pca.transform(centroids)

# Plotting clusters
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=50, label='Data Points')
plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], c='red', s=200, marker='X', label='Centroids')
plt.title('K-Means Clustering on Iris Dataset (PCA-Reduced)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()
plt.grid(True)
plt.show()

"""#### Manual"""

import numpy as np
import matplotlib.pyplot as plt

# Sample data (2D for easy visualization)
X = np.array([
    [1, 2], [1.5, 1.8], [5, 8],
    [8, 8], [1, 0.6], [9, 11]
])

# Number of clusters
k = 2

# Randomly choose k data points as initial centroids
np.random.seed(42)
initial_indices = np.random.choice(len(X), k, replace=False)
centroids = X[initial_indices]

# Function to calculate Euclidean distance
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# K-means algorithm
max_iters = 100
for _ in range(max_iters):
    # Step 1: Assign clusters
    clusters = [[] for _ in range(k)]
    for point in X:
        dists = [distance(point, centroid) for centroid in centroids]
        cluster_idx = np.argmin(dists)
        clusters[cluster_idx].append(point)

    # Step 2: Update centroids
    new_centroids = []
    for cluster in clusters:
        if cluster:
            new_centroids.append(np.mean(cluster, axis=0))
        else:
            new_centroids.append(np.random.rand(2))  # handle empty cluster
    new_centroids = np.array(new_centroids)

    # Stop if centroids don't change
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

# Final cluster assignments
final_labels = []
for point in X:
    dists = [distance(point, centroid) for centroid in centroids]
    final_labels.append(np.argmin(dists))

# Plot result
X = np.array(X)
final_labels = np.array(final_labels)
colors = ['r', 'g']
for i in range(k):
    plt.scatter(X[final_labels == i, 0], X[final_labels == i, 1], c=colors[i], label=f'Cluster {i}')
plt.scatter(centroids[:, 0], centroids[:, 1], c='blue', marker='x', s=100, label='Centroids')
plt.title("Manual K-Means Clustering")
plt.legend()
plt.show()

"""### 12. Hierarchial Clustering

#### Using Sklearn
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target  # True labels (only for evaluation, not used in clustering)

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply Agglomerative Clustering
model = AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = model.fit_predict(X_scaled)

# Visualization (first 2 features)
plt.figure(figsize=(8, 5))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=labels, palette="Set1")
plt.title('Hierarchical Clustering (Agglomerative)')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()