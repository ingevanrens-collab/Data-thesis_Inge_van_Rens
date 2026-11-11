# -*- coding: utf-8 -*-
"""
Spyder Editor

This function plots the resistance as function of gate voltage for several datasets.
"""
# %% Packages
import numpy as np


#%% functions

def read_var(filename, col):
    var = np.loadtxt(filename, unpack=True, skiprows=1, usecols=col)
    return var



def calc_r(filename, channel):
    '''
    Returns resistance in Ohm for a chosen channel (int)
    '''
    SD_R = read_var(filename=filename, col=6)
    V_R = read_var(filename=filename, col=6+2*channel)
    Theta_SD = read_var(filename=filename, col=7)
    Theta = read_var(filename=filename, col=7+2*channel)
    resistance = 1000*V_R/SD_R #* np.cos((Theta-Theta_SD+180)*np.pi/180)
    return resistance



def peak_resistance(filename, channel):
    resistance = calc_r(filename, channel)
    return max(abs(resistance))



def find_valley(filename, channel, left_lim=0, right_lim=70):
    resistance = calc_r(filename, channel)
    Vg_V = read_var(filename=filename, col=5)
    nu_range = [i for i in range(len(resistance)) if  Vg_V[i]>left_lim and Vg_V[i]<right_lim]
    return min(abs(resistance[nu_range[0]:nu_range[-1]]))




def select_backsweep(filename, channel):
    '''
    Find at which step the gate voltage is at its max and min by manually inserting the sweep range.
    '''
    Vg_V = read_var(filename=filename, col=4)
    # Backsweep (either up or down):
    # Tweak boundary values
    downsweep_start = next(i for i in range(len(Vg_V)) if (Vg_V[i])>50)
    downsweep_end = next(i for i in range(len(Vg_V)) if (Vg_V[i])<-50)
    return downsweep_start, downsweep_end
