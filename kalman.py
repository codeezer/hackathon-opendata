#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy
import pylab


# intial parameters
z = [300,400,500,500,600,700,500,600,500]
n_iter = len(z) 
sz = (n_iter,) # size of array

Q = 1e-2 # process variance

# allocate space for arrays
xhat=numpy.zeros(sz)      # a posteri estimate of x
P=numpy.zeros(sz)         # a posteri error estimate
xhatminus=numpy.zeros(sz) # a priori estimate of x
Pminus=numpy.zeros(sz)    # a priori error estimate
K=numpy.zeros(sz)         # gain or blending factor

R = 0.2**2 # estimate of measurement variance, change to see effect

# intial guesses
xhat[0] = z[0] 
P[0] = 50.0

for k in range(1,n_iter):
    # time update
    xhatminus[k] = xhat[k-1]
    Pminus[k] = P[k-1]+Q
    
    # measurement update
    K[k] = Pminus[k]/( Pminus[k]+R )
    xhat[k] = xhatminus[k]+K[k]*(z[k]-xhatminus[k])
    P[k] = (1-K[k])*Pminus[k]

pylab.figure()
pylab.plot(z,'k+',label='noisy measurements')
pylab.plot(xhat,'b-',label='a posteri estimate')
pylab.legend()
pylab.xlabel('Iteration')
pylab.ylabel('Voltage')

pylab.show()
print(xhat[-1])
