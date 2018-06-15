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


path_str = 'D:/Research/Privacy_Project/opsk-project2/data/' #不删除，留着后面用
file_str = path_str + "raw_part" + str(20) + ".csv"
data = pd.read_csv(file_str)
for ii in range(19):
    file_str = path_str + "raw_part" + str(21+ii) + ".csv"
    data_temp = pd.read_csv(file_str)
    data = pd.concat([data,data_temp])
    print "loading csv: raw_part" + str(21+ii)
del data_temp,file_str




























































