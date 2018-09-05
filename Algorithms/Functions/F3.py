import random, sys, os, math, numpy
#Ackley Function
def run(x,y):
	return -20*numpy.exp(-0.2*numpy.sqrt(0.5*(x**2+y**2)))-numpy.exp(0.5*(numpy.cos(2*numpy.pi*x)+numpy.cos(2*numpy.pi*y)))+numpy.e+20