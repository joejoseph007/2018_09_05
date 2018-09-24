import random, sys, os, math, numpy
#Three-hump camel function  
def run([x,y]):
	return 2*x**2-1.05*x**4+x**6/6+x*y+y**2


def check(Arr,T,Z=[0]):
	xmax=5
	xmin=-5
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range

