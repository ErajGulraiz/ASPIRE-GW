import numpy as np
import matplotlib.pyplot as plt
import random
import math as math
import scipy as sc
import csv
from numpy import *
from step2 import *
from struct import pack, unpack

alpha=-2.35
mmin=5.
mmax=50.

def distribution(m):      #analytical form of P(m) to calculate for each random mass
	return 1/m**2.35 




for i in np.arange(len(test)):

	samplesize= test[i]
	print (samplesize)
	intbhlist = np.random.uniform(5,50,size=test[i])
	nc= (alpha+1)/(mmax**(alpha+1)-mmin**(alpha+1)) #integration of P(m)
	ran= np.random.uniform(0,1,samplesize)

	xran= float(((alpha+1)*ran/nc +mmin**(alpha+1))**(1./(alpha+1)))
	 #exact form of power law prob dist, normalizing the area under the curve to make it a probability density function.

	
		
	
	#file = open ('z'+str(i+1)+'.txt', "w")
	#file.write(xran)
	#file.close()
		
	
		#with open ('z'+str(i+1)+'.dat', "w") as fout:

		#	fout.write(str(xran))
			
	plt.hist(xran)
	plt.show()

	 
	plt.plot(intbhlist,distribution(intbhlist),'*')
	plt.xlabel (r'$M_{\odot}$')
	plt.ylabel ('P (m)')
	plt.title('Random BH souces acc. to analytical form of Prob. Distribution')
	plt.show()

	
	fig, ax1 = plt.subplots(figsize=(10,7))
	ax1.set_ylabel('P (m)')
#x1.set_xticks([0,5,10,15,20,25,30,35,40,45,50])
	ax1.set_xlabel(r'$M_{\odot}$')
	ax1.plot(intbhlist,distribution(intbhlist),'k1')#plotting the bh random sources that fall in the uniform mass distribution 
	ax1.tick_params(axis='y')
	ax2 = ax1.twinx()
	ax2.set_ylabel('Distribution of the random masses')  # sharing x-axis with first plot i.e. the random sources or indicesin solar masses
	ax2.hist(xran,color='skyblue',alpha=0.65) 
#the histogram for the exact form of power law prob distribution 
	ax2.tick_params(axis='y')
	fig.suptitle('BH GW Sources in Mass Distribution')
	fig.tight_layout() 

# plt.savefig('distribution_with_help.jpg')
	plt.show()
		
	






