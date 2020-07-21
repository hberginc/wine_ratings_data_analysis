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



def replace_val(unclean_df, index, col, string):
    '''
    parameters:
    unclean_df = dataframe
    index = integer row index where you wish to replace a value
    col = string col where value needs replacement
    string = what to replace in index:col
    
    return dataframe with replaced value
    '''
    unclean_df.loc[index,col] = string
    return unclean_df
              
                

def drop_null_rows(unclean_df, col):
    '''
    parameters:
    unclean_df =  specific data frame
    col = column as a string which you wish to drop null values

    returns:
    dataframe as is with dropped rows on particular colum
    '''
    dropped_rows = unclean_df[unclean_df[col].notna()]

    return dropped_rows.reset_index()




def clean_df(dropped_rows, cols):
    '''
    parameters:
    dropped_rows = dataframe with rows deleted from desired columns
    cols= list of columns desired to include in final

    returns:data frame only with columns selected
    '''
    cleaned_df = dropped_rows[cols].reset_index()
    return cleaned_df

    