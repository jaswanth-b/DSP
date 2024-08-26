import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
w=np.arange(-np.pi, np.pi,.01)
X=np.zeros(len(w),dtype=complex)
for n in range(len(x)):
    X+=x[n]*np.exp(-1j*w*n)
ESD = np.abs(X)**2

plt.figure(figsize=(10,6))
plt.plot(w,ESD)
plt.title('Energy Spectral Density of x[n]')
plt.xlabel('Frequency')
plt.ylabel('Energy Spectral Density')
plt.show()
