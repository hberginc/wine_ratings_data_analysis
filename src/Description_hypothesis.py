import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from helper_functions import *
'''
Ho = The length of the description does not correlate to higher ratings.
Ha = The length of the descriotion is statistically correlated to higher ratings

alpha = 0.05
'''

#use cleaning Class 
path = '~/galvanize/Capstone_1/data/winemag-data-130k-v2.csv'
cleaner = DataClean(path)
cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
cleaner.drop_null_rows(['country'])
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaner.clean_df(cols)
df = cleaner.data


#make another column that counts the length of the description
df['description_length'] = df['description'].str.len()
new_df = df[['points', 'description_length']]

fig, ax = plt.subplots(1)
ax.scatter(new_df['points'], new_df['description_length'])
ax.set_xlabel('Rating')
ax.set_ylabel('Description_Length')
plt.show()
plt.savefig('scatter_desc_length.png')