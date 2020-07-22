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


#view Italian and non_Italian wine Point values
x_non_it_data = cleaned[cleaned['country'] != 'Italy']['points']
x_italy_data = cleaned[cleaned['country'] == 'Italy']['points']


x_range = np.linspace(80,100)
italy_cdf = empirical_distribution_cdf(x_range, x_italy_data)
non_italy_cdf = empirical_distribution_cdf(x_range, x_non_it_data)

#plot overlay cdf
# fig, ax = plt.subplots(1)
# plot_cdfs_overlay(ax, italy_cdf, non_italy_cdf, 80, 100)
# plt.show()



# The Mann-Whitney U test is a non-parametric test that can be used in place of an unpaired t-test. It is used to test the null hypothesis that two samples come from the same population (i.e. have the same median) or, alternatively, whether observations in one sample tend to be larger than observations in the other.

p_val = stats.mannwhitneyu(x_italy_data, x_non_it_data, use_continuity=False, alternative='greater')[1]
print(f'The p value is {p_val}.')
#0.0008348843726267126.


#using spearman coorelation coefficients
it_samp = sample_data(x_italy_data, 20000)
other_samp = sample_data(x_non_it_data, 20000)
itcorr, itp_val = stats.spearmanr(it_samp, other_samp)

print(itcorr, itp_val)

