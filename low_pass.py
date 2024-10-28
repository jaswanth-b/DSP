import random
import numpy as np
from matplotlib import pyplot as plt

fs=int(input("Enter sampling Frequency: "))
N=int(input("Enter Lenght(N): "))
fc=int(input(f"Enter cut_off frequency(should be less than {fs/2}): "))
if fc<=(fs/2):
	F=[]
	for k in range(0,(N//2)+1):
		F.append((fs/N)*k)
	
	kc=-1
	for i in range(len(F)):
		kc+=1
		if fc<=F[i]:
			break

	#Finding impulse signal
	H=[0]*(N)
	for i in range(0,kc):
		H[i]=1
	for j in range(-1,-kc-1,-1):
		H[j]=1
	print(H)

	#Generating Random signal
	signal=[]
	for i in range(N):
		signal.append(random.randint(0,50))
	
	#DFT of signal
	N = len(signal)
	dft = [0]*(N+1)
	for k in range(N):  
	    for n in range(N):  
	        dft[k] += signal[n] * np.exp(-2j * np.pi * k * n / N)

	convulution=[0]*(N+1)
	for i in range(N):
		convulution[i]=abs(dft[i]*H[i])
	print(convulution)
else:
	print("cut_off Frequency is greater than nyquiste rate.")
plt.plot(convulution)
plt.show()
