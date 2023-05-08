import sys
import subprocess
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'pandas'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'numpy'])

#Basic necessary Libraries
import numpy as np
import pandas as pd
from pathlib import Path
import os

cr_path = Path(os.getcwd())
par_path = cr_path.parent.absolute()
proj_path = str(par_path.parent.absolute())

df=pd.read_csv(proj_path + '\\RawData\\customer_shopping_data.csv')

#Drop any unnecessary columns:
df = df.drop(['customer_id','invoice_no','shopping_mall'], axis=1)
df

df['invoice_date'] = pd.to_datetime(df['invoice_date'])
# Year
df['year'] = df['invoice_date'].dt.strftime("%Y")

# Month
df['month'] = df['invoice_date'].dt.strftime("%m")

# Weekday
df['weekday'] = df['invoice_date'].dt.strftime("%w")

# Day
df['day'] = df['invoice_date'].dt.strftime("%d")

# Total Price
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

# Age  cat
df['age_cat'] = df['age'].apply(age_cat)
df.sample(10)

df.to_csv(proj_path + '\\ProcessedData\\PreProcessed.csv');
exit = input()
