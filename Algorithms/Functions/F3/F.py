import random, sys, os, math, numpy
#Ackley Function
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return -20*numpy.exp(-0.2*numpy.sqrt(0.5*(x**2+y**2)))-numpy.exp(0.5*(numpy.cos(2*numpy.pi*x)+numpy.cos(2*numpy.pi*y)))+numpy.e+20


def check(Arr,T,Z=[0]):
	xmax=50
	xmin=-50
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range


