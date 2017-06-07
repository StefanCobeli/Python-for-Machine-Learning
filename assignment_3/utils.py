import numpy,numpy.linalg

# Return the stationary distribution of a markov chain with transition matrix P
def getstationary(P):
    A = numpy.concatenate([(P.T - numpy.identity(8)),numpy.ones([1,8])],axis=0)
    b = numpy.array([0]*8+[1])
    return numpy.linalg.lstsq(A,b)[0]

# Performs a Markov chain transition for multiple particles in parallel
def mcstep(X,Ppad,seedval):
    Xp = numpy.dot(X,Ppad)
    Xc = numpy.cumsum(Xp,axis=1)
    L,H = Xc[:,:-1],Xc[:,1:]
    R = numpy.random.mtrand.RandomState(seedval).uniform(0,1,[len(Xp),1])
    return (R > L)*(R < H)*1.0

# Initial position of particles in the lattice
def getinitialstate():
	X = numpy.random.mtrand.RandomState(123).uniform(0,1,[1000,8])
	X = (X == numpy.max(X,axis=1)[:,numpy.newaxis])*1.0
	return X

