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

# Create bar chart for gender distribution
plt.bar(gender_df.index, gender_df['quantity'])
plt.title('Gender Distribution by Count')
plt.xlabel('Gender')
plt.ylabel('Count')

plt.savefig(proj_path + '\\Outputs\\GenderDistributionbyCount.png')

pivot_table = pd.pivot_table(df, index='gender', columns='category', values='quantity')

# plot the bar graph
pivot_table.plot(kind='bar')
plt.title('Average Revenue by Categories Relative to Gender')
plt.xlabel('Gender')
plt.ylabel('Average Revenue')
plt.savefig(proj_path + '\\Outputs\\AverageRevenuebyCategoriesRelativetoGender.png')

plt.pie(gender_df['total_price'], labels=gender_df.index, autopct='%1.1f%%')
plt.title('Gender Distribution by Revenue')
plt.savefig(proj_path + '\\Outputs\\GenderDistributionbyRevenue.png')

exit = input()
