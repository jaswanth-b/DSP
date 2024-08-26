import numpy as np
from matplotlib import pyplot as plt
fs=8000
t=np.arange(0,0.5,1.0/fs)
x=np.sin(2*np.pi*200*t)
ts=np.arange(0,int(.5*fs),8)
y=x[ts] #sampled signal
plt.plot(y)
plt.title("sampled signal with 8kHz")
plt.show()

fs=1000
ts=np.arange(0,int(0.5*fs),1)
Y=x[ts]
plt.plot(Y)
plt.title("resampled signal with 1kHz")
plt.show()

Yrange=np.max(Y)+abs(np.min(Y))
L=8
step=Yrange/float(L)
q_levels=np.arange(np.min(Y),np.max(Y),step)
z=[]
for i in Y:
    z.append(q_levels[np.argmin(abs(q_levels-i))])
plt.plot(z)
plt.title("Quantized signal")
plt.show()
with open("quantize.txt","wb") as k:
    for i in z:
        k.write(i)
