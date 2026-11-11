#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Create datasets for analysis

Created on Tue Jan 17 09:32:46 2023

@author: ivrens
"""

import numpy as np
import matplotlib.pyplot as plt

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Create datasets for analysis

Created on Tue Jan 17 09:32:46 2023

@author: ivrens
"""

import numpy as np


#%% plasma chamber exposure - magnet sample


def gatesweep_first_exposure():
    filenames = ['./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,15.002.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,15.003.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.001.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.003.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.005.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.006.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.008.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.010.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.012.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.014.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.016.dat',
                 ]
    labels = ['annealed',
              '5 min plasma',
              #'10 min air exposure',
              #'10 min air exposure',
              '10 min plasma',
              #'10 min air exposure',
              '15 min plasma',
              #'10 min air exposure',
              '25 min plasma',
              #'10 min air exposure',
              '77K'
              ]
    cumulative_plasma = [0, 5, 10, 15, 25, 27]
    return filenames, labels, cumulative_plasma



def gatesweep_second_exposure():
    filenames = ['./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.001.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.002.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.003.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.004.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.005.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.006.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.007.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.008.dat',
                 ]
    labels = ['before exposure',
              #'before exposure',
              #'30 min plasma in total',
              #'30 min plasma in total',
              '30 min plasma in total',
              #'30 min plasma in total',
              '10 min air exposure',
              #'10 min air exposure',
              ]
    filenrs = [1,5,7]
    return filenames, labels, filenrs



def gatesweep_full_exposure():
    filenames = ['./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,15.002.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.003.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.006.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.010.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.014.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.016.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.001.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.005.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.007.dat',
                 ]
    labels = ['pristine, annealed',
              #'5 min plasma',
              #'10 min plasma',
              '15 min plasma',
              '25 min plasma',
              #'77K',
              #'25 min + air exposure',
              '30 min plasma',
              #'10 min air exposure',
              ]
    cumulative_plasma = [0, 15, 25, 30]
    return filenames, labels, cumulative_plasma



def gatesweep_full_exposure_extended():
    filenames = ['./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,15.002.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.003.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.006.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.010.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.014.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-5,12.016.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.001.dat',
                 './2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.005.dat',
                 #'./2406-preparations/g3/g3-SD-11,6-V1-9,10-V2-9,8.007.dat',
                 ]
    labels = ['pristine, annealed',
              '5 min plasma',
              '10 min plasma',
              '15 min plasma',
              '25 min plasma',
              #'77K',
              #'25 min + air exposure',
              '30 min plasma',
              #'10 min air exposure',
              ]
    cumulative_plasma = [0, 5, 10, 15, 25, 30]
    return filenames, labels, cumulative_plasma



#%% state 0 no field Cell4

def gatesweep_0T_state0():
    filenames = [#'./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.004.dat',
                 #'./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.005.dat',
                 #'./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.003.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.002.dat',
                 #'./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.001.dat',
                 #'./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-8,10-V4-5,24.003.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-8,10-V4-5,24.002.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-8,10-V4-5,24.001.dat',
                 
                 ]
    labels = [#'4.2K',
              #'4.2K',
              #'4.2K',
              '99K',
              #'105K',
              #'238K',
              '270K',
              '280K',
              ]
    temperatures = [4.2,99,105,238,270,280]
    temperatures = [99,270,280]
    return filenames, labels, temperatures



#%% state 1 field dependence Cell4

def gatesweep_4K_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.031.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.024.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.022.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.013.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.018.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.020.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.016.dat',
                 ]
    labels = ['0T',
              '5T',
              '10T',
              '15T',
              '20T',
              '25T',
              '30T']
    fields = [0,5,10,15,20,25,30]
    return filenames, labels, fields



def gatesweep_4K_symmetry_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.029.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.020.dat',
                 ]
    labels = ['-25T, Rx',
              '-25T, Ry',
              '25T, Rx',
              '25T, Ry']
    fields = [-25, 25]
    return filenames, labels, fields



def gatesweep_4K_state1_reduced():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.031.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.018.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.020.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.016.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    newLabel = []
    for field in fields :
        newLabel.append(str(field) + "T")
    return filenames, newLabel, fields



def gatesweep_10K_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.034.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.027.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.029.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.025.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



def gatesweep_25K_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.036.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.032.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.030.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.028.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.026.dat',
                 ]
    labels = ['0T',
              '15T',
              '20T',
              '25T',
              '30T']
    fields = [0,15,20,25,30]
    return filenames, labels, fields



def gatesweep_50K_state1():
    filenames = ['./2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.034.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.022.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.024.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.020.dat',
                 ]
    labels = ['0T',
              '15T',
              '20T',
              '25T',
              '30T']
    fields = [0,15,20,25,30]
    return filenames, labels, fields



def gatesweep_75K_state1():
    filenames = ['./2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.036.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.003.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



def gatesweep_143K_state1():
    filenames = ['./2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.008.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.010.dat',
                 ]
    labels = ['0T',
              '15T',
              '20T',
              '25T',
              '30T']
    fields = [0,15,20,25,30]
    return filenames, labels, fields



#%% state 1 T dependence Cell4


def gatesweep_0T_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.031.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.034.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.036.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.034.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.036.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.038.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.041.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '25K',
              '50K',
              '75K',
              '100K',
              '143K',
              '290K',
              ]
    temperatures = [4.2, 10, 25, 50, 75, 100, 143, 290]
    return filenames, labels, temperatures



def gatesweep_15T_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.013.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.032.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.022.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.008.dat',
                 ]
    labels = ['4.2K',
              '25K',
              '50K',
              '143K',
              ]
    temperatures = [4.2, 25, 50, 143]
    return filenames, labels, temperatures



def gatesweep_20T_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.018.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.027.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.031.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.030.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.037.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.003.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.011.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.017.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.015.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '18K',
              '25K',
              '35K',
              '50K',
              '75K',
              '90K',
              '110K',
              '143K',
              '200K',
              ]
    temperatures = np.array([4.2, 10, 18, 25, 35, 50, 75, 90, 110, 143, 200])
    return filenames, labels, temperatures



def gatesweep_25T_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.020.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.029.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.033.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.028.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.039.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.024.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.013.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.017.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '18K',
              '25K',
              '35K',
              '50K',
              '75K',
              '90K',
              '110K',
              '143K',
              '200K',
              ]
    temperatures = np.array([4.2, 10, 18, 25, 35, 50, 75, 90, 110, 143, 200])
    return filenames, labels, temperatures



def gatesweep_30T_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.016.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.025.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.035.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.020.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.015.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.010.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.009.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.013.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '25K',
              '35K',
              '50K',
              '75K',
              
              '110K',
              '143K',
              '90K',
              '200K',
              ]
    
    newLabel = []
    temperatures = np.array([4.2, 10, 25, 35, 50, 75,  110, 143,90, 200])
    for temperature in temperatures :
        newLabel.append(str(temperature) + "k")
    
    return filenames, newLabel, temperatures


#%% State 1 field sweeps

def fieldsweep_state1():
    filenames = ['./2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.015.dat',
                 './2407-hgraphene/2024_06_30/g3-SD-4,9-V1-6,7-V2-24,10-V3-7,21-V4-5,24.028.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.003.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.012.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_02/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.040.dat',
                 './2407-hgraphene/2024_07_04/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.008.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '25K',
              '50K',
              '75K',
              '100K',
              '143K',
              ]
    temperatures = [4.2, 
                    10, 
                    143, 200, 50, 75, 90]
    return filenames, labels, temperatures

#%% Activation parameters

def activation_params_s1_plus2():
    left_lim = 60
    right_lim = 72
    start_index = [1,3,3]
    #start_index = 1
    stop_index = [4,-2,-2]
    #stop_index = 4
    return left_lim, right_lim, start_index, stop_index



def activation_results_s1_plus2():
    delta = np.array([0, 8.9443404, 20.95130822, 40.9817302])
    error = np.array([0, 0.39462961, 0.94233847, 2.01317141])
    label = r'25 min, $\nu$=+2'
    marker = '^'
    return delta, error, label, marker



def activation_params_s1_min2():
    left_lim = 25
    right_lim = 40
    start_index = [1,4,4]
    #start_index = 1
    stop_index = [3,-4,-2]
    #stop_index = 4
    return left_lim, right_lim, start_index, stop_index



def activation_results_s1_min2():
    delta = np.array([0, 8.49314269, 22.18362737, 38.70015497])
    error = np.array([0, 0.52836447, 1.13993807, 2.90546183])
    label = r'25 min, $\nu$=-2'
    marker = 'v'
    return delta, error, label, marker



def activation_params_s2_min2():
    left_lim = 35
    right_lim = 50
    start_index = [1,1,1]
    stop_index = [4,4,4]
    return left_lim, right_lim, start_index, stop_index



def activation_results_s2_min2():
    delta = np.array([0, 6.85047485, 17.17238901, 27.6404605])
    error = np.array([0, 0.10353937, 0.19465614, 1.01864601])
    label = r'30 min, $\nu$=-2'
    marker = 'v'
    return delta, error, label, marker



def activation_params_s2_min6():
    left_lim = -10
    right_lim = 15
    start_index = [0,1,1]
    #start_index = 0
    stop_index = [2,3,3]
    #stop_index = 2
    return left_lim, right_lim, start_index, stop_index



def activation_results_s2_min6():
    delta = np.array([0, 0.15239936, 1.66051922, 2.74619905])
    error = np.array([0, 0.04705888, 0.08525961, 0.03678114])
    label = r'30 min, $\nu$=-6'
    marker = 'h'
    return delta, error, label, marker



def activation_params_s3_min2():
    left_lim = 30
    right_lim = 50
    start_index = [1,1,1]
    stop_index = [3,3,3]
    return left_lim, right_lim, start_index, stop_index



def activation_results_s3_min2():
    delta = np.array([0, 0.55500702, 5.69151402, 15.59089765])
    error = np.array([0, 0.46965054, 0.02557817, 0.30212032])
    label = r'state 3, $\nu$=-2'
    marker = 'v'
    return delta, error, label, marker



def activation_params_s3_min6():
    left_lim = -10
    right_lim = 15
    start_index = [1,1,1]
    stop_index = [3,3,3]
    return left_lim, right_lim, start_index, stop_index



def activation_results_s3_min6():
    delta = np.array([0, 0.11086379, 1.3117515, 1.94694033])
    error = np.array([0, 0.0658903, 0.04242372, 0.10807018])
    label = r'state 3, $\nu$=-6'
    marker = 'h'
    return delta, error, label, marker



def activation_reference_plus2():
    fields = np.array([0,5,10,15,20,25,30])
    delta = np.array([0, 120, 560, 1100, 1550, 1950, 2240])
    label = r'pristine, $\nu$=+2'
    return fields, delta, label



def activation_reference_plus6():
    fields = np.array([0, 10,15,20,25,30])
    delta = np.array([0, 140, 270, 350, 390, 470])
    label = r'pristine, $\nu$=+6'
    return fields, delta, label



#%% B sweeps in SC2

def Bsweep_compare():
    filenames = ['./g11-1213-SD-9,4-V1-10,11-V2-12,15-V3-11,12-V4-15,6.006.dat',
                 './Hplasma/g11-1213-SD-10,4-V1-11,12-V2-12,15-V3-15,5.006.dat',
                 ]
    labels = ['0 min', '0.5 min']
    return filenames, labels



def Bsweep_pristine():
    filenames = [
                 './g11-1213-SD-9,4-V1-10,11-V2-12,15-V3-11,12-V4-15,6.008.dat',
                 './g11-1213-SD-9,4-V1-10,11-V2-12,15-V3-11,12-V4-15,6.012.dat',
                 ]
    labels = ['50V', '-50V', '0V']
    return filenames, labels



def Bsweep_plasma():
    filenames = ['./Hplasma/g11-1213-SD-10,4-V1-11,12-V2-12,15-V3-15,5.006.dat',
                 './Hplasma/g11-1213-SD-10,4-V1-11,12-V2-12,15-V3-15,5.008.dat',
                 './Hplasma/g11-1213-SD-10,4-V1-11,12-V2-12,15-V3-15,5.011.dat',
                 './Hplasma/g11-1213-SD-10,4-V1-11,12-V2-12,15-V3-15,5.014.dat',
                 ]
    labels = ['50V', '-50V', '-50V', '-50V']
    return filenames, labels


#%% state 2 T dependence Cell4

def gatesweep_0T_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.016.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.017.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.018.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.027.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.026.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '15K',
              '25K',
              '91K',
              '130K',
              ]
    temperatures = [4.2, 10, 15, 25, 91, 130]
    return filenames, labels, temperatures



def gatesweep_20T_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.011.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.003.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.005.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.014.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.021.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.023.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.002.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.005.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '15K',
              '25K',
              '50K',
              '130K',
              #'161K',
              #'200K',
              ]
    temperatures = [4.2, 10, 15, 25, 50, 130]
    return filenames, labels, temperatures



def gatesweep_25T_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.012.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.007.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.015.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.022.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.025.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '15K',
              '25K',
              '50K',
              '130K',
              ]
    temperatures = [4.2, 10, 15, 25, 50, 130]
    return filenames, labels, temperatures



def gatesweep_30T_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.010.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.002.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.013.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.020.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.001.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '15K',
              '25K',
              '50K',
              '130K',
              #'161K',
              #'200K',
              ]
    temperatures = [4.2, 10, 15, 25, 50, 130]
    return filenames, labels, temperatures



#%% state 2 field dependence Cell4


def gatesweep_4K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.016.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.009.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.011.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.012.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.010.dat',
                 ]
    labels = ['0T',
              '15T',
              '20T',
              '25T',
              '30T']
    fields = [0,15,20,25,30]
    return filenames, labels, fields



def gatesweep_10K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.017.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.003.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.002.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



def gatesweep_15K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.018.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.005.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.007.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.006.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



def gatesweep_25K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.014.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.015.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.013.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



def gatesweep_50K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.021.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.022.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.020.dat',
                 ]
    labels = ['20T',
              '25T',
              '30T']
    fields = [20,25,30]
    return filenames, labels, fields




def gatesweep_130K_state2():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.023.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.025.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields



#%% state 3 field dependence Cell4

def gatesweep_0T_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.030.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.031.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.032.dat',
                 #'./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 ]
    labels = ['4.2K',
              '55K',
              '100K',
              '150K',
              #'220K',
              ]
    temperatures = [4.2, 55, 100, 150]
    return filenames, labels, temperatures



def gatesweep_20T_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.007.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.021.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.029.dat',
                 ]
    labels = ['4.2K',
              '18K',
              '35K',
              '50K',
              ]
    temperatures = [4.2, 18, 35, 50]
    return filenames, labels, temperatures


def gatesweep_25T_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.009.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.023.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.025.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.028.dat',
                 ]
    labels = ['4.2K',
              '18K',
              '35K',
              '50K',
              ]
    temperatures = [4.2, 18, 35, 50]
    return filenames, labels, temperatures



def gatesweep_30T_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.027.dat',
                 ]
    labels = ['4.2K',
              '18K',
              '35K',
              '50K',
              ]
    temperatures = [4.2, 18, 35, 50]
    return filenames, labels, temperatures



#%% state 3 T dependence Cell4

def gatesweep_4K_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.011.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.007.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.009.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 ]
    labels = ['0T',
              '15T',
              '20T',
              '25T',
              '30T',
              ]
    fields = [0,15,20,25,30]
    return filenames, labels, fields



def gatesweep_18K_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.021.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.023.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 ]
    labels = ['20T',
              '25T',
              '30T']
    fields = [20,25,30]
    return filenames, labels, fields



def gatesweep_35K_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.026.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.025.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 ]
    labels = ['20T',
              '25T',
              '30T']
    fields = [20,25,30]
    return filenames, labels, fields



def gatesweep_50K_state3():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.030.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.029.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.028.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.027.dat',
                 ]
    labels = ['0T',
              '20T',
              '25T',
              '30T']
    fields = [0,20,25,30]
    return filenames, labels, fields


# %% Raman data


def data_raman_300():
    files = ['2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_0min_5x60s_225uW.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_5min_5x60s_225uW_300gr.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_15min_5x60s_225uW_300gr_good.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_30min_5x60s_225uW_300gr.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_60min_5x60s_225uW_300gr.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_60min_annealed_5x60s_225uW_300gr.csv'
            ]
    labels = ['pristine',
          '5 min',
          '15 min',
          '30 min',
          '60 min',
          'annealed'
          ]
    exposures = [0, 5, 15, 30, 60]
    return files, labels, exposures



def data_raman_300_limited():
    files = ['2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_0min_5x60s_225uW.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_30min_5x60s_225uW_300gr.csv',
            '2503-plasma chamber Raman/250315_Graphene_Raman/14_03_2025/graphene_60min_annealed_5x60s_225uW_300gr.csv'
            ]
    labels = ['pristine',
          '30 min H',
          'annealed'
          ]
    return files, labels

# %% Old data for comparison

def Elias_peaks():
    temperatures = [280, 242, 160, 120, 80, 40, 20, 10, 4.2]
    peaks_elias = np.array([21792.5704, 24159.31282, 29691.81978, 35258.48777, 44336.98625, 70916.33267, 120116.3122, 230772.5131, 497184.3078])
    return peaks_elias, temperatures



def g12_6244_0s():
    temperatures = [294, 4.2, 15, 17, 100, 200]
    peaks = np.array([877.2708217949934, 871.5461154784771, 751.1777363011745, 808.4311225657832, 828.88437109649, 889.8353133125987])
    return peaks, temperatures



def g12_6244_10s():
    temperatures = [294, 140, 13, 4.2]
    peaks = np.array([952.4097651762045, 1040.4955517601775, 977.3829496594149, 727.1153836341277])
    return peaks, temperatures



def g12_6244_20s():
    temperatures = [4.2, 10, 50, 80, 140, 293]
    peaks = np.array([2043.04793716, 2078.20924487, 1934.21590708, 2470.61772065, 2804.10220259, 2558.2526797])
    return peaks, temperatures



def g12_6244_80s():
    temperatures = [210, 146, 80, 20, 30, 50, 4.2,] #4.2, 10, 20]
    peaks = np.array([3413.84256568, 3542.88441985, 3716.83990584, 4148.462896500577, 4155.30259766, 3909.7119852, #3877.0917636900167, 
                      6085.81775256, ])
                      #4066.5365786, 3636.03371433])
    return peaks, temperatures



def g11_1213_0s():
    temperatures = [297, 220, 77, 4.2]
    peaks = np.array([765.9659900981955, 676.5443227558767, 668.4844050118182, 639.3954911238202])
    return peaks, temperatures



def g11_1213_30s():
    temperatures = [297, 90, 4.2, 15.8, 9.6]
    peaks = np.array([1132.3191646025226, 1283.4075249383532, 2170.1600036143507, 1675.4633453961358, 1794.8628492106087])
    return peaks, temperatures



def g3_5min():
    temperatures = [99,270,280]
    peaks = np.array([929.3567071, 951.7830126, 954.62658422])
    peaks_errors = np.array([0.22860455, 0.12613744, 0.11277837])
    exposure = 5
    return peaks, peaks_errors, temperatures, exposure


def g3_25min():
    temperatures = [4.2, 10, 25, 50, 75, 100, 143, 290]
    peaks = np.array([2548.35854442, 2349.40395326, 2055.55641769, 1852.77254015, 1754.88642818, 1707.17262644, 1657.966548, 1510.22211968])
    peaks_errors = np.array([3.21385874, 2.46536022, 1.10364585, 1.09770796, 0.55550896, 0.43989325, 0.30711146, 0.21686109])
    exposure = 25
    return peaks, peaks_errors, temperatures, exposure


def g3_30min():
    temperatures = [4.2, 10, 15, 25, 91, 130]
    peaks = np.array([6197.87209357, 5874.15782222, 5542.41262075, 5047.12924237, 4227.21796113, 3935.56238886])
    peaks_errors = np.array([10.93255411, 10.23634047,  5.5162457,   8.77697184,  1.17447196,  3.12692861])
    exposure = 30
    return peaks, peaks_errors, temperatures, exposure

#%% New datasets 


def gatesweep_0T_state23():
    filenames = ['./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.030.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.031.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.032.dat',
                 #'./2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-7,21-V4-5,24.001.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.016.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.017.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.018.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.027.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.026.dat',
                 ]
    labels = ['4.2K',
              '55K',
              '100K',
              '150K',
              #'220K',
              '4.2K',
              '10K',
              '15K',
              '25K',
              '91K',
              '130K',
              ]
    temperatures = [4.2, 55, 100, 150, 4.2, 10, 15, 25, 91, 130]
    return filenames, labels, temperatures



def gatesweep_30T_state23():
    filenames = ['./2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.010.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.002.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.006.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.013.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.020.dat',
                 './2407-hgraphene/2024_07_06/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.001.dat',
                 #'./2407-hgraphene/2024_07_07/g3-SD-4,9-V1-6,8-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.004.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.019.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.024.dat',
                 './2407-hgraphene/2024_07_05/g3-SD-4,9-V1-6,7-V2-5,6-V3-8,10-V4-5,24.027.dat',
                 ]
    labels = ['4.2K',
              '10K',
              '15K',
              '25K',
              '50K',
              '130K',
              #'161K',
              #'200K',
              '4.2K',
              '18K',
              '35K',
              '50K',
              ]
    temperatures = [4.2, 10, 15, 25, 50, 130, 4.2, 18, 35, 50]
    return filenames, labels, temperatures



def mass_eff_summary():
    carbons = np.array([200.,128.,98.,50.,32.,8.,2.])
    coverage = 100./carbons
    mass_eff = [0.050806364, 0.059058855, 0.0814048, 0.1430601, 0.193749799, 0.609871527, 1.116345321]
    bandgap = [0.0587999, 0.0895901, 0.1109858, 0.207787, 0.298935, 1.159326, 4.49988]
    return coverage, mass_eff, bandgap

