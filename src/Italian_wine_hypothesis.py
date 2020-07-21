import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from cleaned_data import *
'''
Ho = Italian wines have the same average rating as other countries
Ha = Italian wines have a statistically significant higher rating. 

alpha = 0.05
p_value = 1.251555077297758e-09
Cannot reject null hypothesis
'''



#use cleaning functions 
uncleaned_data = read_data('/home/heather/galvanize/Capstone_1/wine_ratings/data/winemag-data-130k-v2.csv')
added_variety = replace_val(uncleaned_data, 86909, 'variety', 'Cabernet Sauvignon')
dropped_rows = drop_null_rows(added_variety, 'country')
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaned_df = clean_df(dropped_rows, cols)



cleaned_df['points'].describe()
'''
count    129908.000000
mean         88.447047
std           3.040066
min          80.000000
25%          86.000000
50%          88.000000
75%          91.000000
max         100.000000
'''

'''
since mean is 88.447 and std is 3.04, 
use histogram to view the 
normal distribution of  the sample mean
'''
x_data = cleaned_df['points']
normal_test = stats.norm(88.447, 3.04)

fig, ax = plt.subplots(1)
x = np.linspace(77, 100)
ax.hist(x_data, bins = 20, alpha = 0.7, density = True, color = 'blue')
ax.plot(x, normal_test.pdf(x), color = 'red')
plt.show()


#find info on just Italian wines
italy_data = cleaned_df[cleaned_df['country'] == 'Italy']
#compare italy_data to norm_dist
x_data_It = italy_data['points']

fig, ax = plt.subplots(1)
x = np.linspace(77, 100)
ax.hist(x_data_It, bins = 15, alpha = 0.7, density = True, color = 'purple')
ax.plot(x, normal_test.pdf(x), color = 'red')
plt.show()


#checkout actual p_value
p_val = stats.ttest_1samp(x_data_It,np.mean(cleaned_df['points']))[1]
print(f'The p value is {p_val}.')
#1.251555077297758e-09
