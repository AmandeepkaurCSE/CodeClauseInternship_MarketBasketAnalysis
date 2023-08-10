#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# # Loading Dataset

# In[2]:


Data = pd.read_csv("Groceries_dataset.csv")
Data


# In[3]:


Data.head()


# In[4]:


Data.shape


# In[5]:


Data.info()


# In[6]:


Data.describe()


# In[7]:


Data.isnull().sum().sum()


# # Data Exploration

# In[8]:


X=Data["itemDescription"].value_counts().sort_values(ascending=False)[:5]
X = pd.DataFrame(X).reset_index()
# Rename columns
X.columns = ["itemDescription", "values"]
X


# In[9]:


plt.figure(figsize=(10, 6))  # Set the figure size 
a=sns.barplot(x="itemDescription", y="values", data=X)

# Add labels and title
plt.xlabel("Item Description")
plt.ylabel("Count")
plt.title("Top 5 Most Frequent Item Descriptions")
for x in a.containers:
    a.bar_label(x)
plt.show()


# In[10]:


# Load the data into a DataFrame
Data1 = pd.DataFrame(Data)

# Convert the "Date" column to datetime
Data1["Date"] = pd.to_datetime(Data1["Date"])

# Group data by month and calculate purchase frequency
monthly_purchase = Data1.groupby(Data1["Date"].dt.to_period("M")).size()

# Create a line plot for purchase frequency over time
plt.figure(figsize=(10, 6))
monthly_purchase.plot(kind="line", marker="o")
plt.title("Purchase Frequency Over Time (Monthly)")
plt.xlabel("Date (Month)")
plt.ylabel("Purchase Frequency")
plt.grid(True)
plt.show()


# In[11]:


purchase_count_per_member=pd.DataFrame(Data["Member_number"].value_counts().sort_values(ascending=False)[:9]).reset_index()
# Rename columns
purchase_count_per_member.columns = ["Member_number", "values"]
purchase_count_per_member


# In[12]:


# Sort the DataFrame by 'values' column
purchase_count_per_member = purchase_count_per_member.sort_values(by='values', ascending=False)

plt.figure(figsize=(10, 6))
a = sns.barplot(x="Member_number", y="values", data=purchase_count_per_member, order=purchase_count_per_member["Member_number"])
plt.title("Purchase Count per Member")
plt.xlabel("Member Number")
plt.ylabel("Purchase Count")

for x in a.containers:
    a.bar_label(x)

plt.show()


# # Apriori Algorithm

# The Apriori algorithm is an unsupervised algorithm used in machine learning for association rule mining, particularly in market basket analysis.
# 
# The primary objective of the Apriori algorithm is to identify frequent itemsets, which are sets of items that frequently occur together in the dataset. These frequent itemsets can then be used to generate association rules that capture patterns of co-occurrence between items.

# In[13]:


# Installed this package if it is not installed before
get_ipython().system('pip install mlxtend')


# In[14]:


from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[15]:


Data["Quantity"]=1


# In[16]:


Data


# In[17]:


Transactions=Data.groupby(["Member_number","itemDescription"])["Quantity"].sum().unstack().reset_index().set_index("Member_number")


# In[18]:


Transactions=Transactions.fillna(0)
Transactions


# In[19]:


def Encode(x):
    if x<=0:
        return 0
    elif x>0:
        return 1
Basket=Transactions.applymap(Encode)
Basket


# In[20]:


Frequent_itemset=apriori(Basket,min_support=0.06,use_colnames=True)
rules=association_rules(Frequent_itemset,metric="lift",min_threshold=1)


# In[21]:


rules.head()


# In[22]:


rules[(rules["confidence"]>0.5) & (rules["lift"]>1) ]

