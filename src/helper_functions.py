import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

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

def dict_template_for_plot():
    '''
    return:
    Example of how to 
    use dictinary parameter in 
    plot_cdf_overlay_2
    '''
    print('distrib_dict = {INFO_name: {"data":val, "color":val, "label":val}, INFO2_name: {"data":val, "color":val, "label":val}}')
   


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
    samps = np.random.choice(data, size = num_samps, replace = False)
    return samps


def bonferroni_correction(times_utilized,original_alpha):
    alph = original_alpha
    for i in range(1, times_utilized+1):
        alph /= i
    return alph
