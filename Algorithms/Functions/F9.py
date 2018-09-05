import random, sys, os, math, numpy
#Eggholder Function
def run(x,y):
	return -(y+47)*numpy.sin(numpy.sqrt(numpy.fabs(x/2+y+47)))-x*numpy.sin(numpy.sqrt(numpy.fabs(x-y-47)))
#print run(512,404.2319)