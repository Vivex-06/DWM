import pandas as pd  # Import pandas using 'pip install pandas' in terminal if not installed
from sklearn.naive_bayes import BernoulliNB # Import sklearn using 'pip install scikit-learn' in terminal

# Load the data
data = pd.read_csv(r"PlayTennis.csv") # Locate the 'PlayTennis.csv' file in the same folder you are running the code
print(data)

# Understand the data
print(data.isnull().sum())

# Feature and target
feature = data[["Outlook"]]
target = data["Play Tennis"]

# New features
new_feature = pd.get_dummies(feature, drop_first=True)
print(new_feature)

# Model
model = BernoulliNB()
model.fit(new_feature.values, target)

# Predict
we = input("1 for overcast, 2 for rainy, and 3 for sunny: ")
if we == "1":
    data = [[0, 0]]
elif we == "2":
    data = [[1, 0]]
else:
    data = [[0, 1]]
res = model.predict(data)
print(res)
