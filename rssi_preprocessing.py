# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:47:24 2018

@author: husterlgy
"""
import numpy as np
import scipy 


def rssi_prepocessing(raw_rssi,width):
    '''moving average'''
    for ii in range(len(raw_rssi)):
        



        
    
    return rssi
    


'''指数加权平均'''
def exp_average(input_serial):
    beta_ = 0.9
    
    output_serial = np.zeros(input_serial.shape[0])
    v_prev = 0
    
    for ii in range(len(output_serial)):
        
        v_current = iterate_of_exp_average(v_prev, input_serial[ii], beta_)
        output_serial[ii] = v_current
        v_prev = v_current
            
    return output_serial
def iterate_of_exp_average(v_prev, theta_current, beta_):
    v_current = beta_ * v_prev + (1 - beta_) * theta_current
    
    return v_current




'''Hampel滤波器'''
def hampel(org_vals):
    vals = pd.DataFrame(org_vals) # create a new data frame based on your original df.
    std = vals[0].std() # get the standard dev from the total of columns you want to de-outlier
    bad_idx = vals.index[vals[0].ge(std * 3)] # place your df indexes in an array which are 3 stds away from your mean. 
    bad_idx_min = vals.index[vals[0].le(-std * 3)]
    for i in bad_idx: # Loop over the upper range of outliers and replace the outliers with your mean
        idx = ([i-3, i-2, i-1, i+1, i+2, i+3]) # the array of indexes around your outlier
        new_mean = vals[0].loc[idx].mean() # the mean of the values around your outlier excluding the outlier itself
        vals.loc[i, 0] = new_mean # replace outlier with mean
    for i in bad_idx_min: # same as above but with the lower range
        idx = ([i-3, i-2, i-1, i+1, i+2, i+3])
        new_mean = vals[0].loc[idx].mean()
        vals.loc[i, 0] = new_mean
        
    vals = np.array(vals)
    vals = vals.reshape(len(vals))
     
    return(vals) # return the new values.