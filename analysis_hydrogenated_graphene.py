# -*- coding: utf-8 -*-
"""
Spyder Editor

This file contains plotting functions for figure specifically for my thesis.
"""

# %% Packages
import numpy as np
import math
import matplotlib.pyplot as plt
import datasets_combined as datasets
import fitting_Cell4 as fit_cell4
import extract_data_Cell4 as extract_cell4
import extract_plasmachamber as extract_plasma
from cycler import cycler
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

from PIL import Image

# %% Functions

def find_activation(dataset, channel, temperatures, left_lim, right_lim, start_index=0, stop_index=-1):
    inv_temp = 1/np.array(temperatures)
    valleys = np.zeros(shape=(len(dataset)))
    for i, file in enumerate(dataset):
        valley = extract_cell4.find_valley(file, channel, left_lim, right_lim)
        valleys[i] = valley
    fitparams, sigma = fit_cell4.activation_fit(inv_temp[start_index:stop_index+1], valleys[start_index:stop_index+1])
    return fitparams, sigma


# %% Plotting functions

def fnct_fig_raman():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 16})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[10,8])
    ax_raman_left = fig.add_axes([0.05, 0.06, 0.44, 0.88])
    ax_raman_right = fig.add_axes([0.52, 0.06, 0.44, 0.88])
    
    files, labels, exposures = datasets.data_raman_300()
    cmap = mpl.colormaps['plasma']
    n_lines=len(files)
    colors = cmap(np.linspace(0, 1, n_lines))
    #colors_raman = [colors[exp] for exp in exposures]
    colors_raman = list(colors)
    colors_raman.pop()
    colors_raman.append('grey')

    for i, filename in enumerate(files):
        wavelength, intensity = extract_plasma.read_var(filename, col=[0,1])
        wavenumber = 1E7/532.089 - 1E7/wavelength
        indices_scaling_peak_Si = np.where((wavenumber > 500) & (wavenumber < 525))
        scaling_factor_Si = np.sum(intensity[indices_scaling_peak_Si])/len(indices_scaling_peak_Si[0])

        ax_raman_left.plot(wavenumber, intensity/scaling_factor_Si + 0.26 - 0.05*i, c=colors_raman[i], linewidth=2)
        ax_raman_right.plot(wavenumber, intensity/scaling_factor_Si + 0.26 - 0.05*i, c=colors_raman[i], linewidth=2)
    
    ax_raman_left.set_xlim(900,1750)
    ax_raman_right.set_xlim(2300,3150)
    
    ax_raman_left.spines['right'].set_visible(False)
    ax_raman_right.spines['left'].set_visible(False)
    ax_raman_left.yaxis.tick_left()
    ax_raman_left.tick_params(direction='in', labelright='off', length=8)
    ax_raman_right.yaxis.tick_right()
    ax_raman_right.tick_params(direction='in', length=8)
    
    d = .01  # how big to make the diagonal lines in axes coordinates
    # arguments to pass plot, just so we don't keep repeating them
    kwargs = dict(transform=ax_raman_left.transAxes, color='k', clip_on=False)
    ax_raman_left.plot((1-d, 1+d), (-d, +d), **kwargs, linewidth=1)
    ax_raman_left.plot((1-d, 1+d), (1-d, 1+d), **kwargs, linewidth=1)

    kwargs.update(transform=ax_raman_right.transAxes)  # switch to the bottom axes
    ax_raman_right.plot((-d, +d), (1-d, 1+d), **kwargs, linewidth=1)
    ax_raman_right.plot((-d, +d), (-d, +d), **kwargs, linewidth=1)

    ax_raman_right.legend(labels)
    #fig.suptitle('Raman shift (cm$^{-1}$)')
    ax_raman_left.set_ylabel('Intensity (arb. units)')
    #fig.subplots_adjust(wspace=1)
    
    # label Raman peaks
    ax_raman_left.annotate('Si', [940, 0.01], fontsize=20)
    ax_raman_left.annotate('D', [1320, 0.01], fontsize=20)
    ax_raman_left.annotate('G', [1555, 0.01], fontsize=20)
    ax_raman_right.annotate('2D', [2630,0.01], fontsize=20)
    ax_raman_right.annotate('D+D\'', [2850,0.03], fontsize=20)
    
    ax_raman_left.set_ylim(0,0.4)
    ax_raman_left.set_yticks([])
    ax_raman_right.set_ylim(0,0.4)
    ax_raman_right.set_yticks([])
    ax_raman_right.annotate('Raman shift (cm$^{-1}$)', [1950,-0.05], fontsize=20, annotation_clip=False)
    
    
    plt.savefig('thesis/raman.png')


def fnct_fig_temp():
    # Setup subplots
    plt.rcParams.update({'font.size': 18})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[8,7])
    ax_T = fig.add_axes([0.12, 0.12, 0.84, 0.74])
    ax_T_upper = ax_T.twiny()

    cmap = mpl.colormaps['plasma']
    n_lines=35
    colors = cmap(np.linspace(0, 1, n_lines))

    dataset_temperature = datasets.gatesweep_0T_state1()[0]
    for file_temperature in dataset_temperature:
        print(file_temperature)
        R_T = extract_cell4.calc_r(filename=file_temperature, channel=1)/1000
        Vg_V = extract_cell4.read_var(filename=file_temperature, col=5)
        max_index = np.argmax(R_T)
        n_cm_2 = 4*(Vg_V-Vg_V[max_index]) * 0.7254E12 / 50 * 10**-12
        T_K = extract_cell4.read_var(filename=file_temperature, col=4)
        ax_T.scatter(Vg_V, R_T, marker='.', c=T_K, cmap='coolwarm', vmax=200, vmin=0)
    
    # lower axis labels
    ax_T.set_ylabel('$R$ (k$\Omega$)')
    ax_T.set_ylim(bottom=0)
    ax_T.set_xlim(0,79)
    ax_T.set_xlabel('V$_g$(V)')
    ax_T.tick_params(direction='in', length=8)
    
    new_ticks = np.array([-3,-2,-1,0,1])
    ax_T_upper.set_xlim(ax_T.get_xlim())
    ax_T_upper.set_xlabel('$n$ (10$^{12}$cm$^{-2}$)')
    #ax_T_upper.set_xlim(-3.1,1.5)
    print(new_ticks, Vg_V[max_index])
    ax_T_upper.set_xticks(np.array(new_ticks)*50./(4.*0.7254)+Vg_V[max_index])
    print(np.array(new_ticks)*50./(4.*0.7254)+Vg_V[max_index])
    ax_T_upper.set_xticklabels(new_ticks)
    
    ax_T_upper.tick_params(which='both', direction='in', right=True, length=8)

    
    # colorbar settings
    norm = mpl.colors.Normalize(vmin=0, vmax=200) 
    sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm) 
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax_T)
    cbar.ax.invert_yaxis()
    cbar.set_label('$T$(K)')
    
    plt.savefig('thesis/gatesweep_temperature.png')


def fnct_fig_CNP_resistance():
    # Setup subplots
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[10,7])
    
    ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.75])
    ax2 = ax1.twiny()
    
    
    new_data = [datasets.g3_5min(), datasets.g3_25min(), datasets.g3_30min()]

    cmap = mpl.colormaps['plasma']
    n_lines=35
    colors = cmap(np.linspace(0, 1, n_lines))
    for peaks, errorbars_peaks, temperatures,exposure in new_data:
        print(peaks)
        ax1.scatter(np.array(temperatures)**(-1/3), peaks/1000, color = colors[exposure], linewidths=5)
    #ax1.set_yscale('log')
    ax1.set_xlabel(r'$T^{-\frac{1}{3}}(K^{-\frac{1}{3}})$')
    ax1.set_ylabel(r'$R_{peak} (k\Omega)$')
    ax1.set_ylim(bottom=0)
    ax1.tick_params(axis='both', which='both', direction='in', left=True, right=True)

    labels = ['5 min', '25 min', '30 min']
    ax1.legend(labels)
    
    new_ticks = np.array([4.2, 10, 20, 50, 100, 300])
    ax2.set_xlim(ax1.get_xlim())
    ax2.set_xticks(np.array(new_ticks)**(-1/3))
    ax2.set_xticklabels(new_ticks)
    ax2.tick_params(axis='both', which='both', direction='in')
    ax2.set_xlabel('T(K)')
    
    plt.savefig('thesis/resistance_CNP.png')


def fnct_fig_magnetotransport():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[16,7])
    ax_s1 = fig.add_axes([0.05, 0.15, 0.4, 0.75])
    ax_s2 = fig.add_axes([0.5, 0.15, 0.489, 0.75])
    ax_s1.annotate('a', [0.03, 0.91], xycoords='figure fraction', annotation_clip=False, fontweight='bold')
    ax_s2.annotate('b', [0.48, 0.91], xycoords='figure fraction', annotation_clip=False, fontweight='bold')
    
    # Figure state 1
    dataset, labels, temperatures = datasets.gatesweep_30T_state1()
    for file, temperature in zip(dataset, temperatures):
        R1 = extract_cell4.calc_r(filename=file, channel=1)/1000
        Vg_V = extract_cell4.read_var(filename=file, col=5)
        max_index = np.argmax(R1)
        n_cm_2 = 4*(Vg_V-Vg_V[max_index]) * 0.7254E12 / 50 * 10**-12
        T_K = extract_cell4.read_var(filename=file, col=4)
        ax_s1.scatter(n_cm_2, R1, marker='.', c=T_K, cmap='coolwarm', vmax=200, vmin=0)
    
    # lower axis labels
    ax_s1.set_ylabel('$R$ (k$\Omega$)', fontsize=23)
    ax_s1.set_ylim(0,5.5)
    ax_s1.set_xlabel('$n$ (10$^{12}$cm$^{-2}$)', fontsize=23)
    ax_s1.set_xlim(-2.9,1.7)
    ax_s1.set_xticks((-2,-1,0,1,))
    ax_s1.tick_params(which='both', direction='in', right=True, length=8)
    
    # upper axis labels
    ax_s1_lower = ax_s1.twiny()
    new_ticks = np.array([-2, 0, 2])
    ax_s1_lower.set_xlim(ax_s1.get_xlim())
    ax_s1_lower.set_xticks((np.array(new_ticks))*0.7254)
    ax_s1_lower.set_xticklabels(new_ticks)
    ax_s1_lower.set_xlabel(r'$\nu$', fontsize=23)
    ax_s1_lower.tick_params(direction='in', length=8)
    
    # Figure state 1
    dataset, labels, temperatures = datasets.gatesweep_30T_state2()
    for file, temperature in zip(dataset, temperatures):
        R1 = extract_cell4.calc_r(filename=file, channel=1)/1000
        Vg_V = extract_cell4.read_var(filename=file, col=5)
        max_index = np.argmax(R1)
        n_cm_2 = 4*(Vg_V-Vg_V[max_index]) * 0.7254E12 / 50 * 10**-12
        T_K = extract_cell4.read_var(filename=file, col=4)
        ax_s2.scatter(n_cm_2, R1, marker='.', c=T_K, cmap='coolwarm', vmax=200, vmin=0)
    
    # lower axis labels
    ax_s2.set_ylim(0,5.5)
    ax_s2.set_xlabel('$n$ (10$^{12}$cm$^{-2}$)', fontsize=23)
    ax_s2.set_xlim(-5.5,0.1)
    #ax_s2.set_xticks((-3,-2,-1,0,1,))
    ax_s2.tick_params(which='both', direction='in', right=True, length=8)
    
    # upper axis labels
    ax_s2_lower = ax_s2.twiny()
    new_ticks = np.array([-6,-2,0])
    ax_s2_lower.set_xlim(ax_s2.get_xlim())
    ax_s2_lower.set_xticks((np.array(new_ticks))*0.7254)
    ax_s2_lower.set_xticklabels(new_ticks)
    ax_s2_lower.set_xlabel(r'$\nu$', fontsize=23)
    ax_s2_lower.tick_params(direction='in', length=8)

    # colorbar settings
    norm = mpl.colors.Normalize(vmin=4, vmax=200) 
    sm = plt.cm.ScalarMappable(cmap='coolwarm', norm=norm) 
    sm.set_array([])
    cbar = fig.colorbar(sm, ax=ax_s2)
    cbar.set_label('$T$(K)', fontsize=23)
    
    plt.savefig('thesis/magnetotransport.png')
    

def fnct_fig_arrhenius_minima():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[16,7])
    ax_minima_s1 = fig.add_axes([0.08, 0.15, 0.4, 0.7])
    ax_minima_upper_s1 = ax_minima_s1.twiny()
    ax_minima_s2 = fig.add_axes([0.55, 0.15, 0.4, 0.7])
    ax_minima_upper_s2 = ax_minima_s2.twiny()
    ax_minima_s1.annotate('a', [0.05, 0.91], xycoords='figure fraction', annotation_clip=False, fontweight='bold')
    ax_minima_s2.annotate('b', [0.52, 0.91], xycoords='figure fraction', annotation_clip=False, fontweight='bold')
    
    # Plot state 1
    cont_temps = np.linspace(start=4, stop=300, num=100)
    channel = 1
    data_s1 = [datasets.gatesweep_20T_state1(), datasets.gatesweep_25T_state1(), datasets.gatesweep_30T_state1()]
    left_lim_s1, right_lim_s1, start_index_s1, stop_index_s1 = datasets.activation_params_s1_min2()
    labels = ['20T', '25T', '30T']
    fields = [20,25,30]
    handles_s1 = []
    
    for j, (dataset, label, temperatures) in enumerate(data_s1):
        valleys = np.zeros(shape=(len(dataset)))
        for i, file in enumerate(dataset):
            valleys[i] = extract_cell4.find_valley(file, channel, left_lim_s1, right_lim_s1)
        fitparams, sigma = find_activation(dataset, channel, temperatures, left_lim_s1, right_lim_s1, start_index_s1[j], stop_index_s1[j])
        print(fitparams,sigma)
        color = mpl.colormaps['plasma_r']((fields[j]-17)/(max(fields)-17))
        legend_point = mpl.lines.Line2D([0], [0], marker='o', markersize=10, color=color, linestyle='')
        handles_s1.extend([legend_point])
        
        fit_results = np.exp(fitparams[0]/cont_temps + fitparams[1])
        upper_fit = np.exp((fitparams[0]+sigma[0])/cont_temps + fitparams[1]+sigma[1])
        lower_fit = np.exp((fitparams[0]-sigma[0])/cont_temps + fitparams[1]-sigma[1])
        ax_minima_s1.plot(1/cont_temps, fit_results/1000, color=color, linewidth=1, linestyle='dashed', label='_nolegend_')
        for i in range(len(valleys)):
            if i>=start_index_s1[j] and i<=(stop_index_s1[j] % len(valleys)):
                ax_minima_s1.scatter(1/np.array(temperatures[i]), valleys[i]/1000, color=color, facecolors=color, s=75)
            else:
                ax_minima_s1.scatter(1/np.array(temperatures[i]), valleys[i]/1000, color=color, facecolors='none', s=75)
        ax_minima_s1.fill_between(1/cont_temps, upper_fit/1000, lower_fit/1000, color=color, alpha=0.2, label='_nolegend_')
    
    ax_minima_s1.set_yscale('log')
    ax_minima_s1.set_xlim(left=0.003, right=0.26)
    ax_minima_s1.set_ylim(bottom=0.05, top=4)
    ax_minima_s1.set_xlabel(r'1/$T$(1/K)', fontsize=23)
    ax_minima_s1.set_ylabel(r'$R$(k$\Omega)$', fontsize=23)
    ax_minima_s1.tick_params(axis='both', which='both', direction='in', left=True, right=True, length=8)
    
    new_ticks = np.array([4, 10, 20, 150])
    ax_minima_upper_s1.set_xlim(ax_minima_s1.get_xlim())
    ax_minima_upper_s1.set_xticks(1/new_ticks)
    ax_minima_upper_s1.set_xticklabels(new_ticks)
    ax_minima_upper_s1.set_xlabel('$T$(K)', fontsize=23)
    ax_minima_upper_s1.tick_params(direction='in', length=8)
    
    ax_minima_s1.legend(labels=labels, handles=handles_s1, fontsize=23, loc='lower left', handlelength=0.5)
    
    
    # Plot state 2
    data_s2 = [datasets.gatesweep_20T_state2(), datasets.gatesweep_25T_state2(), datasets.gatesweep_30T_state2()]
    left_lim_s2, right_lim_s2, start_index_s2, stop_index_s2 = datasets.activation_params_s2_min2()
    handles_s2 = []
    
    for j, (dataset, label, temperatures) in enumerate(data_s2):
        valleys = np.zeros(shape=(len(dataset)))
        for i, file in enumerate(dataset):
            valleys[i] = extract_cell4.find_valley(file, channel, left_lim_s2, right_lim_s2)
        fitparams, sigma = find_activation(dataset, channel, temperatures, left_lim_s2, right_lim_s2, start_index_s2[j], stop_index_s2[j])
        print(fitparams,sigma)
        color = mpl.colormaps['plasma_r']((fields[j]-17)/(max(fields)-17))
        legend_point = mpl.lines.Line2D([0], [0], marker='o', markersize=10, color=color, linestyle='')
        handles_s2.extend([legend_point])
        
        fit_results = np.exp(fitparams[0]/cont_temps + fitparams[1])
        upper_fit = np.exp((fitparams[0]+sigma[0])/cont_temps + fitparams[1]+sigma[1])
        lower_fit = np.exp((fitparams[0]-sigma[0])/cont_temps + fitparams[1]-sigma[1])
        ax_minima_s2.plot(1/cont_temps, fit_results/1000, color=color, linewidth=1, linestyle='dashed', label='_nolegend_')
        for i in range(len(valleys)):
            if i>=start_index_s2[j] and i<=(stop_index_s2[j] % len(valleys)):
                ax_minima_s2.scatter(1/np.array(temperatures[i]), valleys[i]/1000, color=color, facecolors=color, s=75)
            else:
                ax_minima_s2.scatter(1/np.array(temperatures[i]), valleys[i]/1000, color=color, facecolors='none', s=75)
        ax_minima_s2.fill_between(1/cont_temps, upper_fit/1000, lower_fit/1000, color=color, alpha=0.2, label='_nolegend_')
    
    ax_minima_s2.set_yscale('log')
    ax_minima_s2.set_xlim(left=0.003, right=0.26)
    ax_minima_s2.set_ylim(bottom=0.05, top=4)
    ax_minima_s2.set_xlabel(r'1/$T$(1/K)', fontsize=23)
    ax_minima_s2.tick_params(axis='both', which='both', direction='in', left=True, right=True, length=8)
    
    new_ticks = np.array([4, 10, 20, 150])
    ax_minima_upper_s2.set_xlim(ax_minima_s2.get_xlim())
    ax_minima_upper_s2.set_xticks(1/new_ticks)
    ax_minima_upper_s2.set_xticklabels(new_ticks)
    ax_minima_upper_s2.set_xlabel('$T$(K)', fontsize=23)
    ax_minima_upper_s2.tick_params(direction='in', length=8)
    
    #ax_minima_s2.legend(labels=labels, handles=handles_s1, fontsize=23, loc='lower left', handlelength=0.5)
    
    plt.savefig('thesis/arrhenius_minima.png')


def fnct_fig_activation_summary():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 20})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[8,7])
    ax_ll = fig.add_axes([0.15, 0.15, 0.7, 0.8])
    fields = np.array([0,20,25,30])
    data = [datasets.activation_results_s1_min2(), datasets.activation_results_s1_plus2(), 
            datasets.activation_results_s2_min2(), datasets.activation_results_s2_min6(),] 
            #datasets.activation_results_s3_min2(), datasets.activation_results_s3_min6()]
    
    reference_data = [datasets.activation_reference_plus2(), datasets.activation_reference_plus6()]

    for i, (delta, error, label, marker) in enumerate(data):
        color = mpl.colormaps['plasma_r']((fields[math.ceil((i+1)/2)]-17)/(max(fields)-17))
        linear_check, linear_error = fit_cell4.linear_fit(fields[1::], delta[1::]*2, error[1::]*2)
        fit_results = fit_cell4.lin(fields, linear_check[0], linear_check[1])
        ax_ll.errorbar(fields[1::], delta[1::]*2, error[1::]*2, label=label, elinewidth=1, capsize=5, linestyle='', marker=marker, markersize=15, color=color)
        ax_ll.plot(fields, fit_results, color=color, linestyle='dashed', linewidth=1)    
    
    ax_ll.set_ylim(0,85)
    ax_ll.set_xlim(14,30.5)
    ax_ll.set_xlabel('$B$(T)', fontsize=23)
    ax_ll.set_ylabel(r'$\Delta_{LL} - \Gamma$ (K)', fontsize=23)
    ax_ll.tick_params(axis='both', which='both', direction='in', left=True, right=True, top=True, length=8)
    #ax_ll.set_title('Summary activation energy', fontsize=23)
    #ax_ll.set_yscale('log', fontsize=23)
    ax_ll.legend(fontsize=23)
    
    plt.savefig('thesis/activation_summary.png')


def fnct_fig_simulations():
    # Define figure and subplots
    plt.rcParams.update({'font.size': 18})
    plt.rcParams.update({'lines.linewidth': 5})
    fig = plt.figure(figsize=[7,5])
    
    ax_summary= fig.add_axes([0.15,0.15,0.75,0.8])
    
    carbons, mass_eff, bandgap = datasets.mass_eff_summary()
    ax_summary_gap = ax_summary.twinx()
    ax_summary.scatter(carbons, mass_eff, color='black', alpha=0.5)
    ax_summary.set_xscale('log')
    ax_summary.set_xlabel('H Coverage')
    ax_summary.set_ylabel('$m^*_{\mathrm{e}}$/m$_{\mathrm{0}}$')
    ax_summary.set_xticklabels([f'{x:.0f}%' for x in ax_summary.get_xticks()])
    ax_summary.tick_params(axis='both', which='both', direction='in', length=8)
    ax_summary_gap.scatter(carbons, bandgap, color='red', marker='^', alpha=0.5)
    ax_summary_gap.set_ylabel('$E_{\mathrm{gap}}$ (eV)', color='red')
    ax_summary_gap.tick_params(direction='in')
    ax_summary_gap.spines['right'].set_color('red')
    ax_summary_gap.tick_params(axis='y', colors='red', length=8)
    ax_summary.annotate("", [0.1, 0.52],[0.60, 0.52], xycoords='axes fraction', arrowprops=dict(arrowstyle='->'), annotation_clip=False,)
    ax_summary.annotate("", [0.95, 0.27],[0.75, 0.27], xycoords='axes fraction', arrowprops=dict(arrowstyle='->', color='red'), annotation_clip=False,)
    
    plt.savefig('thesis/coverage_vs_bandgap.png')





# %% Execute code
fnct_fig_temp()