# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 15:41:39 2018

@author: husterlgy
"""
path_str = 'D:/Research/Privacy_Project/opsk-project2/data/' #不删除，留着后面用
file_str = path_str + "raw_part" + str(20) + ".csv"
data = pd.read_csv(file_str)
data = data.sort_values(by = 'flightICAO24')
data_sortby_fight = data.sort_values('flightICAO24')

idx_with_rssi = np.where(data['gpsRSSI']!=0)
data_with_rssi = data.iloc[idx_with_rssi[0]]
data_with_rssi = data_with_rssi.sort_values(by = 'flightICAO24')

flightID2 = Counter(data_with_rssi['flightICAO24'])
flightID = Counter(data_with_rssi['flightICAO24'])
for key in flightID2.keys():
    if(flightID2[key]<300):
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


temp_pd = flight_RSSI['020045'][820995539]
temp_pd = temp_pd.sort_values('TimeAtServer')

#dist = gps2dist(temp_pd)#unit:m
#dist = dist/1000

rssi = temp_pd['gpsRSSI']
rssi = np.array(rssi)
plt.plot(rssi)

aa = rssi.copy()
bb = hampel(aa)
cc = exp_average(bb)
#from rssi_preprocessing import rssi_preprocessing
'''Fig 5'''
l1, = plt.plot(rssi)
l2, = plt.plot(cc,linewidth=2.5,color = 'r')
plt.xlim( (100,1100) )
plt.xlabel('Data Index',fontsize=16)
plt.ylabel('RSSI',fontsize=16)
plt.legend(handles = [l1, l2,], labels = ['Raw RSSI', 'Processed RSSI'], loc = 'upper right', fontsize=14)
plt.tick_params(labelsize=14)
plt.savefig('Fig5.png', dpi=400)


   
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

















