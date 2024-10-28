import numpy as np
from matplotlib import pyplot as plt
from scipy import signal
p1=float(input("pole location on z plane:"))
p2=float(input("frequency of pole:"))
z1=float(input("zero location on z plane:"))
z2=float(input("frequency of zero:"))
pole=p1*np.exp(1j*p2)
zero=z1*np.exp(1j*z2)
w=np.arange(-np.pi,np.pi,0.001)
H=np.zeros(len(w),dtype=complex)
for i in range(len(w)):
    H[i]=(1-zero*np.exp(-1j*w[i]))/(1-pole*np.exp(-1j*w[i]))
plt.plot(w,np.abs(H))
plt.show()
