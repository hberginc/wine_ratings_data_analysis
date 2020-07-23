import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from Data_Clean_class import *
from helper_functions import *

if __name__ == '__main__':

    #use cleaning functions 
    path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
    cleaner = DataClean(path)
    cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
    cleaner.drop_null_rows(['country'])
    cols = ['country', 'points', 'province', 'region_1']
    cleaned = cleaner.clean_df(cols)


    #view California data and 
    Italy_data = cleaned[cleaned['country'] == 'Italy']['points']
    France_data = cleaned[cleaned['country'] == 'France']['points']
    California_data = cleaned[cleaned['province']=='California']['points']
    

    #add values to dictionary
    distrib_dict = {'Italy': {'data':Italy_data, 'color': 'green', 'label': 'Italian Wine'}, 'France': {'data':France_data, 'color': 'blue', 'label': 'French Wine'}, 'California':{'data':California_data, 'color':'red', 'label':'California Wine'}}

    #plot overlay cdf
    fig, ax = plt.subplots(1)
    plot_cdf_overlay_2(ax, distrib_dict, 80, 100)
    plt.savefig('overlapping_cdf_three.png')
    plt.show()



    p_val1 = stats.mannwhitneyu(Italy_data, France_data, use_continuity=False)[1]
    print(f'The p value is {p_val1}.')
    #Using Bonferoni Correction due to utiliing Italy data twice:
    new_alpha1 = bonferroni_correction(2, 0.05)
    print(f'Reject the null because new alpha is {new_alpha1} which is still higher than our p_value')

    print('\n')



    p_val2 = stats.mannwhitneyu(Italy_data, California_data, use_continuity=False)[1]
    print(f'The p value is {p_val2}.')
    #Using Bonferoni Correction due to utiliing Italy data three times:
    new_alpha2 = bonferroni_correction(3, 0.05)
    print(f'Reject the null because new alpha is {new_alpha2} which is still higher than our p_value')

    print('\n')


    p_val3 = stats.mannwhitneyu(California_data, France_data, use_continuity=False)[1]
    print(f'The p value is {p_val3}.')
    #Using Bonferoni Correction due to utiliing French and Cali Data twice times:
    new_alpha3 = bonferroni_correction(2, 0.05)
    print(f'Reject the null because new alpha is {new_alpha3} which is still higher than our p_value\n')
