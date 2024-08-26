import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3,4]
y=[1,2,3,4,0,0,0]
y1=np.roll(y,3)
n=len(y1)
def dtft(x,n):
    w=np.arange(-np.pi,np.pi,0.01)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=sum(x[i]*np.exp(-1j*w[k]*i) for i in range(n))
    return w,X

w,Y1=dtft(y1,n)
pt.figure(figsize=(12,8))
pt.subplot(2,1,1)
pt.title("dtft of x[n-3]")
pt.plot(w,np.abs(Y1))
w,X1=dtft(x1,len(x1))
X1=np.exp(-1j*w*3)*X1
pt.subplot(2,1,2)
pt.title("e^-jw3X(w)")
pt.plot(w,np.abs(X1))
pt.show()
if(X1.all()==Y1.all()):
    print("time shift verified")
