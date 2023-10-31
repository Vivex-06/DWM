"""
    A humble advice: (Remove the comment if it acts as a hindrance)
    Do not try to install libraries and dependecies in your home system while trying to execute the code,
    make use of Anaconda and run the code on cloud environment with pre-installed dependencies.
"""

import pandas as pd 
from mlxtend.frequent_patterns import apriori 
from mlxtend.frequent_patterns import association_rules


# Load the dataset from the Excel file
df = pd.read_excel('Online_Retail.xlsx')

# Data Preprocessing
# Drop rows with missing values in the 'InvoiceNo' and 'Description' columns
df.dropna(subset=['InvoiceNo', 'Description'], inplace=True)

# Convert the 'InvoiceNo' column to a string for proper grouping
df['InvoiceNo'] = df['InvoiceNo'].astype(str)

# Group items by 'InvoiceNo' and 'Description' and sum the quantities
basket = (df[df['Quantity'] > 0]
 .groupby(['InvoiceNo', 'Description'])['Quantity']
 .sum().unstack().reset_index().fillna(0)
 .set_index('InvoiceNo'))

# Convert quantities to binary values (1 for purchased, 0 for not)
def encode_units(x):
 if x <= 0:
    return 0
 if x >= 1:
    return 1
basket_sets = basket.applymap(encode_units)

# Perform the Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(basket_sets, min_support=0.05, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric='lift', min_threshold=1.0)

# Display the frequent itemsets and association rules
print("Frequent Itemsets:")
print(frequent_itemsets)
print("\nAssociation Rules:")
print(rules)
