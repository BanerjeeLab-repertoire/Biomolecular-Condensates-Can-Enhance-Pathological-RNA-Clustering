#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 12:06:16 2023

@author: tharun
"""

import pandas as pd
import matplotlib.pyplot as plt


sheet_name = "insert"  # insert here means include the path for the raw excel file containing FRAP data


df = pd.read_excel(r'insert') # insert here means include the path for the raw excel file containing FRAP data


x_data = df['Time_0']
y_data = df['0 hours']
y_std = df['SE']


x_data_2 = df['Time_4']
y_data_2 = df['4 hours']
y_std_2 = df['SE']


x_data_4 = df['Time_8']
y_data_4 = df['8 hours']
y_std_4 = df['SE']


plt.plot(x_data, y_data, label='0 hr', linewidth=2, linestyle='-', marker='o')
plt.fill_between(x_data, y_data-y_std, y_data+y_std, alpha=0.2)


plt.plot(x_data_2, y_data_2, label='4 hr', linewidth=2, linestyle='-', marker='o')
plt.fill_between(x_data_2, y_data_2-y_std_2, y_data_2+y_std_2, alpha=0.2)

plt.plot(x_data_4, y_data_4, label='8 hr', linewidth=2, linestyle='-', marker='o')
plt.fill_between(x_data_4, y_data_4-y_std_4, y_data_4+y_std_4, alpha=0.2)


plt.xlabel('Time (s)', fontsize=16)
plt.ylabel('Recovery %', fontsize=16)
plt.legend()


plt.xlim([0, 90])
plt.ylim([0, 1.1])


plt.tick_params(axis='both', which='major', labelsize=16)


plt.show()
