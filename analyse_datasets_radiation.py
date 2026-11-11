# -*- coding: utf-8 -*-
"""
Spyder Editor

This function plots the resistance as function of gate voltage for several datasets.
"""
# %% Packages
import numpy as np
import math
import matplotlib.pyplot as plt
import datasets_radiation as datasets
import extract_data_radiation as extract_radiation
from cycler import cycler
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from PIL import Image


# %% Functions


# %% Plotting functions

def fnct_plot_timelapse():
    (file_timestamp,labels,col_Vg,col_V1x) = datasets.gatesweeps_timelapse_21_late()
    cmap = mpl.colormaps['hsv']
    #colors = cmap(np.linspace(0, 1, len(file_timestamp)))
    for i in range(len(file_timestamp)):
        print(file_timestamp[i])
        R = extract_radiation.calc_r(filename=file_timestamp[i], col=col_V1x[i])/1000
        Vg_V = extract_radiation.read_var(filename=file_timestamp[i], col=col_Vg[i])
        plt.plot(Vg_V, R, label=labels[i])
    plt.legend()
    plt.tick_params('both', direction='in')
    plt.ylim(bottom=0)
    plt.xlim(left=0,right=40)
    plt.ylabel(r'$R$(k$\Omega$)')
    plt.xlabel(r'$V_G$(V)')        
    plt.savefig('gatesweeps_timelapse.png')



def fnct_plot_beta_damage():
    (file_beta_damage,label_beta_damage) = datasets.gatesweeps_before_after_alpha()
    cmap = mpl.colormaps['plasma']
    colors = cmap(np.linspace(0, 1, len(file_beta_damage)))
    for i in range(len(file_beta_damage)):
        print(file_beta_damage[i])
        R = extract_radiation.calc_r(filename=file_beta_damage[i], col=3)/1E6
        Vg_V = extract_radiation.read_var(filename=file_beta_damage[i], col=1)
        plt.plot(Vg_V, R, label=label_beta_damage[i])
    plt.legend()
    plt.tick_params('both', direction='in')
    plt.ylim(bottom=0)
    plt.xlim(left=0,right=40)
    plt.ylabel(r'$R$(k$\Omega$)')
    plt.xlabel(r'$V_G$(V)')
        
    plt.savefig('gatesweeps_alpha_damage.png')
# %% Execute code
fnct_plot_beta_damage()