import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF
from helper_functions import *

#use cleaning functions 
path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
cleaner = DataClean(path)
cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
cleaner.drop_null_rows(['country'])
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaned = cleaner.clean_df(cols)


#view California data and 
Italy_data = cleaned[cleaned['country'] == 'Italy']['points']
France_data = cleaned[cleaned['country'] == 'France']['points']
California_data = cleaned[cleaned['region_1']=='California']['points']

#add values to dictionary
distrib_dict = {'California':{'data':California_data, 'color':'red', 'label':'California Wine'}, 'Italy': {'data':Italy_data, 'color': 'green', 'label': 'Italian Wine'}, 'France': {'data':France_data, 'color': 'blue', 'label': 'French Wine'}}

#plot overlay cdf
fig, ax = plt.subplots(1)
plot_cdf_overlay_2(ax, distrib_dict, 80, 100)
plt.savefig('regions_cdf.png')
plt.show()







#Calfornia 2,629
#France 22,093
#Italy 19,540
#Spearman correlation tests(ordered) 
#correlation coefficient
#p_value