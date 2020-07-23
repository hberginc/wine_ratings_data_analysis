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
    cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
    cleaned = cleaner.clean_df(cols)


    #view Italian and non_Italian wine Point values
    x_non_it_data = cleaned[cleaned['country'] != 'Italy']['points']
    x_italy_data = cleaned[cleaned['country'] == 'Italy']['points']


    #dict_template_for_plot()
    dict_for_Italian_heavy = {'Italy':{'data':x_italy_data, 'color': 'g', "label": 'Italian_Wine'}, 'Other':{'data':x_non_it_data, 'color':'purple', 'label': 'Non_Italian_Wine'}}


    #plot CDF
    fig, ax = plt.subplots(1)
    plot_cdf_overlay_2(ax, dict_for_Italian_heavy, 80, 100)
    ax.set_xlabel('Rating')
    ax.set_ylabel('CDF')
    plt.savefig('cdf_vis.png')
    plt.show()


    #calculate_p_val
    p_val = stats.mannwhitneyu(x_italy_data, x_non_it_data, use_continuity=False, alternative='greater')[1]
    print(f'The p value is {p_val}.')




