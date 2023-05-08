# PDS_Significant
Team-Significant

#Basic necessary Libraries
import numpy as np
import pandas as pd

#Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# The dataset used for the analysis (customer_shopping_data.csv)
df = pd.read_csv('customer_shopping_data.csv')

# Drop Unnecessary columns [Customer_id, invoice_no, shopping_mall]
df = df.drop(['customer_id','invoice_no','shopping_mall'], axis=1)

* Data Visualization - Gender Distribution.
df['invoice_date'] = pd.to_datetime(df['invoice_date'])

* Year
df['year'] = df['invoice_date'].dt.strftime("%Y")

* Month
df['month'] = df['invoice_date'].dt.strftime("%m")

* Weekday
df['weekday'] = df['invoice_date'].dt.strftime("%w")

* Day
df['day'] = df['invoice_date'].dt.strftime("%d")

* Total Price
df['total_price'] = df['quantity'] * df['price']
def age_cat(age):
    if age < 18:
        return 'Tennagers'
    elif age >= 18 and age < 30:
        return 'Young'
    elif age >= 30 and age < 50:
        return 'Middle'
    else:
        return 'old'

* Age  cat
df['age_cat'] = df['age'].apply(age_cat)
df.sample(10)

def Distribution_df(df, column):
    return df.groupby(column)['quantity'].sum()
gender_df=Distribution_df(df,'gender')
gender_df

* Calculate total revenue by gender
gender_df = df.groupby('gender').agg({'quantity': 'sum', 'total_price': 'sum'})

* Create bar chart for gender distribution
plt.bar(gender_df.index, gender_df['quantity'])
plt.title('Gender Distribution by Count')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

* create a pivot table to calculate the average revenue by categories relative to gender
pivot_table = pd.pivot_table(df, index='gender', columns='category', values='quantity')

* plot the bar graph
pivot_table.plot(kind='bar')
plt.title('Average Revenue by Categories Relative to Gender')
plt.xlabel('Gender')
plt.ylabel('Average Revenue')
plt.show()

* Create pie chart for revenue by gender
plt.pie(gender_df['total_price'], labels=gender_df.index, autopct='%1.1f%%')
plt.title('Gender Distribution by Revenue')
plt.show()
print(gender_df.columns)

# Using Apriori Algorithm.
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

* Prepare the data for apriori algorithm
transactions = df.groupby(['invoice_date', 'category'])['quantity'].sum().unstack().reset_index().fillna(0).set_index('invoice_date')

* Convert the values to binary
def encode_units(x):
    if x <= 0:
        return 0
    if x >= 1:
        return 1

transactions = transactions.applymap(encode_units)

* Apply the apriori algorithm
frequent_itemsets = apriori(transactions, min_support=0.05, use_colnames=True)

* Calculate association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules

* Visualize the association rules
plt.figure(figsize=(10, 5))
sns.scatterplot(x=rules['support'], y=rules['confidence'], size=rules['lift'], hue=rules['lift'], palette='viridis')
plt.title('Association Rules Scatterplot')
plt.xlabel('Support')
plt.ylabel('Confidence')
plt.legend(title='Lift', loc='upper right')
plt.show()

* Additional statistical analysis - describe the 'total_price' column
price_stats = df['total_price'].describe()
print(price_stats)

* Data visualization - boxplot for total prices by category
plt.figure(figsize=(10, 5))
sns.boxplot(x='category', y='total_price', data=df)
plt.title('Total Prices by Category')
plt.xlabel('Category')
plt.ylabel('Total Price')
plt.show()

# Top Categories Analysis represented in Bar charts.

* Top categories by quantity
 top_categories = df.groupby('category')['quantity'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
sns.barplot(x=top_categories.index, y=top_categories.values)
plt.title('Top Categories by Quantity')
plt.xlabel('Category')
plt.ylabel('Quantity')
plt.xticks(rotation=45)
plt.show()

# Customer Age Distribution represented in Histogram.

* plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Time series Analysis represented in Line plot graph.

* monthly_revenue = df.groupby(['year', 'month'])['total_price'].sum().reset_index()
monthly_revenue['year_month'] = monthly_revenue['year'] + '-' + monthly_revenue['month']

plt.figure(figsize=(15, 5))
sns.lineplot(x='year_month', y='total_price', data=monthly_revenue)
plt.title('Monthly Revenue Over Time')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

# Other Visualizations are performed.

* age_revenue = df.groupby('age_cat')['total_price'].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=age_revenue.index, y=age_revenue.values)
plt.title('Revenue by Age Category')
plt.xlabel('Age Category')
plt.ylabel('Revenue')
plt.show()

* payment_revenue = df.groupby('payment_method')['total_price'].sum()

plt.figure(figsize=(10, 5))
sns.barplot(x=payment_revenue.index, y=payment_revenue.values)
plt.title('Total Revenue by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Revenue')
plt.show()

* average_price = df.groupby('category')['price'].mean()

plt.figure(figsize=(10, 5))
sns.barplot(x=average_price.index, y=average_price.values)
plt.title('Average Price per Item by Category')
plt.xlabel('Category')
plt.ylabel('Average Price')
plt.show()

* age_payment = df.groupby(['age_cat', 'payment_method'])['quantity'].sum().unstack()

age_payment.plot(kind='bar', stacked=True, figsize=(10, 5))
plt.title('Relationship Between Age Category and Payment Method')
plt.xlabel('Age Category')
plt.ylabel('Quantity')
plt.show()

