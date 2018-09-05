import random, sys, os, math, numpy
#Griewank Function
def run(x,y):
	return (x**2 + y**2)/4000-numpy.cos(x/2**(0.5))*numpy.cos(y/2**(0.5))+1
