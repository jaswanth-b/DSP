import numpy as np
import matplotlib.pyplot as plt
x=[1,2,3,4]
def cycle_delay(x,m):
	y=np.roll(x,m)
	return y
X=cycle_delay(x,3)
print(X)
