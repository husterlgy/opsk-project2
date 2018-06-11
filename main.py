# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 14:20:00 2018

@author: husterlgy
"""
import numpy as np 
import pandas as pd
import scipy 
from collections import Counter
import matplotlib.pyplot as plt
from gps2dist import gps2dist

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

flight_RSSI = {}
for key in flightID.keys():
    temp_pd = data_with_rssi.iloc[np.where(data_with_rssi['flightICAO24'] == key)]
    sensor_ID = Counter(temp_pd['senserNumber'])
    temp_dict = {}
    for sensor in sensor_ID.keys():
        temp_dict[sensor] = temp_pd.iloc[np.where(temp_pd['senserNumber'] == sensor)]
    flight_RSSI[key] = temp_dict
del key,sensor,temp_pd,temp_dict,sensor_ID,idx_with_rssi#delete temp parameters

'''flight_RSSI->{flightICAO->{sensorID->flight_data}}'''


'''preliminary colleration analysis of RSSI and positon'''


temp_pd = flight_RSSI['4690f0'][13020203]
temp_pd = temp_pd.sort_values('TimeAtServer')

dist = gps2dist(temp_pd)#unit:m
dist = dist/1000

rssi = temp_pd['gpsRSSI']
rssi = np.array(rssi)

#from rssi_preprocessing import rssi_preprocessing


width = 40
aa = temp_pd['gpsRSSI'].rolling(width).mean()
aa = np.array(aa)
for ii in range(width):
#    aa[ii] = temp_pd['gpsRSSI'].iloc[ii]
    aa[ii] = aa[width:-1].mean()


dist = (dist - dist.min())/(dist.max() - dist.min())
aa = (aa - aa.min())/(aa.max() - aa.min())
dist = dist*dist
plt.plot(dist)
plt.plot(aa)





































