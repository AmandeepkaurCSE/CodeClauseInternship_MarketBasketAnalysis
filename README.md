## CodeClauseInternship MarketBasketAnalysis

#### Importing Libraries: 
I have imported necessary libraries like NumPy, Pandas, Matplotlib, Seaborn, and the MLxtend library for association rule mining.

#### Loading and Exploring Data: 
I have loaded a dataset named "Groceries_dataset.csv" using Pandas and performed initial data exploration. I have displayed the shape, info, and summary statistics of the dataset.

#### Data Visualization: 
I have created visualizations using Seaborn to explore the data. I have created bar plots to visualize the top 5 most frequent item descriptions and a line plot to show the purchase frequency over time (monthly).
Purchase Count Analysis: You've analyzed the purchase count per member and created a bar plot to visualize the purchase count for the top 9 members.

#### Apriori Algorithm: 
I have used the Apriori algorithm from the MLxtend library to perform association rule mining. I have prepared the data by encoding it into binary format, indicating the presence or absence of items in each transaction.

#### Association Rules: 
I have generated association rules using the Apriori algorithm and calculated various metrics like support, confidence, and lift for the rules.I have filtered and displayed the rules based on certain conditions.

#### Summary: 
As a theory or conclusion, the code demonstrates the process of loading, exploring, visualizing, and analyzing transactional data. It then applies the Apriori algorithm to mine association rules that indicate the likelihood of purchasing certain items together.
