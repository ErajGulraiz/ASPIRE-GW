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

plt.subplots(figsize=(10,7))

def distribution(m):
#     return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    return 1/m**2.35

plt.plot(intbhlist,distribution(intbhlist),'*',intbhlist,distribution(random_bh),'*')
plt.xlabel (r'$M_{\odot}$')
plt.ylabel ('P (m)')
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

#sunday
data = np.loadtxt('Merger_rate_NSBH_rate_ch_3_time_delay_1.0_power_law_1_rate_0.dat' )
redshift = data [:,0]
merger_rate = data [:,1]
plt.subplots(figsize=(10,7))
plt.plot(redshift,merger_rate,'.-')
plt.xlabel('redshift (z)')
plt.ylabel(r'$R_{GW}(z)\ [Gpc^{-3}\ yr^{-1}]$')
