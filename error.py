# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:39:22 2023

@author: Principal
"""
import numpy as np
"""
    Calculate the absolute and relative errors for a given data set.

    Parameters:
    - x (list or array): Input data for error calculation.
    - round_decimals (int, optional): Number of decimals for rounding. Default is 2.

    Returns:
    - error_absolute (float): Absolute error.
    - error_relative (float): Relative error.
"""

def calculate_error(data,round_decimals):

        
    data_mean = np.mean(data)
    data_max = max(data)
    data_min = min(data)
        
    if abs(data_max - data_mean) > abs(data_min - data_mean):
        error_absolute = np.around(data_max - data_mean)
    elif abs(data_min - data_mean) > abs(data_max - data_mean):
        error_absolute = np.around(abs(data_min - data_mean), decimals=round_decimals)
    else:
        error_absolute = np.around(abs(data_max - data_mean), decimals=round_decimals)

    error_relative = (error_absolute / data_mean) * 100 if data_mean != 0 else np.nan
    error_relative = np.round(error_relative, decimals=round_decimals)

    return error_absolute, error_relative