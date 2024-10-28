import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3]
x2=[1,2,3,0,0]
x3=[1,2,3,0,0,0,0,0,0,0]
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
    
w,X1=dft(x1,len(x1))
pt.figure(figsize=(20,10))
pt.subplot(3,1,1)
pt.plot(np.abs(X1))
w,X2=dft(x2,len(x2))
pt.subplot(3,1,2)
pt.plot(np.abs(X2))
w,X3=dft(x3,len(x3))
pt.subplot(3,1,3)
pt.plot(np.abs(X3))
pt.show()
