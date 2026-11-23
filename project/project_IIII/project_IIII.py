#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 12:29:20 2025

@author: Home
"""
#%%
#A combined-spectrum version of this data is used: https://www.ncei.noaa.gov/data/poes-metop-space-environment-monitor/access/l1a/v01r00/2023/noaa15/

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import glob
import pandas as pd
from scipy import stats


np.set_printoptions(threshold=sys.maxsize)
ifiles00 = sorted(glob.glob(os.path.expanduser("~/Documents/POES_Data_S3/POES_combinedSpectrum_m02_00_*.nc")))
ifiles90 = sorted(glob.glob(os.path.expanduser("~/Documents/POES_Data_S3/POES_combinedSpectrum_m02_90_*.nc")))

n = np.arange(1, len(ifiles00)+1)
meanlist00_E1 = []
meanlist00_E2 = []
meanlist00_E3 = []
meanlist00_E4 = []

meanlist90_E1 = []
meanlist90_E2 = []
meanlist90_E3 = []
meanlist90_E4 = []

#================= Compute daily average of Dst =================

df = pd.read_excel(os.path.expanduser("~/Downloads/Dst_General_magnetic_index.xlsx"), names=["Timestamp", "Value"])

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Day"] = df["Timestamp"].dt.date
df["Time"] = df["Timestamp"].dt.time


daily_list = []
daily_means = {}
daily_arrays = {}
for date, group in df.groupby('Day'):
    daily_list.append(group[['Time', 'Value']].to_numpy())
    daily_means[date] = group['Value'].mean()
    
    
    # plt.scatter(daily_arrays[str(date)],s=4)

     
    # plt.title(f'dst {str(date)}')
    # plt.minorticks_on()
    # plt.grid(which='major',linestyle='-',alpha=0.8)
    # plt.grid(which='minor',linestyle='--',alpha=0.5)
    # plt.xlabel('Time')
    # plt.ylabel('Value')
    # plt.legend(loc="upper right", ncols=2)
    # # plt.savefig("project_IIIh.png")
    # plt.show()

dst_means = np.array(list(daily_means.values()))

print(dst_means)

for itime in range(0, len(ifiles00)):

#======================================EOCounts==================================
    
    file2read00 = netCDF4.Dataset(ifiles00[itime],'r')
    lshell00 = np.array(file2read00.variables['lValue'])
    time00 = np.array(file2read00.variables['rtime'])
    EOcounts_corrected00 = np.array(file2read00.variables['EOcounts_corrected'])
    
    file2read90 = netCDF4.Dataset(ifiles90[itime],'r')
    lshell90 = np.array(file2read90.variables['lValue'])
    time90 = np.array(file2read90.variables['rtime'])    
    EOcounts_corrected90 = np.array(file2read90.variables['EOcounts_corrected'])

#=======================================LShells==================================
    
    lshell_index00, lshell_index90 = np.where(lshell00>5), np.where
    lshell_index00 = np.array(lshell_index00)
    
    lshell_index90 = np.where(lshell90>5)
    lshell_index90 = np.array(lshell_index90)
    time00_s = (time00)*3600
    time90_s = (time90)*3600    


#==============================EOcount Void Data Sort============================

    
    how_many_less_than1 = np.where(EOcounts_corrected00[:,0]/EOcounts_corrected90[:,0] > 2)
    how_many_less_than2 = np.where(EOcounts_corrected00[:,1]/EOcounts_corrected90[:,1] > 2)
    how_many_less_than3 = np.where(EOcounts_corrected00[:,2]/EOcounts_corrected90[:,2] > 2)
    how_many_less_than4 = np.where(EOcounts_corrected00[:,3]/EOcounts_corrected90[:,3] > 2)
   
    hmlt1 = np.array(how_many_less_than1)
    hmlt2 = np.array(how_many_less_than2)
    hmlt3 = np.array(how_many_less_than3)
    hmlt4 = np.array(how_many_less_than4)
    
    newtime1 = time00_s[hmlt1]
    newtime2 = time00_s[hmlt2]
    

    EOcounts1_filtered00 = EOcounts_corrected00[hmlt1[:],0]
    EOcounts2_filtered00 = EOcounts_corrected00[hmlt2[:],1]
    EOcounts3_filtered00 = EOcounts_corrected00[hmlt3[:],2]
    EOcounts4_filtered00 = EOcounts_corrected00[hmlt4[:],3]


    EOcounts1_filtered90 = EOcounts_corrected90[hmlt1[:],0]
    EOcounts2_filtered90 = EOcounts_corrected90[hmlt2[:],1]
    EOcounts3_filtered90 = EOcounts_corrected90[hmlt3[:],2]
    EOcounts4_filtered90 = EOcounts_corrected90[hmlt4[:],3]
    
    
    #STATISTICS
    
#Channel 1:
    mean00_1 = EOcounts1_filtered00.mean()
    meanlist00_E1.append(mean00_1)
    
    mean90_1 = EOcounts1_filtered90.mean()
    meanlist90_E1.append(mean90_1)

#Channel 2:
    mean00_2 = EOcounts2_filtered00.mean()
    meanlist00_E2.append(mean00_2)

    mean90_2 = EOcounts2_filtered90.mean()
    meanlist90_E2.append(mean90_2)

#Channel 3:
    mean00_3 = EOcounts3_filtered00.mean()
    meanlist00_E3.append(mean00_3)
    
    mean90_3 = EOcounts3_filtered90.mean()
    meanlist90_E3.append(mean90_3)


    
#Channel 4:
    mean00_4 = EOcounts4_filtered00.mean()
    meanlist00_E4.append(mean00_4)

    mean90_4 = EOcounts4_filtered90.mean()
    meanlist90_E4.append(mean90_4)

    #PLOTS

meanlist00_E1 = np.asarray(meanlist00_E1, dtype=float)
meanlist00_E2 = np.asarray(meanlist00_E2, dtype=float)

#Figure out what EOcounts is
#List the energy ranges for E1 through E4

# E1 Channel: E > 30keV (nominal range around 30 to 2,500 keV)
# E2 Channel: E > 100keV (nominal range around 100 to 2,500 keV)
# E3 Channel: E > 300keV (nominal range around 300 to 2,500 keV)
# E4 Channel (P6 Channel): E > ~700keV


#Compute correlation coefficient between energy channels, hypothesis test that the coeficcinet is not 0, compute error bar on coeficcient by thursday
#find some literature where they have looked at the correlations (exploratory analysis)
# - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2022JA030489
# - https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2023JA031641

#Compute daily average of Dst.
# for plots: add p value, r, and confidence interval


plt.scatter(n,meanlist00_E1,s=4,label = "E1")
plt.scatter(n,meanlist00_E2,s=4,label = "E2")
plt.scatter(n,meanlist00_E3,s=4,label = "E3")
plt.scatter(n,meanlist00_E4,s=4,label = "E4")
plt.plot(n, dst_means, lw = 1, c = 'k', label = "DST Means")
 
plt.title('$0°$ Electron Precipitation Means over Time')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Mean EOCounts')
plt.xlim(0.7, None) 
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIIa.png")
plt.show()


#Add DST to these plots    


plt.scatter(n,meanlist90_E1,s=4,label = "E1")
plt.scatter(n,meanlist90_E2,s=4,label = "E2")
plt.scatter(n,meanlist90_E3,s=4,label = "E3")
plt.scatter(n,meanlist90_E4,s=4,label = "E4")
plt.plot(n, dst_means, lw = 1, c = 'k', label = "DST Means")

plt.title('$90°$ Electron Precipitation Means over Time')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Time')
plt.ylabel('Mean EOCounts')
plt.xlim(0.7, None) 
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIIb.png")
plt.show()

alpha = 0.05

fig, axs = plt.subplots(2, 2, figsize=(12, 10))

plots = [
    (axs[0, 0], meanlist00_E1, meanlist00_E2, r'$0^\circ$: Channel 1 Means vs Channel 2 Means', 'Channel 1', 'Channel 2'),
    (axs[1, 0], meanlist90_E1, meanlist90_E2, r'$90^\circ$: Channel 1 Means vs Channel 2 Means', 'Channel 1', 'Channel 2'),
    (axs[0, 1], meanlist00_E3, meanlist00_E4, r'$0^\circ$: Channel 3 Means vs Channel 4 Means', 'Channel 3', 'Channel 4'),
    (axs[1, 1], meanlist90_E3, meanlist90_E4, r'$90^\circ$: Channel 3 Means vs Channel 4 Means', 'Channel 3', 'Channel 4')
]

for ax, x_raw, y_raw, title, xlabel, ylabel in plots:
    # 1. Ensure inputs are 1D float NumPy arrays
    x = np.asarray(x_raw, dtype=float)
    y = np.asarray(y_raw, dtype=float)

    res = stats.pearsonr(x, y)
    r_val = res.statistic
    p_val = res.pvalue
    ci_low, ci_high = res.confidence_interval(confidence_level=0.95)

    # 3. Calculate linear fit and 95% confidence band
    slope, intercept = np.polyfit(x, y, 1)
    x_line = np.linspace(np.min(x), np.max(x), 100)
    y_line = slope * x_line + intercept

    n = len(x)
    dof = n - 2
    t_crit = stats.t.ppf(0.975, dof)
    residuals = y - (slope * x + intercept)
    s_err = np.sqrt(np.sum(residuals**2) / dof)
    ci_band = t_crit * s_err * np.sqrt(
        1/n + (x_line - np.mean(x))**2 / np.sum((x - np.mean(x))**2)
    )

    # 4. Plot data, trendline, and confidence band on the current subplot (ax)
    ax.scatter(x, y, s=5, label='Data')
    ax.plot(x_line, y_line, color='b', linewidth=1.5, label='Linear Fit')
    ax.fill_between(
        x_line,
        y_line - ci_band,
        y_line + ci_band,
        color='g',
        alpha=0.2,
        label='95% CI'
    )

    # 5. Add stats annotation box
    stats_text = (
        f"r value = ${r_val:.3f}$\n"
        f"95% CI: $[{ci_low:.3f}, {ci_high:.3f}]$\n"
        f"$P-value = {p_val:.2e}$"
    )
    ax.text(
        0.05, 0.95, stats_text,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='gray')
    )

    # 6. Keep your existing formatting
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', alpha=0.8)
    ax.grid(which='minor', linestyle='--', alpha=0.5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='lower right', fontsize=8)

fig.suptitle(r"$0^\circ$ and $90^\circ$ Channel Mean Correlation", fontsize=16)
plt.tight_layout()
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(12, 10))

plots = [
    (axs[0, 0], meanlist00_E1, dst_means, r'$0^\circ$ Channel 1 Means vs DST Means', 'Channel 1', 'DST'),
    (axs[1, 0], meanlist00_E2, dst_means, r'$0^\circ$ Channel 2 Means vs DST Means', 'Channel 2', 'DST'),
    (axs[0, 1], meanlist00_E3, dst_means, r'$0^\circ$ Channel 3 Means vs DST Means', 'Channel 3', 'DST'),
    (axs[1, 1], meanlist00_E4, dst_means, r'$0^\circ$ Channel 4 Means vs DST Means', 'Channel 2', 'DST'),
]

for ax, x_raw, y_raw, title, xlabel, ylabel in plots:
    x = np.asarray(x_raw, dtype=float)
    y = np.asarray(y_raw, dtype=float)

    res = stats.pearsonr(x, y)
    r_val = res.statistic
    p_val = res.pvalue
    ci_low, ci_high = res.confidence_interval(confidence_level=0.95)

    # 3. Calculate linear fit and 95% confidence band
    slope, intercept = np.polyfit(x, y, 1)
    x_line = np.linspace(np.min(x), np.max(x), 100)
    y_line = slope * x_line + intercept

    n = len(x)
    dof = n - 2
    t_crit = stats.t.ppf(0.975, dof)
    residuals = y - (slope * x + intercept)
    s_err = np.sqrt(np.sum(residuals**2) / dof)
    ci_band = t_crit * s_err * np.sqrt(
        1/n + (x_line - np.mean(x))**2 / np.sum((x - np.mean(x))**2)
    )

    # 4. Plot data, trendline, and confidence band on the current subplot (ax)
    ax.scatter(x, y, s=5, label='Data')
    ax.plot(x_line, y_line, color='b', linewidth=1.5, label='Linear Fit')
    ax.fill_between(
        x_line,
        y_line - ci_band,
        y_line + ci_band,
        color='g',
        alpha=0.2,
        label='95% CI'
    )

    # 5. Add stats annotation box
    stats_text = (
        f"r value = ${r_val:.3f}$\n"
        f"95% CI: $[{ci_low:.3f}, {ci_high:.3f}]$\n"
        f"$P-value = {p_val:.2e}$"
    )
    ax.text(
        0.05, 0.95, stats_text,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='gray')
    )

    # 6. Keep your existing formatting
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', alpha=0.8)
    ax.grid(which='minor', linestyle='--', alpha=0.5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='lower right', fontsize=8)

fig.suptitle(r"$0^\circ$ Channel Mean vs DST Mean Correlation", fontsize=16)
plt.tight_layout()
plt.savefig("project_IIIIc.png")
plt.show()


fig, axs = plt.subplots(2, 2, figsize=(12, 10))

plots = [
    (axs[0, 0], meanlist90_E1, dst_means, r'$90^\circ$ Channel 1 Means vs DST Means', 'Channel 1', 'DST'),
    (axs[1, 0], meanlist90_E2, dst_means, r'$90^\circ$ Channel 2 Means vs DST Means', 'Channel 2', 'DST'),
    (axs[0, 1], meanlist90_E3, dst_means, r'$90^\circ$ Channel 3 Means vs DST Means', 'Channel 3', 'DST'),
    (axs[1, 1], meanlist90_E4, dst_means, r'$90^\circ$ Channel 4 Means vs DST Means', 'Channel 4', 'DST'),
]

for ax, x_raw, y_raw, title, xlabel, ylabel in plots:
    x = np.asarray(x_raw, dtype=float)
    y = np.asarray(y_raw, dtype=float)

    res = stats.pearsonr(x, y)
    r_val = res.statistic
    p_val = res.pvalue
    ci_low, ci_high = res.confidence_interval(confidence_level=0.95)

    # 3. Calculate linear fit and 95% confidence band
    slope, intercept = np.polyfit(x, y, 1)
    x_line = np.linspace(np.min(x), np.max(x), 100)
    y_line = slope * x_line + intercept

    n = len(x)
    dof = n - 2
    t_crit = stats.t.ppf(0.975, dof)
    residuals = y - (slope * x + intercept)
    s_err = np.sqrt(np.sum(residuals**2) / dof)
    ci_band = t_crit * s_err * np.sqrt(
        1/n + (x_line - np.mean(x))**2 / np.sum((x - np.mean(x))**2)
    )

    # 4. Plot data, trendline, and confidence band on the current subplot (ax)
    ax.scatter(x, y, s=5, label='Data')
    ax.plot(x_line, y_line, color='b', linewidth=1.5, label='Linear Fit')
    ax.fill_between(
        x_line,
        y_line - ci_band,
        y_line + ci_band,
        color='g',
        alpha=0.2,
        label='95% CI'
    )

    # 5. Add stats annotation box
    stats_text = (
        f"r value = ${r_val:.3f}$\n"
        f"95% CI: $[{ci_low:.3f}, {ci_high:.3f}]$\n"
        f"$P-value = {p_val:.2e}$"
    )
    ax.text(
        0.05, 0.95, stats_text,
        transform=ax.transAxes,
        fontsize=9,
        verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.85, edgecolor='gray')
    )

    # 6. Keep your existing formatting
    ax.set_title(title)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', alpha=0.8)
    ax.grid(which='minor', linestyle='--', alpha=0.5)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend(loc='lower right', fontsize=8)

fig.suptitle(r"$90^\circ$ Channel Mean vs DST Mean Correlation", fontsize=16)
plt.tight_layout()
plt.savefig("project_IIIId.png")
plt.show()


