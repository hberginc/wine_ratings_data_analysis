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
        col = column as a string which you wish to drop null values

        returns:
        dataframe as is with dropped rows on particular colum
        '''
        return self.data[self.data[col].notna()].reset_index()

        


    def clean_df(self, cols):
        '''
        parameters:
        dropped_rows = dataframe with rows deleted from desired columns
        cols= list of columns desired to include in final

        returns:data frame only with columns selected
        '''
        cleaned_df = self.data[cols].reset_index()
        return cleaned_df





def plot_cdfs_overlay(ax, dist_data_a, dist_data_b, low_x, high_x, label_a = 'Italian_wines', label_b = 'Non_Italian_Wines', title= 'CDF Compare', x_label = 'Points Range', y_label = 'cdf'):
    x = np.linspace(low_x, high_x)
    ax.plot(x, dist_data_a.cdf(x), color = 'red', label = label_a)
    ax.plot(x, dist_data_b.cdf(x), color = 'blue', label = label_b )
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.legend()
    plt.show()



def plot_cdf_left(ax, dist_data,low_x, high_x, title = 'Italian_wine'):
    x = np.linspace(low_x, high_x)
    ax.plot(x, dist_data.cdf(x), color = 'red')
    ax.set_title(title)

def plot_cdf_right(ax, dist_data,low_x, high_x, title = 'non_Italian_wine'):
    x = np.linspace(low_x, high_x)
    ax.plot(x, dist_data.cdf(x), color = 'blue')
    ax.set_title(title)





