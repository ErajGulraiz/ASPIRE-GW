import numpy as np
import matplotlib.pyplot as plt
import random

intbhlist = np.random.uniform(5,50,size=100)

prob = 1/intbhlist**2.35

def distribution(m):
	return 1/m**2.35 
	
plt.plot(intbhlist,distribution(intbhlist),'*')
plt.xlabel (r'$M_{\odot}$')
plt.ylabel ('P (m)')
plt.title('Random BH souces acc. to analytical form of Prob. Distribution')
plt.show()


 #plt.plot(intbhlist,distribution(intbhlist),'*',intbhlist,distribution(random_bh),'*')
#plt.hist(intbhlist, weights=prob, bins= len (intbhlist))

#plt.title('100 random BH')
#plt.ylabel('P(m)')
#plt.xlabel('Indices')
#plt.savefig ('100 values.jpg')
#plt.show()
