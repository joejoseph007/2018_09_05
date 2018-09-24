import random, sys, os, math, numpy
#Rastrigin Function
def run(Arr):
	sum=0	
	for i in range(len(Arr)):
		sum=sum+(Arr[i]-math.cos(2*math.pi*Arr[i]))
	return sum+10

def check(Arr,T,Z=[0]):
	xmax=5.12
	xmin=-5.12
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range


'''
#!/usr/bin/env python
# coding: utf-8

"""
https://en.wikipedia.org/wiki/Rastrigin_function
Non-convex function for testing optimization algorithms.
"""

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import math
import matplotlib.pyplot as plt
import numpy as np

def rastrigin(*X, **kwargs):
    A = kwargs.get('A', 10)
    return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])

if __name__ == '__main__':
    X = np.linspace(-4, 4, 200)    
    Y = np.linspace(-4, 4, 200)    

    X, Y = np.meshgrid(X, Y)

    Z = rastrigin(X, Y, A=10)

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False)    

plt.savefig('rastrigin.png')
'''
