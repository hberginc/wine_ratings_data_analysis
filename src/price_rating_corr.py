import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from helper_functions import *

if __name__ == '__main__':

    path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
    cleaner = DataClean(path)
    cleaner.drop_null_rows(['price'])
    cols = ['country', 'points', 'price']
    df = cleaner.clean_df(cols)

    expensive = df[df['price']>150]
    cheap = df[df['price']<150]


    c_corr, c_p = stats.spearmanr(cheap['price'], cheap['points'])
    e_corr, e_p = stats.spearmanr(expensive['price'], expensive['points'])


    print(f"The expensive wines have a correlation coefficient of {np.round(e_corr, 2)} compared to the cheap wines with a correlation coefficient of {np.round(c_corr, 2)}.")

    print(f'The correlation of price to rating for the cheap wines is {np.round(c_corr/e_corr, 2)} times stronger.')

    print(f'p_value for cheaper = {c_p} and p_value for expensive = {e_p}')