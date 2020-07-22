import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns

from helper_functions import *

path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
df = pd.read_csv(path, header = 'infer', sep = ',', index_col = 0)

