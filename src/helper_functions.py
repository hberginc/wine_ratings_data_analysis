import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

class DataClean(object):

    def __init__(self, df_path):
        self.df_path = df_path
        self.data = self.read_data(self.df_path)

    def read_data(self, df_path):
        '''
        Initializes the uncleaned dataFrame
        parameters:
        path_to_data = string with data path included

        returns: df with infered header, index_col=0 for included index in csv file
        '''
        self.data = pd.read_csv(self.df_path, header = 'infer', sep = ',', index_col = 0)
        return self.data


    def replace_val(self, index, col, string):
        '''
        parameters:
        unclean_df = dataframe
        index = integer row index where you wish to replace a value
        col = string col where value needs replacement
        string = what to replace in index:col
        
        return dataframe with replaced value
        '''
        self.data.loc[index,col] = string
        return self.data
              
                

    def drop_null_rows(self, col):
        '''
        parameters:
        unclean_df =  specific data frame
        col = list of columns for which you wish to drop null values

        returns:
        dataframe as is with dropped rows on particular colum
        '''
        self.data.dropna(axis = 0, how = 'any', subset = col, inplace = True)
        return self.data

        


    def clean_df(self, cols):
        '''
        parameters:
        dropped_rows = dataframe with rows deleted from desired columns
        cols= list of columns desired to include in final

        returns:data frame only with columns selected
        '''
        cleaned_df = self.data[cols].reset_index()
        return cleaned_df





def empirical_distribution_cdf(x, data):
    '''
    CDF of provided data
    input an array
    '''
    value_percentage = 1/len(data)
    acum = np.zeros((len(x)))
    for val in data:
        acum += np.array(x>=val)
    return acum * value_percentage



def plot_cdf_overlay_2(ax, dist_dict, low_x, high_x):
    '''
    parameters: 
    dictionary has nested dictionaries within their key, 
    v pairs are data, color, label
    '''
    x = np.linspace(low_x, high_x)
    for k,kv in dist_dict.items():
        ax.plot(x, empirical_distribution_cdf(x,kv['data']), color = kv['color'], label = kv['label'])
    ax.legend()

def sample_data(data, num_samps=1000):
    samps = np.random.choice(data, size = num_samps, replace = True)
    return samps


def bonferroni_correction(times_utilized,original_alpha):
    alph = original_alpha
    for i in range(1, times_utilized+1):
        alph /= i
    return alph
