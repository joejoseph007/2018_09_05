import random, sys, os, math, numpy
#Schaffer Function N2
def run(x,y):
	return 0.5+((numpy.sin(x**2-y**2))**2-0.5)/(1+0.001*(x**2+y**2))**2
#print run (0,0)