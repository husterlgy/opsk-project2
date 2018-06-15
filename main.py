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
from pandas.io import sql as pd_sql
import sqlite3 

'''Data preprocessing:from csv to sqlite3'''
#path_str = 'D:/Research/Privacy_Project/opsk-project2/data/' #不删除，留着后面用
#file_str = path_str + "raw_part" + str(20) + ".csv"
#data = pd.read_csv(file_str)
#for ii in range(19):
#    file_str = path_str + "raw_part" + str(21+ii) + ".csv"
#    data_temp = pd.read_csv(file_str)
#    data = pd.concat([data,data_temp])
#    print "loading csv: raw_part" + str(21+ii)
#del data_temp,file_str
#
#sql_cnx = sqlite3.connect(path_str + 'data.db')
#print 'Opened database successfully'  
#data.to_sql('flight_info', sql_cnx)
#sql_cnx.close()



'''Data analysis'''
path_str = 'D:/Research/Privacy_Project/opsk-project2/data/'
sql_cnx = sqlite3.connect(path_str + 'data.db')
sql_cursor = sql_cnx.cursor()
sql_cursor.rowcount


sql_cursor.execute("select gpsRSSI from flight_info")
gpsRSSI = sql_cursor.fetchall()
gpsRSSI = np.array(gpsRSSI)


sql_cursor.close()
sql_cnx.close()




























