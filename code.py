#week 1

import numpy as np
import matplotlib.pyplot as plt
import random

plt.rcParams.update({'font.size': 15,'font.family':'serif'})
intbhlist = np.random.randint(5,50,size=100)

bhlist = []
for i in range(0, 100):
    x = round(random.uniform(5., 50.),1)
    bhlist.append(x)
    random_bh = np.array(bhlist)
    
prob = 1/intbhlist**2.35
prob_ = 1/random_bh**2.35

# val = np.linspace(5,50,100)
plt.subplots(figsize=(10,7))
plt.plot(intbhlist,'*')
plt.title('100 random BH')
plt.ylabel(r'$M_{\odot}$')
plt.xlabel('index')
plt.savefig ('100 values.jpg')
plt.show()

plt.subplots(figsize=(10,7))

def distribution(m):
#     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    return 1/m**2.35

plt.plot(intbhlist,distribution(intbhlist),'*',intbhlist,distribution(random_bh),'*')
plt.xlabel (r'$M_{\odot}$')
plt.ylabel ('P (m)')
plt.show()
# plt.savefig('distribution.jpg')

plt.subplots(figsize=(10,7))
plt.subplot(141)
plt.hist (prob)
plt.title('integer')
plt.subplot(142)
plt.hist (prob_)
plt.title('float')
plt.subplot(143)
plt.plot (intbhlist,prob,'*')
plt.title('integer')
plt.subplot(144)
plt.plot (intbhlist,prob_,'*')
plt.title('float')
plt.tight_layout()
# plt.savefig ('kind of result.jpg')
plt.show()

#here is the new code of the new plot
fig, ax1 = plt.subplots(figsize=(10,7))
ax1.set_xlabel('P (m)')
ax1.set_ylabel(r'$M_{\odot}$')
ax1.plot(distribution(intbhlist),intbhlist,'k1')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('Distribution of the random masses')
ax2.hist(distribution(intbhlist),color='skyblue',alpha=0.65)
ax2.tick_params(axis='y')
fig.tight_layout()
# plt.savefig('distribution_new.jpg')
plt.show()

#sunday
data = np.loadtxt('Merger_rate_NSBH_rate_ch_3_time_delay_1.0_power_law_1_rate_0.dat' )
redshift = data [:,0]
merger_rate = data [:,1]
plt.subplots(figsize=(10,7))
plt.plot(redshift,merger_rate,'.-')
plt.xlabel('redshift (z)')
plt.ylabel(r'$R_{GW}(z)\ [Gpc^{-3}\ yr^{-1}]$')
plt.show()

##updated plot
#suvodip's codes
alpha=-2.35
mmin=5.
mmax=50.
samplesize=10**6
nc= (alpha+1)/(mmax**(alpha+1)-mmin**(alpha+1))
ran= np.random.uniform(0,1,samplesize)
xran= ((alpha+1)*ran/nc +mmin**(alpha+1))**(1./(alpha+1))
#updated plot
fig, ax1 = plt.subplots(figsize=(10,7))
ax1.set_ylabel('P (m)')
ax1.set_xlabel(r'$M_{\odot}$')
ax1.plot(random_bh,distribution(random_bh),'k1')
ax1.tick_params(axis='y')
ax2 = ax1.twinx()
ax2.set_ylabel('Distribution of the random masses')  # we already handled the x-label with ax1
ax2.hist(xran,color='skyblue',alpha=0.65)
ax2.tick_params(axis='y')
fig.tight_layout() 
# plt.savefig('distribution_with_help.jpg')
plt.show()

