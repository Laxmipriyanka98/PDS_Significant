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
import os


#Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns


cr_path = Path(os.getcwd())
par_path = cr_path.parent.absolute()
proj_path = str(par_path.parent.absolute())


# Create pie chart for revenue by gender
plt.pie(gender_df['total_price'], labels=gender_df.index, autopct='%1.1f%%')
plt.title('Gender Distribution by Revenue')
print(gender_df.columns)
plt.savefig(proj_path + '\\Outputs\\GenderDistribution.png')

exit = input()
