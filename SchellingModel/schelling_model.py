import numpy as np
import matplotlib.pyplot as plt
import sys

def initial_config(size = 50):
	return np.random.randn(size,size)<0
	
def index_to_coord(ind,nrows,ncols):
	i = ind//ncols
	j = ind-i*ncols
	return (i,j)
	
def mirroir(I,i,j,m,n):
	if i<0:
		i = m + i
	if i>=m:
		i = i-m
	if j<0:
		j = n + j
	if j>=n:
		j = j-n
	return I[i,j]

	
def number_same_neighbors(I,coord,m,n):
	(i,j) = coord
	somme = 0
	for k in range(-1,2):
		for l in range(-1,2):
			if (k!=0 and j!=0):
				somme += mirroir(I,i+k,j+l,m,n)
	return somme
		
		
def satisfaction(s,val,T=8):
	if val == 0:
		if s == T:
			return False
		if s>=4:
			return False
		return True
	return satisfaction(T-s,0)


def one_move(I,T):
	(m,n)=I.shape
	indices = np.random.permutation(m*n)
	ind0 = indices[0]
	ind1 = indices[1]
	(i0,j0)=index_to_coord(ind0,m,n)
	(i1,j1)=index_to_coord(ind1,m,n)
	# Recompute 
	#s0 = number_same_neighbors(I,(i0,j0),m,n)
	s1 = number_same_neighbors(I,(i1,j1),m,n)
	# Accept the move or not
	if satisfaction(s1, I[i0,j0],T):	
		# move
		tmp = I[i0,j0]
		I[i0,j0] = I[i1,j1]
		I[i1,j1] = tmp
		

if __name__ == "__main__":
	I = initial_config(size = 50)
	if len(sys.argv)==1:
		N=100
	if len(sys.argv)==2:
		N = int(sys.argv[1])
	plt.figure()
	plt.subplot(1,2,1)
	plt.imshow(I)
	for iter in range(N):
		one_move(I,8)
	plt.subplot(1,2,2)
	plt.imshow(I)
	plt.show()
	
