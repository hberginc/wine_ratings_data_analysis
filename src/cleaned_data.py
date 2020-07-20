import numpy as np 
import pandas as pd 

def read_data(path_to_data):
    '''Initializes the uncleaned dataFrame
    parameters:
    path_to_data = string with data path included

    returns: df with infered header, index_col=0 for included index in csv file
    '''
    unclean_df = pd.read_csv(path_to_data, header = 'infer', sep = ',', index_col = 0)
    return unclean_df

def drop_null_rows(unclean_df, col):
    '''
    parameters:
    unclean_df =  specific data frame
    col = columns which you wish to drop null values

    returns:
    dataframe as is with dropped rows on particular colum
    '''
    dropped_rows = unclean_df[unclean_df['county'].notna()]

    return dropped_rows

def clean_df(dropped_rows, cols):
    '''
    parameters:
    dropped_rows = dataframe with rows deleted from desired columns
    cols= list of columns desired to include in final

    returns:data frame only with columns selected
    '''
    cleaned_df = dropped_rows[cols]
    return cleaned_df

    