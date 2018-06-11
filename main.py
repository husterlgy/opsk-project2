# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:20:00 2018

@author: husterlgy
"""
import numpy as np 
import pandas as pd
import scipy 
from collections import Counter


data = pd.read_csv('data.csv')
data = data.sort_values(by = 'flightICAO24')
data_sortby_fight = data.sort_values('flightICAO24')

idx_with_rssi = np.where(data['gpsRSSI']!=0)
data_with_rssi = data.iloc[idx_with_rssi[0]]
data_with_rssi = data_with_rssi.sort_values(by = 'flightICAO24')

flightID = Counter(data_with_rssi['flightICAO24'])
for key in flightID.keys():
    if(flightID[key]<300):
         del flightID[key]




























