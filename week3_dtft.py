import numpy as np
import matplotlib.pyplot as plt
n=np.arange(0,500)
x=np.sin(2*np.pi*200/8000*n)
def dtft(x):
    w=np.arange(-np.pi,np.pi,0.0001*np.pi)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=np.sum(x*np.exp(-1j*w[k]*np.arange(len(x))))
    return w,X
w,X=dtft(x)
plt.figure(figsize=(12,6))
plt.subplot(2,1,1)
plt.title("magnitude spectrum")
plt.plot(w,np.abs(X))
plt.subplot(2,1,2)
plt.title("phase spectrum")
plt.plot(w,np.angle(X))
plt.show()
