import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from helper_functions import *

if __name__ == '__main__':

    # use cleaning functions 
    path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
    cleaner = DataClean(path)
    cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
    cleaner.drop_null_rows(['country'])
    cols = ['country', 'points', 'price', 'province']
    df = cleaner.clean_df(cols)


    #set up variables
    Italy_data = region_based_df(df, 'country', 'Italy')['points']
    non_it_data = region_based_df(df, 'country', 'Italy', equal_to=False)['points']
    France_data = region_based_df(df, 'country', 'France')['points']
    California_data = region_based_df(df, 'province', 'California')['points']

    #calculate_p_val
    p_val = stats.mannwhitneyu(Italy_data, non_it_data, use_continuity=False, alternative='greater')
    print(f'{p_val} is lower than 0.05 so Italy is better than Other Countries.')



    p_val1 = stats.mannwhitneyu(Italy_data, France_data, alternative = 'greater')[1]
    #Using Bonfreroni Correction due to utiliing Italy data twice:
    new_alpha1 = bonferroni_correction(2, 0.05)
    print(f'ITALY greater than FRANCE? new_alpha: {new_alpha1} p_val = {p_val1}')


   
    p_val2 = stats.mannwhitneyu(Italy_data, California_data, alternative = 'greater')[1]
    #Using Bonferroni Correction due to utiliing Italy data three times:
    new_alpha2 = bonferroni_correction(3, 0.05)
    print(f'ITALY greater_than CALI? new_alpha: {new_alpha2} p_val = {p_val2}')
    


    p_val3 = stats.mannwhitneyu(France_data, California_data, alternative = 'greater')[1]
    #Using Bonferroni Correction due to utiliing French and Cali Data twice times:
    new_alpha3 = bonferroni_correction(2, 0.05)
    print(f'France greater_than CALI? new_alpha: {new_alpha3} p_val = {p_val3}')





