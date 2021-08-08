import numpy as np
import matplotlib.pyplot as plt
import imageio
import os

def generate_samples(R, a=0,period=1, N=100):
	time_samples = -np.pi/2 - np.linspace(0,2*period*np.pi,N)
	coordinates = np.stack([R*(-time_samples-np.pi/2) + a*np.cos(time_samples), R + a*np.sin(time_samples) ],axis = 0)
	return time_samples, coordinates
	
def draw_circle(R,shift):
	time_samples = np.linspace(0,2*np.pi,1000)
	coordinates = np.stack([R*np.cos(time_samples),shift+R*np.sin(time_samples)],axis = 0)
	return coordinates
	
def length_curve(coordinates):
	infinitesimal_length = np.sqrt(np.sum(np.diff(coordinates,axis = 1) **2 ,axis=0))
	return np.cumsum(infinitesimal_length)

# First step
t,c = generate_samples(1,1,2)
# t2,c2 = generate_samples(1,0.6,2)
# print(c)
# plt.figure()
# plt.plot(c[0,:].flatten(),c[1,:].flatten())
# plt.plot(c2[0,:].flatten(),c2[1,:].flatten())
#plt.show()

plt.plot(length_curve(c))
plt.show()

# Animation, gif file

R = 1
N = 100
period = 2
coordinates = draw_circle(1,1)
coordinates2 = draw_circle(0.6,1)
t,c = generate_samples(1,1,period,N)
length1=length_curve(c)
t2,c2 = generate_samples(1,0.6,period,N)
length2=length_curve(c2)
perimeter = 2*np.pi*period*R
filenames = []
for i in range(N-1):
	plt.plot( perimeter *i /N + coordinates[0,:], coordinates[1,:],'k')
	plt.plot( perimeter *i /N + coordinates2[0,:], coordinates2[1,:],'k')
	plt.plot(c[0,0:i],c[1,0:i],'r')
	plt.plot(c2[0,0:i],c2[1,0:i],'b')
	plt.plot(c[0,i],c[1,i],'.r')
	plt.plot(c2[0,i],c2[1,i],'.b')
	# Length
	plt.text(0,4*R,"Longueur = " + str(round(length1[i],2) ),color='r')
	plt.text(0,3*R,"Longueur = " + str(round(length2[i],2) ),color='b')
	plt.xlim([- R, perimeter + R])
	plt.gca().set_aspect('equal')
	filename = 'tmp/image_'+str(i)+'.png'
	filenames.append(filename)
	plt.savefig(filename)
	plt.close()
	
	
with imageio.get_writer('cycloid.gif', mode = 'I') as writer:
	for filename in filenames:
		image = imageio.imread(filename)
		writer.append_data(image)
		
for filename in set(filenames):
	os.remove(filename)
