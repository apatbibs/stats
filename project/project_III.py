#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 14 12:29:20 2025

@author: Home
"""

#A combined-spectrum version of this data is used: https://www.ncei.noaa.gov/data/poes-metop-space-environment-monitor/access/l1a/v01r00/2023/noaa15/

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import netCDF4
import glob
import pandas as pd
from scipy import stats

#Interested in using this data and I need to find a question that I can ask for which statistics and hypothesis tests can be derived.

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

# 3. Extract separate columns/arrays for Day and Time
df["Day"] = df["Timestamp"].dt.date
df["Time"] = df["Timestamp"].dt.time
daily_means = {}
daily_arrays = {}
for date, group in df.groupby('Day'):
    # Extract only the 'Time' and 'Value' (Column B) columns as a NumPy array
    daily_arrays[str(date)] = group[['Time', 'Value']].to_numpy()
    daily_means[date] = group['Value'].mean()

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

    # print(mean00_1)
    # print(mean90_1)
    # print()
    
    #Channel 2:
    mean00_2 = EOcounts2_filtered00.mean()
    meanlist00_E2.append(mean00_2)

    mean90_2 = EOcounts2_filtered90.mean()
    meanlist90_E2.append(mean90_2)

    # print(mean00_2)
    # print(mean90_2)
    # print()
    
    #Channel 3:
    mean00_3 = EOcounts3_filtered00.mean()
    meanlist00_E3.append(mean00_3)
    
    mean90_3 = EOcounts3_filtered90.mean()
    meanlist90_E3.append(mean90_3)

    # print(mean00_1)
    # print(mean90_1)
    # print()
    
    #Channel 4:
    mean00_4 = EOcounts4_filtered00.mean()
    meanlist00_E4.append(mean00_4)

    mean90_4 = EOcounts4_filtered90.mean()
    meanlist90_E4.append(mean90_4)

    # print(mean00_4)
    # print(mean90_4)

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




plt.scatter(n,meanlist00_E1,s=4,label = "E1")
plt.scatter(n,meanlist00_E2,s=4,label = "E2")
plt.scatter(n,meanlist00_E3,s=4,label = "E3")
plt.scatter(n,meanlist00_E4,s=4,label = "E4")
 
plt.title('$0°$ Electron Precipitation Means over Time')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Mean EOCounts')
plt.xlim(0.7, None) 
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIa.png")
plt.show()
    

plt.scatter(n,meanlist90_E1,s=4,label = "E1")
plt.scatter(n,meanlist90_E2,s=4,label = "E2")
plt.scatter(n,meanlist90_E3,s=4,label = "E3")
plt.scatter(n,meanlist90_E4,s=4,label = "E4")
 
plt.title('$90°$ Electron Precipitation Means over Time')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Mean EOCounts')
plt.xlim(0.7, None) 
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIb.png")
plt.show()

alpha = 0.05


Ch_1_2_00_result = stats.pearsonr(meanlist00_E1, meanlist00_E2)
r_1_2_00 = Ch_1_2_00_result.statistic
p_value_1_2_00 = Ch_1_2_00_result.pvalue


# Hypothesis test:
is_significant = p_value_1_2_00 < alpha

# 95% CI (error bar)
ci = Ch_1_2_00_result.confidence_interval(confidence_level=0.95)
err_low = r_1_2_00 - ci.low
err_high = ci.high - r_1_2_00
print()
print(f"Correlation Coefficient for Channels 1 & 2 on the 0 degree detector: {r_1_2_00:.6f} (+{err_high:.6f}/-{err_low:.6f})")
print(f"95% CI: [{ci.low:.4f}, {ci.high:.4f}]")
print(f"P-value: {p_value_1_2_00:.4e} (Significant at alpha=0.05?: {is_significant})")
print()

Ch_1_2_90_result = stats.pearsonr(meanlist90_E1, meanlist90_E2)
r_1_2_90 = Ch_1_2_90_result.statistic
p_value_1_2_90 = Ch_1_2_90_result.pvalue


# Hypothesis test:
is_significant = p_value_1_2_90 < alpha

# 95% CI (error bar)
ci_1_2_90 = Ch_1_2_90_result.confidence_interval(confidence_level=0.95)
err_low_1_2_90 = r_1_2_90 - ci_1_2_90.low
err_high_1_2_90 = ci_1_2_90.high - r_1_2_90

print(f"Correlation Coefficient for Channels 1 & 2 on the 90 degree detector: (r): {r_1_2_90:.6f} (+{err_high_1_2_90:.6f}/-{err_low_1_2_90:.6f})")
print(f"95% CI: [{ci_1_2_90.low:.4f}, {ci_1_2_90.high:.4f}]")
print(f"P-value: {p_value_1_2_90:.4e} (Significant at alpha=0.05?: {is_significant})")
print()


Ch_3_4_00_result = stats.pearsonr(meanlist00_E3, meanlist00_E4)
r_3_4_00 = Ch_3_4_00_result.statistic
p_value_3_4_00 = Ch_3_4_00_result.pvalue


# Hypothesis test:
is_significant = p_value_3_4_00 < alpha

# 95% CI (error bar)
ci_3_4_00 = Ch_3_4_00_result.confidence_interval(confidence_level=0.95)
err_low_3_4_00 = r_3_4_00 - ci_3_4_00.low
err_high_3_4_00 = ci_3_4_00.high - r_3_4_00

print(f"Correlation Coefficient for Channels 3 & 4 on the 0 degree detector: : {r_3_4_00:.6f} (+{err_high_3_4_00:.6f}/-{err_low_3_4_00:.6f})")
print(f"95% CI: [{ci_3_4_00.low:.4f}, {ci_3_4_00.high:.4f}]")
print(f"P-value: {p_value_3_4_00:.4e} (Significant at alpha=0.05?: {is_significant})")
print()


Ch_3_4_90_result = stats.pearsonr(meanlist90_E3, meanlist90_E4)
r_3_4_90 = Ch_3_4_90_result.statistic
p_value_3_4_90 = Ch_3_4_90_result.pvalue


# Hypothesis test:
is_significant = p_value_3_4_90 < alpha

# 95% CI (error bar)
ci_3_4_90 = Ch_3_4_90_result.confidence_interval(confidence_level=0.95)
err_low_3_4_90 = r_3_4_90 - ci_3_4_90.low
err_high_3_4_90 = ci_3_4_90.high - r_3_4_90

print(f"Correlation Coefficient for Channels 3 & 4 on the 90 degree detector: {r_3_4_90:.6f} (+{err_high_3_4_90:.6f}/-{err_low_3_4_90:.6f})")
print(f"95% CI: [{ci_3_4_90.low:.4f}, {ci_3_4_90.high:.4f}]")
print(f"P-value: {p_value_3_4_90:.4e} (Significant at alpha=0.05?: {is_significant})")
print()



plt.scatter(meanlist00_E1,meanlist00_E2,s=4)
 
plt.title('$0°$: Channel 1 Means vs Channel 2 Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
# plt.xlim(0.7, None) 
# plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIc.png")
plt.show()
    




plt.scatter(meanlist90_E1,meanlist90_E2,s=4)
 
plt.title('$90°$: Channel 1 Means vs Channel 2 Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
# plt.xlim(0.7, None) 
# plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIId.png")
plt.show()




plt.scatter(meanlist00_E3,meanlist00_E4,s=4)
 
plt.title('$0°$: Channel 3 Means vs Channel 4 Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
plt.savefig("project_IIIe.png")
plt.show()
    



plt.scatter(meanlist90_E3,meanlist90_E4,s=4)
 
plt.title('$90°$: Channel 3 Means vs Channel 4 Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Channel 1')
plt.ylabel('Channel 2')
plt.savefig("project_IIIf.png")
plt.show()


plt.scatter(dst_means,meanlist00_E1,s=4,label = "E1")
plt.scatter(dst_means,meanlist00_E2,s=4,label = "E2")
plt.scatter(dst_means,meanlist00_E3,s=4,label = "E3")
plt.scatter(dst_means,meanlist00_E4,s=4,label = "E4")
 
plt.title('$0°$ Electron Precipitation Means over DST Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Mean EOCounts')
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIg.png")
plt.show()
    

plt.scatter(dst_means,meanlist90_E1,s=4,label = "E1")
plt.scatter(dst_means,meanlist90_E2,s=4,label = "E2")
plt.scatter(dst_means,meanlist90_E3,s=4,label = "E3")
plt.scatter(dst_means,meanlist90_E4,s=4,label = "E4")
 
plt.title('$90°$ Electron Precipitation Means over DST Means')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Day')
plt.ylabel('Mean EOCounts')
plt.legend(loc="upper right", ncols=2)
plt.savefig("project_IIIh.png")
plt.show()

