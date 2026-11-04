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

#==================================LShell Index Sort=============================

    # new_lshell00 = lshell00[lshell_index00]
    # new_lshell90 = lshell90[lshell_index90]

    # new_time_array00 = time00_s[lshell_index00]
    # new_time_array90 = time90_s[lshell_index90]
    
    # mintime = (time00*60)

    # new_EOcounts_array00 = (EOcounts_corrected00[lshell_index00])
    # new_EOcounts_array90 = (EOcounts_corrected90[lshell_index90])
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
    
    # lshell1_filtered00 = new_lshell00[0,hmlt1[:]]
    # lshell2_filtered00 = new_lshell00[0,hmlt2[:]]
    # lshell3_filtered00 = new_lshell00[0,hmlt3[:]]
    # lshell4_filtered00 = new_lshell00[0,hmlt4[:]]

    # lshell1_filtered90 = new_lshell90[0,hmlt1[:]]
    # lshell2_filtered90 = new_lshell90[0,hmlt2[:]]
    # lshell3_filtered90 = new_lshell90[0,hmlt3[:]]
    # lshell4_filtered90 = new_lshell90[0,hmlt4[:]]
    
#+++++++++++++++++++++++++++TEST. DISREGARD+++++++++++++++++++++++++++++++++++++++++
    # mask = (new_EOcounts_array00[0, :, :4] / new_EOcounts_array90[0, :, :4]) > 2
    
    # # 2. Extract arrays of indices for each channel (equivalent to hmlt1, hmlt2, ...)
    # # Since each channel has a different number of passing elements, we can store them in a list
    # hmlt_list = [np.where(mask[:, i])[0] for i in range(4)]
    
    # # 3. Filter arrays cleanly using list comprehensions
    # EOcounts_filtered00 = np.array([new_EOcounts_array00[0, :, i] for i in range(4)]).T
    # EOcounts_filtered90 = np.array([new_EOcounts_array90[0, :, i] for i in range(4)]).T
    


#=======================================Plots====================================
    # plt.scatter(new_lshell00,new_EOcounts_array00[0,:,0],s=2,label = "E1 - $00°$")
    # plt.scatter(new_lshell00,new_EOcounts_array00[0,:,1],s=2,label = "E2 - $00°$")
    # plt.scatter(new_lshell00,new_EOcounts_array00[0,:,2],s=2,label = "E3 - $00°$")
    # plt.scatter(new_lshell00,new_EOcounts_array00[0,:,3],s=2,label = "E4 - $00°$")
     
    # plt.title('EOcounts vs Lshell (Corrected)')
    # plt.minorticks_on()
    # plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
    # plt.grid(which='minor',linestyle='--',alpha=0.5)
    # plt.xlabel('LShell')
    # plt.ylabel('EOCounts')
    # plt.legend()
    # plt.savefig("project_Ia.png")
    # plt.show()
    
     
    # plt.scatter(new_lshell90,new_EOcounts_array90[0,:,0],s=2,label = "E1 - $90°$")
    # plt.scatter(new_lshell90,new_EOcounts_array90[0,:,1],s=2,label = "E2 - $90°$")
    # plt.scatter(new_lshell90,new_EOcounts_array90[0,:,2],s=2,label = "E3 - $90°$")
    # plt.scatter(new_lshell90,new_EOcounts_array90[0,:,3],s=2,label = "E4 - $90°$")
     
    # plt.title('EOcounts vs Lshell (Corrected)')
    # plt.minorticks_on()
    # plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
    # plt.grid(which='minor',linestyle='--',alpha=0.5)
    # plt.xlabel('LShell')
    # plt.ylabel('EOCounts')
    # plt.legend()
    # plt.savefig("project_Ib.png")
    # plt.show()


    #  #==================================Filteredplots================================
     
    # plt.scatter(lshell1_filtered00,EOcounts1_filtered00,s=2,label = "E1 - $00°$")
    # plt.scatter(lshell2_filtered00,EOcounts2_filtered00,s=2,label = "E2 - $00°$")
    # plt.scatter(lshell3_filtered00,EOcounts3_filtered00,s=2,label = "E3 - $00°$")
    # plt.scatter(lshell4_filtered00,EOcounts4_filtered00,s=2,label = "E4 - $00°$")
     
    # plt.title('EOcounts vs Lshell (Filtered)')
    # plt.minorticks_on()
    # plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
    # plt.grid(which='minor',linestyle='--',alpha=0.5)
    # plt.xlabel('LShell')
    # plt.ylabel('EOCounts')
    # plt.legend()
    # plt.savefig("project_Ic.png")
    # plt.show()
    
    
 
    # plt.scatter(lshell1_filtered90,EOcounts1_filtered90,s=2,label = "E1 - $90°$")
    # plt.scatter(lshell2_filtered90,EOcounts2_filtered90,s=2,label = "E2 - $90°$")
    # plt.scatter(lshell3_filtered90,EOcounts3_filtered90,s=2,label = "E3 - $90°$")
    # plt.scatter(lshell4_filtered90,EOcounts4_filtered90,s=2,label = "E4 - $90°$")
     
    # plt.title('EOcounts vs Lshell (Filtered)')
    # plt.minorticks_on()
    # plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
    # plt.grid(which='minor',linestyle='--',alpha=0.5)
    # plt.xlabel('LShell')
    # plt.ylabel('EOCounts')
    # plt.legend()
    # plt.savefig("project_Ic.png")
    # plt.show()
    
    
    
    #STATISTICS
    
    #Channel 1:
    mean00_1 = EOcounts1_filtered00.mean()
    meanlist00_E1.append(mean00_1)
    
    mean90_1 = EOcounts1_filtered90.mean()
    meanlist90_E1.append(mean90_1)

    print(mean00_1)
    print(mean90_1)
    print()
    
    #Channel 2:
    mean00_2 = EOcounts2_filtered00.mean()
    meanlist00_E2.append(mean00_2)

    mean90_2 = EOcounts2_filtered90.mean()
    meanlist90_E2.append(mean90_2)

    print(mean00_2)
    print(mean90_2)
    print()
    
    #Channel 3:
    mean00_3 = EOcounts3_filtered00.mean()
    meanlist00_E3.append(mean00_3)
    
    mean90_3 = EOcounts3_filtered90.mean()
    meanlist90_E3.append(mean90_3)

    print(mean00_1)
    print(mean90_1)
    print()
    
    #Channel 4:
    mean00_4 = EOcounts4_filtered00.mean()
    meanlist00_E4.append(mean00_4)

    mean90_4 = EOcounts4_filtered90.mean()
    meanlist90_E4.append(mean90_4)

    print(mean00_4)
    print(mean90_4)


plt.scatter(n,meanlist00_E1,s=2,label = "E1 - $00°$")
plt.scatter(n,meanlist00_E2,s=2,label = "E2 - $00°$")
plt.scatter(n,meanlist00_E3,s=2,label = "E3 - $00°$")
plt.scatter(n,meanlist00_E4,s=2,label = "E4 - $00°$")
 
plt.title('EOcount00 Means over Trials')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Number of Days')
plt.ylabel('Mean EOCounts')
plt.xlim(1, None) 
plt.legend()
plt.savefig("project_IIa.png")
plt.show()
    
plt.scatter(n,meanlist90_E1,s=2,label = "E1 - $90°$")
plt.scatter(n,meanlist90_E2,s=2,label = "E2 - $90°$")
plt.scatter(n,meanlist90_E3,s=2,label = "E3 - $90°$")
plt.scatter(n,meanlist90_E4,s=2,label = "E4 - $90°$")
 
plt.title('EOcount90 Means over Time')
plt.minorticks_on()
plt.grid(which='major',linestyle='-',alpha=0.8)   # add a grid to the major ticks
plt.grid(which='minor',linestyle='--',alpha=0.5)
plt.xlabel('Number of Days')
plt.ylabel('Mean EOCounts')
plt.xlim(0.7, None) 
plt.legend()
plt.savefig("project_IIb.png")
plt.show()