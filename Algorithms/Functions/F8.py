import random, sys, os, math, numpy
#Cross in tray Function
def run(x,y):
	return -0.0001*((numpy.fabs(numpy.sin(x)*numpy.sin(y)*numpy.exp(numpy.fabs(100-numpy.sqrt(x**2+y**2)/numpy.pi)))+1)**0.1)