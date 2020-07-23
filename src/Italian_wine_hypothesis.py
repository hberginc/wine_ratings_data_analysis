import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from Data_Clean_class import *
from helper_functions import *

#use cleaning functions 
path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
cleaner = DataClean(path)
cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
cleaner.drop_null_rows(['country'])
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaned = cleaner.clean_df(cols)


#view Italian and non_Italian wine Point values
x_non_it_data = cleaned[cleaned['country'] != 'Italy']['points']
x_italy_data = cleaned[cleaned['country'] == 'Italy']['points']


#dict_template_for_plot()
dict_for_Italian_heavy = {'Italy':{'data':x_italy_data, 'color': 'g', "label": 'Italian_Wine'}, 'Other':{'data':x_non_it_data, 'color':'b', 'label': 'Non_Italian_Wine'}}

#Include about other regions comparison
France_data = cleaned[cleaned['country'] == 'France']['points']
California_data = cleaned[cleaned['province']=='California']['points']
#add values to dictionary
distrib_dict = {'Italy': {'data':x_italy_data, 'color': 'green', 'label': 'Italian Wine'}, 'France': {'data':France_data, 'color': 'blue', 'label': 'French Wine'}, 'California':{'data':California_data, 'color':'red', 'label':'California Wine'}}

fig, ax = plt.subplots(1,2, figsize=(9, 5))
plot_cdf_overlay_2(ax[0], dict_for_Italian_heavy, 80, 100)
plot_cdf_overlay_2(ax[1], distrib_dict, 80, 100)
ax[0].set_xlabel('Rating')
ax[1].set_xlabel('Rating')
ax[0].set_ylabel('CDF')
ax[1].set_ylabel('CDF')
plt.savefig('cdf_vis.png')
plt.show()



# The Mann-Whitney U test is a non-parametric test that can be used in place of an unpaired t-test. It is used to test the null hypothesis that two samples come from the same population (i.e. have the same median) or, alternatively, whether observations in one sample tend to be larger than observations in the other.

p_val = stats.mannwhitneyu(x_italy_data, x_non_it_data, use_continuity=False, alternative='greater')[1]
print(f'The p value is {p_val}.')
#0.0008348843726267126.




