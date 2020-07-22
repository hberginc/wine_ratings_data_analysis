import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from helper_functions import *
'''
Ho = Wines that are less than the median rating have a the same length descriptions as wines with points above the median.
Ha = Wines that are higher than the median rating have longer descriptions than the wines with lower ratings.
alpha = 0.05
p_value of 0 
Reject the Null Hypothesis
'''

'''
Ho = Wines that have fewer than the median number of words have fewer points.
Ha = Wines that have greater than the median number of words have higher ratings.
alpha = 0.05
alpha = 0
Reject the Null Hypothesis
'''
#df points less than med
#df opposite
#t-test on both to determine p_value of number of words in description


#do wines that have few number of words have fewer points..
#repeate above t-test


#use cleaning Class 
path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
cleaner = DataClean(path)
cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
cleaner.drop_null_rows(['country'])
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
df = cleaner.clean_df(cols)


#make another column that counts the length of the description
df['description_length'] = df['description'].str.len()

#median is exactly 88

below_88_df = df[['points','description_length']][df['points'] < 88]
above_88_df = df[['points','description_length']][df['points'] > 88]

# fig, ax = plt.subplots(1)
# ax.scatter(below_88_df['points'], below_88_df['description_length'], marker = '*', color = 'green')
# ax.scatter(above_88_df['points'], above_88_df['description_length'], marker = '*', color = 'purple')
# ax.set_xlabel('Rating')
# ax.set_ylabel('Description Length')
# ax.set_title('Words in Description per Rating')

df['above_median_rating']=df['points']>88 

violin_plot_df = df[df['points']!=88 ]

# #VIOLIN PLOT
# fig, ax = plt.subplots(1, figsize=(12, 8))
# sns.violinplot('points', 'description_length', hue = 'above_median_rating', data = violin_plot_df, palette="Set2", ax = ax)
# plt.savefig('desc_per_rate_violin.png')
# plt.show()




p_val = stats.ttest_ind(below_88_df['description_length'], above_88_df['description_length'])[1]
# print(f'The p value is {p_val}.')




below_des_med = df[['points','description_length']][df['description_length'] < 237]
above_des_med = df[['points','description_length']][df['description_length'] > 237]

# fig, ax = plt.subplots(1)
# ax.scatter(below_des_med['description_length'], below_des_med['points'], color = 'blue', alpha = 0.5)
# ax.scatter(above_des_med['description_length'], above_des_med['points'], color = 'green', alpha = 0.5)
# ax.set_ylabel('Rating')
# ax.set_xlabel('Description Length')
# ax.set_title('Rating per Length of Description')
# plt.savefig('points_scatter_per_desc.png')
# plt.show()
# plt.close()

p_val_desc = stats.ttest_ind(below_des_med['points'], above_des_med['points'])[1]

fig, ax = plt.subplots(1)
sns.scatterplot(below_des_med['description_length'], below_des_med['points'], x_jitter= True, ax = ax)
sns.scatterplot(above_des_med['description_length'], above_des_med['points'], x_jitter= True, ax = ax)
plt.show()

