import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3]
a=len(x1)
x2=[4,5,6,7]
b=len(x2)
x3=np.convolve(x1,x2)
print("Linear convolution =", x3)
if(a<b):
    for i in range(min(a,b),a+b-1):
        x1.append(0)
    for i in range(max(a,b),a+b-1):
        x2.append(0)
else:
    for i in range(max(a,b),a+b-1):
        x1.append(0)
    for i in range(min(a,b),a+b-1):
        x2.append(0)
def cycle_delay(x,m):
    N=len(x)
    y=[]
    for n in range(0,N):
        if (n-m>=0):
            idx=(n-m)%N
        else:
            idx=N+n-m
        y.append(x[idx])
    return y
def circularconv(x1,x2):
    z=[]
    x2r=[]
    x2r.append(x2[0])
    for i in range(len(x2)):
        if(len(x2)-i-1!=0):
            x2r.append(x2[len(x2)-i-1])
    for n in range(len(x1)):
        y=cycle_delay(x2r,n)
        z.append(np.dot(x1,y))
    return z
Y=circularconv(x1,x2)
print("circular convolution =",Y)
pt.figure(figsize=(12,6))
pt.subplot(2,1,1)
pt.title("Linear convolution")
pt.stem(x3)
pt.subplot(2,1,2)
pt.title("Circular convolution")
pt.stem(Y)
pt.show()
