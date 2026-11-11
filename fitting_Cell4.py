# -*- coding: utf-8 -*-
"""
Spyder Editor

This function plots the resistance as function of gate voltage for several datasets.
"""
# %% Packages
import scipy
import numpy as np
import scipy.optimize



def lin(x, a, b):
    return a*x+b



def gaussian(x, a, b, c):
    return a*np.exp(-((x-b)**2)/(2*c**2))



def vrh(T, sigma_0, T_0):
    beta = 1/3
    return sigma_0 * np.exp( -(T_0/T )**beta )
    


def power_five(x, a, b, c, d, e, f):
    return a + b*x + c*x**2 + d*x**3 + e*x**4 + f*x**5



def peak_fit(Vg, R, left_edge, right_edge):
    selected_Vg = np.zeros(1)
    selected_R = np.zeros(1)
    for i in range(len(Vg)):
        if Vg[i]>left_edge and Vg[i]<right_edge:
            selected_Vg = np.append(selected_Vg, np.array(Vg[i]))
            selected_R = np.append(selected_R, np.array(R[i]))
    popt, pcov = scipy.optimize.curve_fit(gaussian, selected_Vg, selected_R, p0=[5, 55, 55])
    perr = np.sqrt(np.diag(pcov))
    return popt, perr



def valley_fit(Vg, R, left_edge, right_edge):
    selected_Vg = np.zeros(1)
    selected_R = np.zeros(1)
    for i in range(len(Vg)):
        if Vg[i]>left_edge and Vg[i]<right_edge:
            selected_Vg = np.append(selected_Vg, np.array(Vg[i]))
            selected_R = np.append(selected_R, np.array(R[i]))
    popt, pcov = scipy.optimize.curve_fit(power_five, selected_Vg, selected_R)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr



def temperature_fit(temperatures, peak_resistance, peak_error=None):
    conductivity = 1/peak_resistance
    popt, pcov = scipy.optimize.curve_fit(vrh, temperatures, conductivity, p0=[1e-3, 4], sigma=peak_error)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr



def activation_fit(inv_temperatures, resistance):
    print(len(resistance))
    logR = np.log(resistance)
    popt, pcov = scipy.optimize.curve_fit(lin, inv_temperatures, logR)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr



def linear_fit(x, y, sigma='None'):
    popt, pcov = scipy.optimize.curve_fit(lin, x, y, sigma=sigma)
    perr = np.sqrt(np.diag(pcov))
    return popt, perr


