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



def calc_r(filename, col):
    '''
    Returns resistance in Ohm for a chosen channel (int)
    '''
    V_R = read_var(filename=filename, col=col)
    resistance = V_R / 1E-9
    return resistance



def peak_resistance(filename, col):
    resistance = calc_r(filename, col)
    return max(abs(resistance))



def select_backsweep(filename, col_Vg):
    '''
    Find at which step the gate voltage is at its max and min by manually inserting the sweep range.
    '''
    Vg_V = read_var(filename=filename, col=col_Vg)
    # Backsweep (either up or down):
    # Tweak boundary values
    downsweep_start = next(i for i in range(len(Vg_V)) if (Vg_V[i])>50)
    downsweep_end = next(i for i in range(len(Vg_V)) if (Vg_V[i])<-50)
    return downsweep_start, downsweep_end
