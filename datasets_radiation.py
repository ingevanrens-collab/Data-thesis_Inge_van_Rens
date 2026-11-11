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



#%% Radiation experiments


def gatesweeps_timelapse_21():
    filenames = [#'./2026-07-07/graphenea2.1_testsweep_SD_4,2.001.dat',
                 './2026-07-07/graphenea2.1_testsweep_SD_4,2.002.dat',
                 #'./2026-07-09/graphenea2.1_testsweep_SD_4,2.001.dat',
                 #'./2026-07-09/graphenea2.1_testsweep_SD_4,2.002.dat',
                 './2026-07-09/graphenea2.1_testsweep_SD_4,2.003.dat',
                 #'./2026-07-09/graphenea2.1_testsweep_SD_7,2_gate11.001.dat',
                 './2026-07-09/graphenea2.1_testsweep_SD_7,2_gate11.002.dat',
                 #'./2026-07-13/graphenea2.1_testsweep_SD_6,2_gate11.003.dat',
                 './2026-07-13/graphenea2.1_testsweep_SD_6,2_gate11.004.dat',
                 #'./2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.001.dat',
                 #'./2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.002.dat',
                 './2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.003.dat',
                 #'./2026-07-17/graphenea2.1_testsweep_SD_6,2_gate11.001.dat',
                 './2026-07-17/graphenea2.1_testsweep_SD_6,2_gate11.002.dat',
                 ]
    time_days = [0,#0,
                 2,#2,2,
                 2.5,#2.5,
                 6,#6,
                 9,#9,9,
                 10,#10
                 ]
    column_Vg = [3,#3,
                 1,#1,1,
                 1,#1,
                 1,#1,
                 1,#1,1,
                 1,#1,
                 ]
    column_V1x = [1,#1,
                  3,#3,3,
                  3,#3,
                  3,#3,
                  3,#3,3,
                  3,#3,
                  ]
    return filenames, time_days, column_Vg, column_V1x

def gatesweeps_timelapse_21_constant_contacts():
    filenames = [#'./2026-07-07/graphenea2.1_testsweep_SD_4,2.001.dat',
                 './2026-07-07/graphenea2.1_testsweep_SD_4,2.002.dat',
                 #'./2026-07-09/graphenea2.1_testsweep_SD_4,2.001.dat',
                 './2026-07-09/graphenea2.1_testsweep_SD_4,2.002.dat',
                 './2026-07-09/graphenea2.1_testsweep_SD_4,2.003.dat',
                 ]
    labels = ['Initial sweep',
              'After 2 days',
              'After 2.5 days'
              ]
    column_Vg = [3,#3,
                 1,#1,1,
                 1,#1,
                 ]
    column_V1x = [1,#1,
                  3,#3,3,
                  3,#3,
                  ]
    return filenames, labels, column_Vg, column_V1x


def gatesweeps_timelapse_21_late():
    filenames = [#'./2026-07-13/graphenea2.1_testsweep_SD_6,2_gate11.003.dat',
                 './2026-07-13/graphenea2.1_testsweep_SD_6,2_gate11.004.dat',
                 #'./2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.001.dat',
                 #'./2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.002.dat',
                 './2026-07-16/graphenea2.1_testsweep_SD_6,2_gate11.003.dat',
                 #'./2026-07-17/graphenea2.1_testsweep_SD_6,2_gate11.001.dat',
                 './2026-07-17/graphenea2.1_testsweep_SD_6,2_gate11.002.dat',
                 ]
    labels = ['Initial sweep',
              'After 3 days',
              'After 4 days'
              ]
    column_Vg = [1,#1,
                 1,#1,1,
                 1,#1,
                 ]
    column_V1x = [3,#3,
                  3,#3,3,
                  3,#3,
                  ]
    return filenames, labels, column_Vg, column_V1x


def gatesweeps_before_after_beta():
    filenames = [
        #'./2026-07-09/graphenea2.3_testsweep_SD_10,2_gate11.001.dat',
        './2026-07-09/graphenea2.3_testsweep_SD_10,2_gate11.002.dat',
        #'./2026-07-14/graphenea2.3_testsweep_SD_10,2_gate11.001.dat',
        './2026-07-14/graphenea2.3_testsweep_SD_10,2_gate11.002.dat',
        #'./2026-07-16/graphenea2.3_testsweep_SD_10,2_gate1.001.dat',
        #'./2026-07-16/graphenea2.3_testsweep_SD_10,2_gate1.002.dat',
        './2026-07-16/graphenea2.3_testsweep_SD_10,2_gate1.003.dat',
    ]
    labels = [
        'Initial sweep',
        'Before beta exposure',
        'After beta exposure',
    ]
    return filenames, labels


def gatesweeps_before_after_alpha():
    filenames = [
        './2026-07-09/graphenea2.4_testsweep_SD_7,2_gate11.003.dat',
        './2026-07-16/graphenea2.4_testsweep_SD_10,2_gate1.002.dat',
        './2026-07-17/graphenea2.4_testsweep_SD_10,2_gate11.002.dat',
    ]
    labels = [
        'Initial sweep',
        'Before alpha exposure',
        'After alpha exposure',
    ]
    return filenames, labels