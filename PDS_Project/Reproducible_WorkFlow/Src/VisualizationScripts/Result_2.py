import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'altair'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'holoviews'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'networkx'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'seaborn'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'matplotlib'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'mlxtend'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'altair-saver'])

#Basic necessary Libraries
import numpy as np
import pandas as pd

#Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')

#Apriori libraries 
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
from pathlib import Path
import os

cr_path = Path(os.getcwd())
par_path = cr_path.parent.absolute()
proj_path = str(par_path.parent.absolute())

df=pd.read_csv(proj_path + '\\ProcessedData\\PreProcessed.csv')

gender_df = df.groupby('gender').agg({'quantity': 'sum', 'total_price': 'sum'})

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Prepare the data for apriori algorithm
transactions = df.groupby(['invoice_date', 'category'])['quantity'].sum().unstack().reset_index().fillna(0).set_index('invoice_date')

# Convert the values to binary
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

transactions = transactions.applymap(encode_units)

# Apply the apriori algorithm
frequent_itemsets = apriori(transactions, min_support=0.05, use_colnames=True)

# Calculate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules

# Visualize the association rules
plt.figure(figsize=(10, 5))
sns.scatterplot(x=rules['support'], y=rules['confidence'], size=rules['lift'], hue=rules['lift'], palette='viridis')
plt.title('Association Rules Scatterplot')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.legend(title='Lift', loc='upper right')
plt.savefig(proj_path + '\\Outputs\\AssociationRulesScatterplot.png')

# Additional statistical analysis - describe the 'total_price' column
price_stats = df['total_price'].describe()
print(price_stats)

# Data visualization - boxplot for total prices by category
plt.figure(figsize=(10, 5))
sns.boxplot(x='category', y='total_price', data=df)
plt.title('Total Prices by Category')
plt.xlabel('Category')
plt.ylabel('Total Price')
plt.savefig(proj_path + '\\Outputs\\Total Prices by Category.png')


top_categories = df.groupby('category')['quantity'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_categories.index, y=top_categories.values)
plt.title('Top Categories by Quantity')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.savefig(proj_path + '\\Outputs\\TopCategoriesbyQuantity.png')

top_revenue_categories = df.groupby('category')['total_price'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_revenue_categories.index, y=top_revenue_categories.values)
plt.title('Top Categories by Revenue')
plt.xlabel('Category')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.savefig(proj_path + '\\Outputs\\TopCategoriesbyRevenue.png')

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig(proj_path + '\\Outputs\\DistributionofCustomerAge.png')

monthly_revenue = df.groupby(['year', 'month'])['total_price'].sum().reset_index()
monthly_revenue['year_month'] = monthly_revenue['year'].astype(str) + '-' + monthly_revenue['month'].astype(str)

plt.figure(figsize=(15, 5))
sns.lineplot(x='year_month', y='total_price', data=monthly_revenue)
plt.title('Monthly Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.savefig(proj_path + '\\Outputs\\Monthly Revenue Over Time.png')

age_revenue = df.groupby('age_cat')['total_price'].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=age_revenue.index, y=age_revenue.values)
plt.title('Revenue by Age Category')
plt.xlabel('Age Category')
plt.ylabel('Revenue')
plt.savefig(proj_path + '\\Outputs\\RevenuebyAgeCategory.png')

payment_revenue = df.groupby('payment_method')['total_price'].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=payment_revenue.index, y=payment_revenue.values)
plt.title('Total Revenue by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Revenue')
plt.savefig(proj_path + '\\Outputs\\TotalRevenuebyPaymentMethod.png')

average_price = df.groupby('category')['price'].mean()

plt.figure(figsize=(10, 5))
sns.barplot(x=average_price.index, y=average_price.values)
plt.title('Average Price per Item by Category')
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.savefig(proj_path + '\\Outputs\\AveragePriceperItembyCategory.png')

age_payment = df.groupby(['age_cat', 'payment_method'])['quantity'].sum().unstack()

age_payment.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.title('Relationship Between Age Category and Payment Method')
plt.xlabel('Age Category')
plt.ylabel('Quantity')
plt.savefig(proj_path + '\\Outputs\\RelationshipBetweenAgeCategoryandPaymentMethod.png')

exit = input()
