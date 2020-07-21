import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from cleaned_data import *
'''
Ho = The length of the description does not correlate to higher ratings.
Ha = The length of the descriotion is statistically correlated to higher ratings

alpha = 0.05
'''



#use cleaning functions 
uncleaned_data = read_data('/home/heather/galvanize/Capstone_1/wine_ratings/data/winemag-data-130k-v2.csv')
added_variety = replace_val(uncleaned_data, 86909, 'variety', 'Cabernet Sauvignon')
dropped_rows = drop_null_rows(added_variety, 'country')
cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
cleaned_df = clean_df(dropped_rows, cols)

