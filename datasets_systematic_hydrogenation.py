#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Create datasets for analysis

Created on Tue Jan 17 09:32:46 2023

@author: ivrens
"""

import numpy as np
import matplotlib.pyplot as plt


def compose_filename_exposure(folder, identifier, index):
    filename = f'''./{folder}/{folder}-{identifier}.{index:03}.dat'''
    return filename


#%% Datasets gate sweep

def sweep_stabilisation():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    edited = '_edited'
    filename_edited = compose_filename_exposure(folder=sample, identifier=sequence+edited, index=61)
    filelist = [63, 65, 67, 69, 71]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames.insert(0,filename_edited)
    stableLabels = ['1 hr', '1 day', '7 days', '14 days', '15 days', '16 days']
    return filenames, stableLabels


def sweep_morning():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [7, 18, 32, 42, 60, 71, 82, 90, 93]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    slowLabels = ['0 min', '1 min', '4 min', '6 min', '9 min', '19 min', '23 min', '33 min', '43 min', '53 min']
    return filenames, slowLabels


def sweep_annealing():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [7, 18, 42, 60, 82, 90]
    #filelist = [90]
    sequence2 = 'SD-14,11,17-V1-17,11-V2-12,11-after annealing'
    filelist2 = [2, 5]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    filenames = filenames + ([compose_filename_exposure(folder=sample, identifier=sequence2, index=nr) for nr in filelist2])
    slowLabels = ['0 min', '1 min', '4 min', '9 min', '19 min', '33 min', '43 min', 'annealing 180 $^\circ$C', 'annealing 400 $^\circ$C']
    #slowLabels = ['0 min', '43 min', 'annealing 180 $^\circ$C', 'annealing 400 $^\circ$C']
    return filenames, slowLabels


def sweep_annealing2():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [7, 18, 42, 60, 82, 90, 95]
    sequence2 = 'SD-14,11,17-V1-17,11-V2-12,11-after annealing'
    filelist2 = [2, 5]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    filenames = filenames + ([compose_filename_exposure(folder=sample, identifier=sequence2, index=nr) for nr in filelist2])
    slowLabels = ['0 min', '1 min', '4 min', '9 min', '19 min', '33 min', '43 min', '53 min', 'annealing 180 $^\circ$C', 'annealing 400 $^\circ$C']
    return filenames, slowLabels


def sweep_fast():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [2, 9, 13, 16, 20, 30, 34, 42, 45, 49, 54, 58, 60, 61, 74, 80, 85, 88, 93]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    fastLabels = filelist
    return filenames, fastLabels


def sweep_1min():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [2, 9, 13, 16, 20, 30, 34]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    minLabels = [f"{time} min" for time in range(0, 8)]
    return filenames, minLabels


def sweep_2min():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [34, 42, 45, 49, 54, 58, 60]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    minLabels = [f"{2*time+7} min" for time in range(7)]
    return filenames, minLabels


def sweep_5min():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [60, 61, 74, 80, 85, 88, 93]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    minLabels = ['19 min', '23 min', '28 min', '33 min', '38 min', '43 min', '53 min']
    return filenames, minLabels


def sweep_annealing3():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [95, 97]
    sequence2 = 'SD-14,11,17-V1-17,11-V2-12,11-after annealing'
    filelist2 = [2, 5]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = filenames + ([compose_filename_exposure(folder=sample, identifier=sequence2, index=nr) for nr in filelist2])
    minLabels = filelist + filelist2
    return filenames, minLabels


def sweep_annealing4():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [95]
    sequence2 = 'SD-14,11,17-V1-17,11-V2-12,11-after annealing'
    filelist2 = [2, 5]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    filenames = filenames + ([compose_filename_exposure(folder=sample, identifier=sequence2, index=nr) for nr in filelist2])
    minLabels = filelist0 + filelist + filelist2
    return filenames, minLabels


def sweep_offset():
    sample = 'g2'
    sequence0 = 'SD-14,11,17-V1-17,11-V2-12,13'
    filelist0 = [1]
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [7, 18, 42, 60, 82, 90]
    #filelist = [42, 60, 82, 90]
    #filelist = [90]
    sequence2 = 'SD-14,11,17-V1-17,11-V2-12,11-after annealing'
    filelist2 = [2]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    filenames = ([compose_filename_exposure(folder=sample, identifier=sequence0, index=nr) for nr in filelist0] + filenames)
    filenames = filenames + ([compose_filename_exposure(folder=sample, identifier=sequence2, index=nr) for nr in filelist2])
    slowLabels = ['0 min', '1 min', '4 min', '9 min', '19 min', '33 min', '43 min', 'annealing 180 $^\circ$C']
    #slowLabels = ['0 min', '9 min', '19 min', '33 min', '43 min', 'annealing 180 $^\circ$C']
    return filenames, slowLabels


# %% Datasets exposure
def time_stable():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [62, 64, 66, 68, 70]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    stableLabels = filelist
    return filenames, stableLabels


def time_exposure1min():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [1, 8, 12, 15, 19, 29, 33]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = [f"{time} min" for time in range(1, 8)]
    return filenames, timeLabels


def time_exposure2min():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [41, 44, 48, 52, 57, 59]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = [f"{2*time+7} min" for time in range(1, 7)]
    return filenames, timeLabels


def time_exposure5min():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [61, 72, 78, 83, 86, 91]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = ['23 min', '28 min', '33 min', '38 min', '43 min', '53 min']
    return filenames, timeLabels


def time_exposure_all():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-plasma'
    filelist = [1, 8, 12, 15, 19, 29, 33, 41, 44, 48, 52, 57, 59, 61, 72, 78, 83, 86, 91]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    minLabels = filelist
    return filenames, minLabels


# %% Datasets annealing
def annealing():
    sample = 'g2'
    sequence = 'SD-14,11,17-V1-17,11-V2-12,11-annealing-last'
    filelist = [1]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    minLabels = filelist
    return filenames, minLabels


# %% Datasets other than g2
def c5_firststeps():
    sample = 'C5'
    sequence = 'SD-10,6-11,12-plasma'
    filelist = [2, 4, 6, 8, 10, 12, 14, 16]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    c5Labels = filelist
    return filenames, c5Labels


def c5_cumulative():
    sample = 'C5'
    sequence = 'SD-10,6-11,12-plasma'
    filelist = [21, 23, 25, 27, 29, 31, 33]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    c5Labels = ['air exposure', '1 min', '3 min', '4 min', '9 min', '13 min', 'annealed 180$^\circ$C']
    return filenames, c5Labels


def c5_day2():
    sample = 'C5'
    sequence = 'SD-10,6-11,12-plasma'
    filelist = [16, 18, 20, 21, 23, 25, 27, 29, 31, 33]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    c5Labels = filelist
    return filenames, c5Labels


def g1_exposure():
    sample = 'g1'
    sequence1 = 'SD-10,14-V1-11,12'
    sequence2 = 'SD-14,10-V1-12,15-after-ann'
    sequence3 = 'SD-14,10-V1-12,15-plasma'
    files1 = 1
    files2 = 1
    files3 = [2, 4, 6, 8, 10, 11, 14]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence1, index=files1), compose_filename_exposure(folder=sample, identifier=sequence2, index=files2)]
    filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence3, index=nr) for nr in files3]
    g1Labels = ['PMMA', 'annealed 170$^\circ$C', '1 min', '4 min', '9 min', 'RT']
    return filenames, g1Labels


def c4_arh2_sweeps():
    sample = 'C4'
    sequence1 = 'SD-12,9-V1-10,11-after-ann'
    sequence2 = 'SD-12,9-V1-10,11-after-ann-2nd'
    sequence3 = 'SD-12,9-V1-10,11-plasma'
    files1 = 1
    files2 = 1
    files3 = [2, 5, 7, 9, 11, 13, 15]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence1, index=files1)] 
    filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence3, index=nr) for nr in files3]
    filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence2, index=files2)]
    c4Labels = ['annealed 165$^\circ$C', '30 sec', '1 min', '1.5 min', '2 min', '5 min', '21 min', '36 min', 'annealed 165$^\circ$C']
    return filenames, c4Labels


def c4_h2_sweeps():
    sample = 'C4'
    sequence1 = 'SD-12,9-V1-10,11-after-ann-2nd'
    # sequence2 = 'SD-12,9-V1-10,11-after-ann3-rd'
    sequence3 = 'SD-12,9-V1-10,11-plasma-2nd'
    files1 = 1
    # files2 = 1
    files3 = [2, 4, 6, 8]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence1, index=files1)] 
    filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence3, index=nr) for nr in files3]
    # filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence2, index=files2)]
    c4Labels = ['annealed', '30 sec', '1 min', '3 min', '7 min']
    return filenames, c4Labels


def c4_annealed():
    sample = 'C4'
    sequence0 = 'SD-12,9-V1-10,11-after-ann3-rd'
    sequence = 'SD-12,9-V1-10,11-ann-300'
    filelist0 = 1
    filelist = range(1, 8)
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence0, index=filelist0)] 
    filenames = filenames + [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    c4Labels = ['170C', '300C, 1 min', '300C, 3 min', '350C, 1 min', '500C, 1 min', '500C, 2 min', '400C, 30 min', '400C, 12 h']
    return filenames, c4Labels


def c4_arh2_exposures():
    sample = 'C4'
    sequence = 'SD-12,9-V1-10,11-plasma'
    filelist = [1, 4, 6, 8, 10, 12, 14]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = ['30 sec', '1 min', '1.5 min', '2 min', '5 min', '21 min', '36 min']
    return filenames, timeLabels


def c4_h2_exposures():
    sample = 'C4'
    sequence = 'SD-12,9-V1-10,11-plasma-2nd'
    filelist = [1, 3, 5, 7, 9]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = ['30 sec', '1 min', '3 min', '7 min', '27 min']
    return filenames, timeLabels


def c4_annealing():
    sample = 'C4'
    sequence = 'SD-12,9-V1-10,11-annealing-3rd'
    filelist = [1]
    filenames = [compose_filename_exposure(folder=sample, identifier=sequence, index=nr) for nr in filelist]
    timeLabels = ['30 sec', '1 min', '3 min', '7 min', '27 min']
    return filenames, timeLabels