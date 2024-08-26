import numpy as np 
import matplotlib.pyplot as pt
from scipy.io import wavfile
fs,x=wavfile.read("Classical.wav")
def upsampling(fs,x):
    factor=int(input("Enter upsampling factor"))
    y=np.zeros(factor*len(x))
    for i in range(len(x)):
        if(i%factor==0):
            y[i]=x[i]
        else:
            y[i]=0
    return fs,y
Fs,Y=upsampling(fs,x)
wavfile.write("upsampled.wav",Fs,Y)
