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
#plt.show()


it_samps = sample_data(Italy_data, 20000)
fr_samps = sample_data(France_data, 20000)
ca_samps = sample_data(California_data, 20000)


iccorr, icp_val = stats.spearmanr(it_samps,ca_samps)
print(f'Italian ratings and California ratings have a correlation of {iccorr} and a p_value of {icp_val}')

ifcorr, ifp_val = stats.spearmanr(it_samps,fr_samps)
print(f'Italian ratings and French ratings have a correlation of {ifcorr} and a p_value of {ifp_val}')

cfcorr, cfp_val = stats.spearmanr(ca_samps,fr_samps)
print(f'French ratings and California ratings have a correlation of {cfcorr} and a p_value of {cfp_val}')



#Calfornia 2,629
#France 22,093
#Italy 19,540
