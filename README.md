## CodeClauseInternship Market Basket Analysis

#### Importing Libraries: 
I have imported necessary libraries like NumPy, Pandas, Matplotlib, Seaborn, and the MLxtend library for association rule mining.

#### Loading and Exploring Data: 
Dataset link : https://www.kaggle.com/datasets/heeraldedhia/groceries-dataset
I have loaded a dataset named "Groceries_dataset.csv" using Pandas and performed initial data exploration. I have displayed the shape, info, and summary statistics of the dataset.

#### Data Visualization: 
I have created visualizations using Seaborn to explore the data. I have created bar plots to visualize the top 5 most frequent item descriptions and a line plot to show the purchase frequency over time (monthly).
Purchase Count Analysis: You've analyzed the purchase count per member and created a bar plot to visualize the purchase count for the top 9 members.
![Screenshot (162)](https://github.com/AmandeepkaurCSE/CodeClauseInternship_MarketBasketAnalysis/assets/64351796/c16102da-dd41-441f-94fb-e03b5199b1cc)

![Screenshot (166)](https://github.com/AmandeepkaurCSE/CodeClauseInternship_MarketBasketAnalysis/assets/64351796/20ab9feb-21ce-48d8-b733-58717ab4cd08)


![Screenshot (163)](https://github.com/AmandeepkaurCSE/CodeClauseInternship_MarketBasketAnalysis/assets/64351796/18857115-6365-475f-9c6d-d0f1ef835f00)

#### Apriori Algorithm: 
I have used the Apriori algorithm from the MLxtend library to perform association rule mining. I have prepared the data by encoding it into binary format, indicating the presence or absence of items in each transaction.

#### Association Rules: 
I have generated association rules using the Apriori algorithm and calculated various metrics like support, confidence, and lift for the rules.I have filtered and displayed the rules based on certain conditions.
![Screenshot (165)](https://github.com/AmandeepkaurCSE/CodeClauseInternship_MarketBasketAnalysis/assets/64351796/6a4304f9-9238-4b41-b717-d908b76fd409)


#### Summary: 
As a theory or conclusion, the code demonstrates the process of loading, exploring, visualizing, and analyzing transactional data. It then applies the Apriori algorithm to mine association rules that indicate the likelihood of purchasing certain items together.
