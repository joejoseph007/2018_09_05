import random, sys, os, math, numpy
#Rastrigin Function
def run(x,y):
	return 20+x**2 + y**2-10*(numpy.cos(numpy.pi*2*x)+numpy.cos(numpy.pi*2*y))
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