# -*- coding: utf-8 -*-
"""
Spyder Editor

This function plots the resistance as function of gate voltage for several datasets.
"""
# %% Packages
import numpy as np
import matplotlib.pyplot as plt
import datasets_systematic_hydrogenation as datasets
from cycler import cycler


# %% Functions
def compose_filename_exposure(folder, identifier, index):
    filename = f'''./{folder}/{folder}-{identifier}.{index:03}.dat'''
    return filename


def read_var(filename, col):
    var = np.loadtxt(filename, unpack=True, skiprows=2, usecols=col)
    return var


def find_col(filename, var):
    # TODO write a function to read a variable name, and return the associated column 
    with open(filename) as f:
        print(f)
    return 0


def find_hv(filename):
    time = read_var(filename=filename, col=0)
    exposure_start = time[0]
    time = read_var(filename=filename, col=0)
    V_plasma = read_var(filename=filename, col=10)
    for i in range(len(V_plasma)):
        if V_plasma[i]>0.1:
            exposure_start = time[i]
            break
    return exposure_start


def calc_r(filename):
    '''
    Returns resistance in Ohm for channel 1
    '''
    SD_R = read_var(filename=filename, col=4)*0.001
    V1_R = read_var(filename=filename, col=6)
    resistance = V1_R/SD_R
    return resistance


def select_backsweep(filename):
    '''
    The backsweep is marked by a small step in gate voltage. It must start away
    from 0 gate voltage. The end of the backsweep is again marked by a small
    step in gate voltage, and there must be a significant difference between
    the gate voltage at the start and end of the backsweep.
    Alternative boundaries for C4, where the lower gate voltage limit is 0V.
    '''
    Vg_V = read_var(filename=filename, col=2)
    R1 = calc_r(filename=filename)/1000
    # Backsweep (either up or down):
    # Tweak boundary values
    downsweep_start = next(i for i in range(len(Vg_V)) if abs(Vg_V[i])>10 and abs(Vg_V[i]-Vg_V[i-2])<0.195)
    downsweep_end = next((i for i in range(downsweep_start,len(Vg_V)) if abs(Vg_V[i]-Vg_V[i-2])<0.195 and abs(Vg_V[i]-Vg_V[downsweep_start])>25), len(Vg_V))
    # Full sweep while Vg is changing:
    # downsweep_start = next(i for i in range(len(Vg_V)) if abs(Vg_V[i]-Vg_V[i-2])>0.095)
    # downsweep_end = next((i for i in range(len(Vg_V)-1, downsweep_start, -1) if abs(Vg_V[i]-Vg_V[i-2])>0.095), len(Vg_V))
    # Forward sweep from 0:
    # downsweep_start = 0
    # downsweep_end = next((i for i in range(downsweep_start,len(Vg_V)) if abs(Vg_V[i]-Vg_V[i-2])<0.195 and abs(Vg_V[i]-Vg_V[downsweep_start])>2), len(Vg_V))
    Vg_down = Vg_V[downsweep_start:downsweep_end]
    R1_down = R1[downsweep_start:downsweep_end]
    return Vg_down, R1_down



# %% Plotting function

def fnct_thesis_stabilisation():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 20})
    #plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[16,7])
    ax_stability_time = fig.add_axes([0.05, 0.15, 0.4, 0.8])
    ax_stability_sweep = fig.add_axes([0.55, 0.15, 0.4, 0.8])
    ax_stability_time.annotate('a', [0.03, 0.95], xycoords='figure fraction', annotation_clip=False, fontweight='bold')
    ax_stability_sweep.annotate('b', [0.53, 0.95], xycoords='figure fraction', annotation_clip=False, fontweight='bold')

    ax_stability_time_voltage = ax_stability_time.twinx()

    dataset_sweep, labels_sweep = datasets.sweep_stabilisation()
    t0 = find_hv(filename=dataset_sweep[0])
    Vg_CNPs = []
    CNP_times = []
    for file_sweep, label_sweep in zip(dataset_sweep, labels_sweep):
        print(file_sweep)
        Vg_V, R1 = select_backsweep(filename=file_sweep)
        R1 = calc_r(filename=file_sweep)/1000
        time = read_var(filename=file_sweep, col=0)
        Vg_V = read_var(filename=file_sweep, col=2)
        ax_stability_sweep.plot(Vg_V, R1, linewidth=1, label=label_sweep)
        ax_stability_time.plot((time-t0)*10**-3/(60*60), R1)
        ax_stability_sweep.legend()
        Vg_CNPs.append(Vg_V[np.argmax(R1)])
        CNP_times.append((time[np.argmax(R1)]-t0)*10**-3/(60*60))
    
    ax_stability_sweep.set_xlabel('Gate voltage (V)')
    ax_stability_sweep.set_ylim(bottom=0)
    ax_stability_sweep.tick_params(direction='in')

    dataset_time, labels_time = datasets.time_stable()
    for file_time in dataset_time:
        R1 = calc_r(file_time)/1000
        time = read_var(filename=file_time, col=0)
        #max_time=max(time-t0)*10**-3/(60*60)
        print(file_time)
        ax_stability_time.plot((time-t0)*10**-3/(60*60), R1, color='k')
    
    ax_stability_time_voltage.plot(CNP_times, Vg_CNPs, c='gray', linestyle=':', marker='o')
    ax_stability_time_voltage.set_ylabel(r'$V_{CNP}(V)$', c='gray')
    #ax_stability_time_voltage.set_yticklabels(c='gray')
    ax_stability_time_voltage.annotate("", [0.95, 0.15],[0.1, 0.15], xycoords='axes fraction', arrowprops=dict(arrowstyle='->', color='grey'), annotation_clip=False,)
    #ax_stability_time.set_xlim(900,1800)
    ax_stability_time_voltage.tick_params(direction='in')
    ax_stability_time_voltage.spines['right'].set_color('gray')
    ax_stability_time_voltage.tick_params(axis='y', colors='gray')
    ax_stability_time.tick_params(direction='in')
    ax_stability_time.set_ylabel('Resistance (k$\Omega$)')
    ax_stability_time.set_xlabel('time (hr)')
    ax_stability_time.set_ylim(bottom=0)

    plt.savefig('stabilization.png')


# %% Execute code
fnct_thesis_stabilisation()
