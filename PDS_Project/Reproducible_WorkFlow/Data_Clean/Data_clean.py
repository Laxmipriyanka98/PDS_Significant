#Basic necessary Libraries
import numpy as np
import pandas as pd

#Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a dataframe
df = pd.read_csv('customer_shopping_data.csv')')

# Drop any unnecessary columns:
df = df.drop(['customer_id','invoice_no','shopping_mall'], axis=1)

#The values the data provided is already clean
