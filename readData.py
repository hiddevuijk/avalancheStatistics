import numpy as np
import matplotlib.pyplot as plt
from criticality import *
import scipy.stats.stats as st

xt = np.genfromtxt('xt.csv',delimiter=';')
phit = np.tanh(xt)

print xt.shape

s = fr2spike(phit,0.1)
sau = SimActiveUnits(s)
av = avalancheSize(sau)
print np.mean(sau)
print np.std(sau)
print st.skew(sau,bias=False)

plt.hist(sau,bins=50)
plt.show()


