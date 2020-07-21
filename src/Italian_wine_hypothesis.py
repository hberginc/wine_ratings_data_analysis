import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from helper_functions import *

#use cleaning functions 
path = '~/galvanize/Capstone_1/data/winemag-data-130k-v2.csv'
cleaner = DataClean(path)
cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
cleaner.drop_null_rows(['country'])
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaner.clean_df(cols)



#view Italian and non_Italian wine Point values
x_non_it_data = cleaner.data[cleaner.data['country'] != 'Italy']['points']
x_italy_data = cleaner.data[cleaner.data['country'] == 'Italy']['points']

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
plot_cdf_left(axs[0], italy_norm, 80, 100)
plot_cdf_right(axs[1], non_it_norm, 80, 100) 
plt.show()
plt.close()

#plot_cdf_overlay
fig, ax = plt.subplots(1)
plot_cdfs_overlay(ax, italy_norm, non_it_norm, 80, 100)
plt.show()
plt.close()

# checkout actual p_value
p_val = stats.ttest_1samp(x_italy_data, non_italy_mean)[1]
print(f'The p value is {p_val}.')



