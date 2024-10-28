import numpy as np
def fft(x):
    N=len(x)
    if(N==1):
        return x
    if(N%2!=0):
        x.append(0)
        N += 1
    if(N==2):
        return [x[0] + x[1], x[0] - x[1]]
    xe=x[0::2] 
    xo=x[1::2]    
    Xe=fft(xe)
    Xo=fft(xo)
    WN=np.exp(-2j*np.pi*np.arange(N//2)/N)
    X=[Xe[k]+WN[k]*Xo[k] for k in range(N//2)]+[Xe[k]-WN[k]*Xo[k]for k in range(N//2)]
    return X

import numpy as np
x=[1,2,3,4]
y=fft(x)
print("FFT:",y)
def dft(x,N):
    X=np.zeros(N,dtype=complex)
    for k in range(N):
        for n in range(N):
            X[k]+=x[n]*np.exp(-1j*(2*np.pi*k*n)/N)
    return X
N=len(x)
z=dft(x,N)
print("\nDFT:",z)
X=np.fft.fft(x)
print("\nnumpy fft:",X)
from scipy.fft import fft
X=fft(x)
print("\nScipy fft:",X)
