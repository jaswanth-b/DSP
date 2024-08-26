import numpy as np
import matplotlib.pyplot as plt
n=np.arange(0,1000)
N=len(n)
x=np.cos(2*np.pi*200*n/N)
def dft(x,N):
    f=[]
    omega=np.arange(0,2*np.pi,(2*np.pi/N))
    for i in range(0,N):
        X=[]
        for k in range(0,N):
            a=x[k]*np.exp(-1j*(2*np.pi*k*i)/N)
            X.append(a)
        f.append(sum(X))
    return omega,f
w,Y=dft(x,N)
plt.stem(w,np.abs(Y))
plt.xlabel("Omega")
plt.ylabel("Amplitude")
plt.show()
plt.stem(w,np.angle(Y))
plt.xlabel("Omega")
plt.ylabel("Amplitude")
plt.show()
