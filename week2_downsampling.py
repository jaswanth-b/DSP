import numpy as np 
import matplotlib.pyplot as pt
from scipy.io import wavfile
fs,x=wavfile.read("Classical.wav")
def downsampling(fs,x):
    factor=int(input("Enter downsampling factor"))
    y=np.zeros(int(len(x)/factor))
    for i in range(int(len(x)/factor)):
        if(i%factor==0):
            y[i]=x[i]
        else:
            pass
    return fs,y
Fs,Y=downsampling(fs,x)
wavfile.write("downsampled.wav",Fs,Y)
