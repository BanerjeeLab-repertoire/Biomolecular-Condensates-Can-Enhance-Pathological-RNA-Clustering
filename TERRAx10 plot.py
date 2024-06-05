# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:30:04 2023

@author: Gable
"""
import matplotlib.pyplot as plt
from scipy.stats import sem
# from scipy.interpolate import make_lsq_spline
import numpy as np
# Terrax10
ConcMg = [1,5,5.5,5.75,5.8,6.009,6,6.1,6.2,6.25,6.3,6.4,6.5,7,7.5,10,25,50,61,75,100,250,500]
trial1 = [90,90,90,82,79,77,70.9,59.1,61.8,65,60.3,57.1,58.9,5,5,5,5,5,5,5,5,5,5]
trial2 = [90,90,90,81,77,78,72.7,64.8,68.7,67,62.4,58.6,60.9,5,5,5,5,5,5,5,5,5,5]
trial3 = [90,90,90,81,74,70,73.5,68.4,59.9,61,57.9,61.8,57.8,5,5,5,5,5,5,5,5,5,5]
trmean = [np.mean([trial1[i], trial2[i], trial3[i]]) for i in range(len(trial1))]
trstderr = [sem([trial1[i], trial2[i], trial3[i]]) for i in range(len(trial1))]
plt.errorbar(ConcMg,trmean,yerr=trstderr,capsize=8,fmt='ko',markersize=5)
plt.plot(ConcMg,trial1,'ko')
plt.plot(ConcMg,trial2,'ko')
plt.plot(ConcMg,trial3,'ko')
