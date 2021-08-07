import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import scipy.integrate as integrate
from scipy import interpolate
from scipy.integrate import simps
from astropy.cosmology import Planck18  as cosmo # Planck 2018
import random

import astropy.constants

plt.rcParams.update({'font.size': 15,'font.family':'serif'})

data = np.loadtxt('Merger_rate_NSBH_rate_ch_3_time_delay_1.0_power_law_1_rate_0.dat' )
redshift = np.array(data [:,0])
merger_rate = np.array(data [:,1])
#plot of the dat file for R_gw as a fuction of zmean
plt.subplots(figsize=(10,7))
plt.plot(redshift,merger_rate,'.-')
plt.xlabel('Redshift (z)')
plt.ylabel(r'$r_{GW}(z)\ [Gpc^{-3}\ yr^{-1}]$') 

#defining redshift limits for different bin size from 0-2
z_ = np.arange(0.01,2.03,0.05)

#upper and lower limits
z0 = np.mean(z_[0]+z_[1]) - ((z_[0]+z_[1])/2)
z1 = np.mean(z_[0]+z_[1]) + ((z_[0]+z_[1])/2)

mergemean = np.mean(merger_rate[0]+merger_rate[1]+merger_rate[2])

#Interpolating the redshift array from the data file to insert the points corresponding to dz factor and get values for merger rate
interp = interpolate.interp1d (redshift, merger_rate)
def r_gw(z):
    return interp(z)

fig, ax = plt.subplots(figsize=(10,6))
f = interpolate.interp1d(redshift, merger_rate)
z_bins = (random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10),random.uniform(0, 10))
ynew = f(z_bins)
plt.grid (linewidth=1.0,linestyle='dashed')
plt.plot(redshift, merger_rate, z_bins, ynew,'o')
plt.xlabel ('z')
plt.ylabel(r'$r_{gw}$')

#plt.show()

def integral(z):
    return 4 * np.pi * ( np.array (cosmo.differential_comoving_volume(z) / 10**9) * r_gw(z) / (1+z) )
    
testf = []
for i in range(len(z_)-1):
    testf.append( integrate.quad( lambda z: 4 * np.pi * ( np.array (cosmo.differential_comoving_volume(z) / 10**9) *
                                                        r_gw(z) / (1+z) ) ,z_[i],z_[i+1])[0] )

print (testf)
test = np.around(testf)
test = test.astype(int)
print (test)
    
plt.subplots(figsize=(8,7))
plt.bar(z_[0:len(z_)-1],test,width=0.02)
plt.xlabel ('z')
plt.ylabel(r'$R_{gw} \ yr^{-1}$')
#plt.show()

