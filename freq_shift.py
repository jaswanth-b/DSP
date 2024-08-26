import numpy as np
import matplotlib.pyplot as pt
x1=[1,2,3,4,5]
n=len(x1)
for i in range(n):
    x1[i]=np.exp(1j*3*n)*x1[i]
def dtft(x,n):
    w=np.arange(-np.pi,np.pi,0.01)
    X=np.zeros(len(w),dtype=complex)
    for k in range(len(w)):
        X[k]=sum(x[i]*np.exp(-1j*w[k]*i) for i in range(n))
    return w,X

w,X1=dtft(x1,n)
pt.figure(figsize=(8,4))
pt.title("X1(W)")
pt.plot(w,np.abs(X1))

a=[0,0,0]
x=x1.copy()
w,X=dtft(x,n)
for i in a:
    X+=i
X=np.roll(X,3)
pt.figure(figsize=(8,4))
pt.title("X(W)")
pt.plot(w,np.abs(X),color='gold')
if(X.all()==X1.all()):
    print("frequency shift verified")