# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 12:33:14 2023

@author: Gable
"""

import matplotlib.pyplot as plt
from scipy.stats import sem
import numpy as np

#TERRA mut Dx10 e.g. UUAGUGx10

#LCST
ConcMg = [10,20,25,50,75,100]
trial1 = [80,31,28.8,26.7,16.8,14.1]
trial2 = [80,30.7,29.7,24.4,15.1,12.8]
trial3 = [80,30.4,27.9,23.7,14.9,15.7]
trmean = [np.mean([trial1[i], trial2[i], trial3[i]]) for i in range(len(trial1))]
trstderr = [sem([trial1[i], trial2[i], trial3[i]]) for i in range(len(trial1))]


plt.plot(ConcMg,trial1,'ko')
plt.plot(ConcMg,trial2,'ko')
plt.plot(ConcMg,trial3,'ko')
plt.errorbar(ConcMg,trmean,yerr=trstderr,capsize=8,fmt='ko',markersize=10)