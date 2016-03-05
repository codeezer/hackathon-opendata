#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy
import pylab
import test as t

# intial parameters
z = t.get_data()
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

estimate = int(xhat[-1])

pylab.figure()
pylab.plot(z,'k+',label='Feeded Data')
pylab.plot(xhat,'b-',label='Estimatation')

#pylab.plot(estimate,'',label='Doctors Required')
pylab.legend()
pylab.xlabel('Year')
pylab.ylabel('No. of Doctors Required')
pylab.title('No. of Doctors Required for year 2072 is : '+str(estimate))
pylab.show()
