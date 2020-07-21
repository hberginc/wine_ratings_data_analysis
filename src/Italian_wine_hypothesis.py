import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from helper_functions import *
'''
Ho = Italian wines have the same average rating as other countries
Ha = Italian wines have a statistically significant higher rating. 

alpha = 0.05
p_value = 8.839008131948766e-13

I can reject my null hypothesis, Italian wines have a statistically significant higher rating than non Italian wines
'''

#use cleaning functions 
uncleaned_data = read_data('/home/heather/galvanize/Capstone_1/wine_ratings/data/winemag-data-130k-v2.csv')
added_variety = replace_val(uncleaned_data, 86909, 'variety', 'Cabernet Sauvignon')
dropped_rows = drop_null_rows(added_variety, 'country')
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaned_df = clean_df(dropped_rows, cols)


#view Italian and non_Italian wine Point values
x_non_it_data = cleaned_df[cleaned_df['country'] != 'Italy']['points']
x_italy_data = cleaned_df[cleaned_df['country'] == 'Italy']['points']

#x_data
non_italy_mean = np.mean(x_non_it_data)
non_italy_std = np.std(x_non_it_data, ddof = 1)
#x_italy_data
italy_mean = np.mean(x_italy_data)
italy_std = np.std(x_italy_data, ddof=1)


#norm_dist_of_means
non_it_norm= stats.norm(non_italy_mean, non_italy_std)
italy_norm = stats.norm(italy_mean, italy_std)


#plot_cdf_side_by_side
fig, axs = plt.subplots(1,2)
plt.subplots_adjust(wspace = 0.6)
x = np.linspace(80, 100)
axs[0].plot(x, non_it_norm.cdf(x), color = 'red')
axs[0].set_title("Non_Italian")
axs[0].set_xlabel('Ratings from 80 to 100')
axs[0].set_ylabel('CDF')
axs[1].plot(x, italy_norm.cdf(x), color = 'blue')
axs[1].set_title("Italian")
axs[1].set_xlabel('Ratings from 80 to 100')
axs[1].set_ylabel('CDF')
plt.show()


#plot_cdf_ontop_of_eachother
fig, ax = plt.subplots(1)
x = np.linspace(80, 100)
ax.plot(x, non_it_norm.cdf(x), color = 'red', label = 'Non_Italian')
ax.plot(x, italy_norm.cdf(x), color = 'blue', label = 'Italian' )
plt.title("CDF's of Italian and Non_Italian Wines")
plt.xlabel('Ratings from 80 to 100')
plt.ylabel('CDF')
plt.legend()
#plt.show()



# checkout actual p_value
p_val = stats.ttest_1samp(x_italy_data, non_italy_mean)[1]
# print(f'The p value is {p_val}.')



