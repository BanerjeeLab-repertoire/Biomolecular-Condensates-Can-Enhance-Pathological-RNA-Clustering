# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 12:16:40 2023

@author: Gable
"""

# import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.animation as mplani
import tifffile
from im2bwM import im2bw
# from skimage import morphology,measure
# from skimage import restoration
from skimage.filters import (threshold_niblack,
                             threshold_sauvola, threshold_multiotsu,threshold_otsu)

from scipy import ndimage as ndi
#Ch1 is the FAM channel e.g. TERRA
#Ch2 is the 594/640 channel e.g. RG5 or T40
#0hr
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and A594\Image 7.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and A594\Image 8.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and A594\Image 9.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and A594\Image 10.tif"

# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and Cy5\Image 28.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and Cy5\Image 30.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\0hr\FAM and Cy5\Image 31.tif"

#4hr
fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\4hr\FAM and A594\Image 22.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\4hr\FAM and A594\Image 23.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\4hr\FAM and A594\Image 24.tif"
# fname1 = r"C:\Users\Gable\Desktop\TERRA4 ternary condensates manders analysis data\4hr\FAM and A594\Image 24.tif"
# fname1 = r"C:\Users\Gable\Desktop\TERRA4 ternary condensates manders analysis data\4hr\FAM and A594\Image 24.tif"

# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\4hr\FAM and Cy5\Image 25.tif" 
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\4hr\FAM and Cy5\Image 26.tif"
# fname1 = r"C:\Users\Gable\Desktop\TERRA4 ternary condensates manders analysis data\0hr\FAM and Cy5\Image 6.tif"
# fname1 = r"C:\Users\Gable\Desktop\TERRA4 ternary condensates manders analysis data\4hr\FAM and Cy5\Image 25.tif"

#8hr
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and A594\Image 23.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and A594\Image 24.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and A594\Image 25.tif"

# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and Cy5\Image 36.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and Cy5\Image 37.tif"
# fname1 = r"C:\Users\Gable\Desktop\Tharun coloc\8hr\FAM and Cy5\Image 38.tif"



# strings to paths for file access (edit these if needed)
# saveloc = 'C:\\Users\\Gable\\Documents\\python codes\\'
# oname = fname[fname.rfind('\\')+1:fname.find('_MMS')]

Im = tifffile.imread(fname1)
# Im2 = tifffile.imread(fname2)
Im1 = Im[0,:,:]
Im2 = Im[1,:,:]

ths1o = threshold_multiotsu(Im1, classes = 3)
ths2o = threshold_multiotsu(Im2, classes = 3)

ths1 = threshold_niblack(Im1)
ths2 = threshold_niblack(Im2)
Maskini11 = im2bw(Im1.copy(),ths1)
Maskini21 = im2bw(Im2.copy(),ths2)
Maskini11 = ndi.binary_fill_holes(Maskini11)
Maskini21 = ndi.binary_fill_holes(Maskini21)



Maskini12 = im2bw(Im1.copy(),1.15*ths1o[1])

Maskini22 = im2bw(Im2.copy(),1.15*ths2o[1])

# plt.figure()
# plt.imshow(Maskini11)
# plt.figure()
# plt.imshow(Maskini12)

# plt.figure()
# plt.imshow(Maskini21) 
# plt.figure()
# plt.imshow(Maskini22)

templog1 = Maskini11==1
templog2 = Maskini21==1
templog3 = templog1 & templog2
templog4 = Maskini12==1
templog5 = Maskini22==1
templog6 = templog4 & templog5

# plt.figure()
# plt.scatter(Im1[templog4][:],Im2[templog4][:], marker='o', alpha=.005)
# plt.figure()
# plt.scatter(Im1[templog5][:],Im2[templog5][:], marker='o', alpha=.005)
# print(np.mean(Im1[templog4])/np.mean(Im1[templog5]),np.mean(Im2[templog4])/np.mean(Im2[templog5]))
##%%

plt.figure() 
plt.hist2d(Im1[templog4][:],Im2[templog4][:])
#%%
#Colocalization of primary condensate
#Pearson's test
Px = Im1.flatten()
Py = Im2.flatten()
Pxmean = np.average(Px)
Pymean = np.average(Py)
Pstat = np.sum((Px-Pxmean)*(Py-Pymean))/(np.sqrt(np.sum((Px-Pxmean)**2))*np.sqrt(np.sum((Py-Pymean)**2)))

#Mander's test
Mcoeff1 = np.sum(templog3)/np.sum(templog1)
Mcoeff2 = np.sum(templog3)/np.sum(templog2)

print(Pstat,Mcoeff1,Mcoeff2)

#Mander's test
Mcoeff3 = np.sum(templog6)/np.sum(templog4)
Mcoeff4 = np.sum(templog6)/np.sum(templog5)

print(Mcoeff3,Mcoeff4)






