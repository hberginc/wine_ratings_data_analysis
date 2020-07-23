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



if __name__ == "__main__":
    path = '~/galvanize/Capstone_1/git_info_wine_ratings/data/winemag-data-130k-v2.csv'
    cleaner = DataClean(path)
    print('"cleaner" variable set to df')
    cleaner.replace_val(86909, 'variety', 'Cabernet Sauvignon')
    print('Missing value replaced with Cabernet')
    cleaner.drop_null_rows(['country'])
    print('Dropped all null country rows')
    cols = ['country', 'description', 'points', 'price', 'province', 'region_1', 'title', 'variety', 'winery']
    cleaned = cleaner.clean_df(cols)
    print('"cleaned" df ready to go!')
    print(cleaned.head(2))