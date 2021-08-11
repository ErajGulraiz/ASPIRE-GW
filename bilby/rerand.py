import numpy as np
import random

from astropy import *
from astropy.cosmology import Planck18
from astropy.cosmology import WMAP9 as cosmo


# FINDING THE MEAN FOR REDSHIFT BIN
z_ = [0.06,0.11]
mean = np.mean ([z_[0],z_[1]])
#print(mean)

#Masses from bin 1 
#print('#################masses from first bin###################')
mass = np.array([17.67348897, 18.12824322, 22.67224203, 5.00506296, 5.42772817])
#print (len(mass))

# NS MASS RANDOM SELECTION 
#RANDOM SELECTION FOR RA
#RANDOM SELECTION FOR DEC
#RANDOM SELECTION FOR THETAJN

m1 =[]
ra = []
dec =[]
tj =[]
for i in range(len(mass)):
	m1=(np.random.uniform(1,2,1))
	ra=(np.random.uniform(0,2*np.pi,1))
	dec=(np.random.uniform(-np.pi/2,np.pi/2,1))
	tj=(np.random.uniform(0,np.pi,1))
	#print (m1,ra,dec,tj)
	
#print('#################masses from second bin###################')

#Masses from bin2 my runs
mass2=	np.array([5.38833375, 9.74641918, 6.132627, 26.92989225, 6.05386231, 5.8415517, 19.76439382, 11.58501246, 5.42193772, 12.89658199, 25.92823793, 11.42820879, 14.38508758])
#print(mass2[0])
#print (len(mass2))
m2 =[]
ra2 = []
dec2 =[]
tj2 =[]
for i in range(len(mass2)):
	m2=(np.random.uniform(1,2,1))
	ra2=(np.random.uniform(0,2*np.pi,1))
	dec2=(np.random.uniform(-np.pi/2,np.pi/2,1))
	tj2=(np.random.uniform(0,np.pi,1))
	#print (m2,ra2,dec2,tj2)
	
#print('##############################################')
	










