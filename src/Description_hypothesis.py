import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from Data_Clean_class import *
from helper_functions import *

if __name__ == '__main__':
    
    #use cleaning Class 
    path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
    cleaner = DataClean(path)
    cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
    cleaner.drop_null_rows(['country'])
    cols = ['country', 'description', 'points']
    df = cleaner.clean_df(cols)


    #make another column that counts the length of the description
    df['description_length'] = df['description'].str.len()


    #median is exactly 88
    med = np.median(df['points'])
    below_88_df = df[['points','description_length']][df['points'] < med]
    above_88_df = df[['points','description_length']][df['points'] > med]


    #add extra column for hue
    df['above_median_rating']=df['points']>med
    #look at all ratings at median
    All_but_88 = df[df['points']!=med]

    #VIOLIN PLOT
    fig, ax = plt.subplots(1, figsize=(12, 8))
    sns.violinplot('points', 'description_length', hue = 'above_median_rating', data = All_but_88, palette="Set2", ax = ax)
    ax.set_title('Above and Below Median Vairance')
    plt.savefig('desc_per_rate_violin.png')
    #plt.show()

    
    p_val = stats.ttest_ind(below_88_df['description_length'], above_88_df['description_length'])[1]
    print(f'The p value is {p_val}.')

    correlation = stats.spearmanr(df['points'], df['description_length'])
    print(correlation)
    #cor coef = 0.5, p_val = 0


    # below_des_med = df[['points','description_length']][df['description_length'] < 237]
    # above_des_med = df[['points','description_length']][df['description_length'] > 237]

    # fig, ax = plt.subplots(1)
    # ax.scatter(below_des_med['description_length'], below_des_med['points'], color = 'blue', alpha = 0.5)
    # ax.scatter(above_des_med['description_length'], above_des_med['points'], color = 'green', alpha = 0.5)
    # ax.set_ylabel('Rating')
    # ax.set_xlabel('Description Length')
    # ax.set_title('Rating per Length of Description')
    # plt.savefig('points_scatter_per_desc.png')
    # plt.show()
    # plt.close()

    # p_val_desc = stats.ttest_ind(below_des_med['points'], above_des_med['points'])[1]

    # fig, ax = plt.subplots(1)
    # sns.scatterplot(below_des_med['description_length'], below_des_med['points'], x_jitter= True, ax = ax)
    # sns.scatterplot(above_des_med['description_length'], above_des_med['points'], x_jitter= True, ax = ax)
    # plt.show()

