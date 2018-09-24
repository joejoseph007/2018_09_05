import random, sys, os, math, numpy
#Cross in tray Function
def run([x,y]):
	return -0.0001*((numpy.fabs(numpy.sin(x)*numpy.sin(y)*numpy.exp(numpy.fabs(100-numpy.sqrt(x**2+y**2)/numpy.pi)))+1)**0.1)

def check(Arr,T,Z=[0]):
	xmax=10
	xmin=-10
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range

