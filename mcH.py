import numpy as np
import emcee
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import minimize
import corner
from IPython.display import display, Math
import random
import math as math
import scipy as sc
import pandas as pd
import statistics 
import astropy.cosmology
import scipy.stats as stats
import astropy.constants as const
from scipy.integrate import quad
import scipy.integrate as integrate
from astropy.cosmology import Planck18  as cosmo
from astropy.cosmology import w0wzCDM
from astropy import units as u
import scipy.stats.kde as kde



c = 3*10**5 #km/s
z= 0.08499
z_ = [0.06,0.11]
zm = np.mean ([z_[0],z_[1]])


df1 = pd.read_csv('bilby_z2f18m_samples.dat',delimiter=' ')
dl1 = np.array(df1['luminosity_distance'])
d1 = sc.stats.gaussian_kde(df1['luminosity_distance'])
pdf1=d1(df1["luminosity_distance"])







#fig, ax1 = plt.subplots(figsize=(10,7))

#ax1.set_ylabel('Density Distribution')
#ax1.set_xlabel('Luminosity Distance')
#ax1.bar(df1["luminosity_distance"], d1(df1["luminosity_distance"]), color = 'y')
#ax1.tick_params(axis ='y')
#ax2 = ax1.twinx()
#ax2.set_ylabel('Distribution')
#ax2.hist(df1['luminosity_distance'], color = 'skyblue', alpha = 0.65, bins = 35)
#fig.suptitle(r'KDE estimation on $d_L$ for sample in z = 0.06-0.11')
#fig.tight_layout()
#plt.show()



def E(z):
	return np.sqrt((cosmo.Om0 * (1+z)** 3) + (1-cosmo.Om0))
	
def log_likelihood(theta, z, dl1 , pdf1):
    H0 = theta    
  #  var = H0 * u.km/u.s/u.Mpc
    cosmo1 = w0wzCDM(H0=float(theta), Om0=cosmo.Om0, Ode0=1.-cosmo.Om0, w0=-1, wz=0)   
    model = np.array(cosmo1.luminosity_distance(z))
    log_l = np.log(np.interp (model,dl1,pdf1))
    return  log_l
    
def log_prior(theta):
    H0 = theta
    if 20 <= H0 <= 200:
        return 0.0
    return -np.inf    
    
def log_probability(theta, z, dl1, pdf1):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, z, dl1, pdf1)
    
#emcee
pos = 40 + 10 * np.random.randn(10, 1)
nwalkers, ndim = 10,1

sampler = emcee.EnsembleSampler(nwalkers, ndim, log_probability, args=(z, dl1, pdf1))
sampler.run_mcmc(pos, 10000, progress=True)
allsamples = sampler.chain    
#print (len(allsamples[0]))  
samp = []
samp1 = []
samp2 = []
samp3 = []
samp4 = []
samp5 = []

for i in range(len(allsamples)):
	samp.append(allsamples[i][5000:])



plt.subplots(figsize=(10,7))
for i in range(len(samp)):
	plt.hist(samp[i],bins=30,label=i+1)
plt.legend()

plt.show()
