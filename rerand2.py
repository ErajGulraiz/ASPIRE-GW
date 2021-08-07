import numpy as np
import random

import astropy
from astropy.cosmology import Planck18
from astropy.cosmology import WMAP9 as cosmo
import csv
import pandas as pd

# FINDING THE MEAN FOR REDSHIFT BIN
z_ = [0.11,0.16]
mean = np.mean ([z_[0],z_[1]])
#print(mean)

#Masses from bin 1 
#print('#################masses from THIRD bin###################')
mass=[]
with open('z3.txt') as csv_file:
    reader = csv.reader(csv_file, delimiter=' ')
    for row in reader:
    	for i in row:
    		mass.append(i)
#print (mass)

#print (len(mass))

mass_= (mass[31:])
#print(mass_)
print(len(mass_))

# NS MASS RANDOM SELECTION 
#RANDOM SELECTION FOR RA
#RANDOM SELECTION FOR DEC
#RANDOM SELECTION FOR THETAJN



m3 =[]
ra3 = []
dec3 =[]
tj3 =[]
for i in range(len(mass_)):
	m3=(np.random.uniform(1,2,1))
	ra3=(np.random.uniform(0,2*np.pi,1))
	dec3=(np.random.uniform(-np.pi/2,np.pi/2,1))
	tj3=(np.random.uniform(0,np.pi,1))
	#print (m3,ra3,dec3,tj3)
	
#print('##############################################'
f3 = pd.read_csv('rerandz3',delimiter=' ')
m_3 = f3['m3']
print(m_3[0])
ra_3 =f3['ra3']
print(ra_3[0])
dec_3 = f3['dec3']
print(dec_3[0])
tj_3 = f3['tj3']
print (tj_3 [0])











