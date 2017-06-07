import numpy,random

# Produces a toy dataset for testing
def toy(M,N,d):
	U = numpy.random.mtrand.RandomState(123).uniform(0,1,[M,d]) # test points
	X = numpy.random.mtrand.RandomState(456).uniform(0,1,[N,d]) # training points
	Y = numpy.random.mtrand.RandomState(789).randint(0,2,[N])   # training labels
	return U,X,Y

# A small handwritten digits dataset
def digits():
	from sklearn.datasets import load_digits
	d=load_digits()
	R = numpy.random.mtrand.RandomState(159).permutation(len(d.data))
	return d.data[R]*1,d.target[R]*1

