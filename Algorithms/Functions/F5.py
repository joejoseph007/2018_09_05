import random, sys, os, math, numpy
#Levi Function N13
def run(x,y):
	return (numpy.sin(3*numpy.pi*x))**2+((x-1)**2)*(1+(numpy.sin(3*numpy.pi*y))**2)+((y-1)**2)*(1+(numpy.sin(2*numpy.pi*y))**2)
