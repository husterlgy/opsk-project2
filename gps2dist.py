# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 15:19:06 2018

@author: lgy
"""
import numpy as np;


def gps2dist(flight_pd):
    '''把sensor array中的数据和flight array中的gps位置信息和高度信息结合起来，计算sensor和flight之间的距离,单位为米'''
    #R_earth = 6371.393;#千米km
    R_earth = 6371.393*1000;#米m
    feet2m = 0.3048;
    '''
    Haversine公式来计算，详细参看wiki
    C = sin(LatA)*sin(LatB) + cos(LatA)*cos(LatB)*cos(MLonA-MLonB)
    Distance = R*Arccos(C)*Pi/180
    '''
    sensorLatitude = flight_pd['sensorLatitude']
    sensorLongitude = flight_pd['sensorLongitude']
    sensorAltitude = flight_pd['sensorAltitude']
    
    flightLatitude = flight_pd['flightLatitude']
    flightLongitude = flight_pd['flightLongitude']
    flightAltitude = flight_pd['flightAltitude']
    
    sensorLatitude = np.array(sensorLatitude)
    sensorLongitude = np.array(sensorLongitude)
    sensorAltitude = np.array(sensorAltitude)
    
    flightLatitude = np.array(flightLatitude)
    flightLongitude = np.array(flightLongitude)
    flightAltitude = np.array(flightAltitude)
    
    
    
    
    
    sensorLatitude_deg = degree2rad(sensorLatitude);
    sensorLongitude_deg = degree2rad(sensorLongitude);
    flightLatitude_deg = degree2rad(flightLatitude);
    flightLongitude_deg = degree2rad(flightLongitude);
    
    
    para1 = (1-np.cos(sensorLatitude_deg-flightLatitude_deg))/2;
    para2 = np.cos(sensorLatitude_deg)*np.cos(flightLatitude_deg);
    para3 = (1-np.cos(sensorLongitude_deg-flightLongitude_deg))/2;
    totol_para = 1-2*(para1+para2*para3);  
    sphere_dist = R_earth*np.arccos(totol_para);
    horizon_dist = 0.3048*(flightAltitude-sensorAltitude);
    los_dist =  np.sqrt(sphere_dist*sphere_dist+horizon_dist*horizon_dist);
    return los_dist

    
#    para = np.sin(sensorLatitude_deg)*np.sin(flightLatitude_deg)+np.cos(sensorLatitude_deg)*np.cos(flightLatitude_deg)*np.cos(sensorLongitude_deg-flightLongitude_deg);
#    return R_earth*np.arccos(para)
#    
    
    
    
def degree2rad(degree_array):
    return degree_array*np.pi/180;