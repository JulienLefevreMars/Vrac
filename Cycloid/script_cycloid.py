import numpy as np
import matplotlib.pyplot as plt

def generate_samples(R,a=0,period=1,N=1000):
	time_samples = np.linspace(0,2*period*np.pi,N)
	coordinates = np.stack([[R*time_samples - a*np.sin(time_samples)],[ R + a*np.cos(time_samples) ]],axis = 0)
	return time_samples, coordinates
	
 
t,c = generate_samples(1,1,2)
t2,c2 = generate_samples(1,0.6,2)
plt.plot(c[0,0,:].flatten(),c[1,0,:].flatten())
plt.plot(c2[0,0,:].flatten(),c2[1,0,:].flatten())
plt.show()
