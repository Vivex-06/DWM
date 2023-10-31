import pandas as pd # Import pandas using 'pip install pandas' in terminal if not installed
import matplotlib.pyplot as plt  # Import matplotlib using 'pip install matplotlib' in terminal if not installed
from sklearn.cluster import KMeans # Import sklearn using 'pip install scikit-learn' in terminal if not installed

# Load the data
data = pd.read_csv(r"ab_data.csv")
print(data)

# Understand the data
print(data.isnull().sum())

# Features
features = data[["user_id", "converted"]]

# Model
model = KMeans(n_clusters=3)
res = model.fit_predict(features)
print(res)

# Clusters
data["clusters"] = res
print(data)
print(model.cluster_centers_)

# Scatter plot
x = data["user_id"]
y = data["converted"]
plt.scatter(x, y, c=data["clusters"])
plt.xlabel("user_id Value")
plt.ylabel("converted Value")
plt.show()
