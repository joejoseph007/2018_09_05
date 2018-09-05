import random, sys, os, math, numpy
#Holder Table Function
def run(x,y):
	return -numpy.fabs(numpy.sin(x)*numpy.cos(y)*numpy.exp(1-numpy.sqrt(x**2+y**2)/numpy.pi))