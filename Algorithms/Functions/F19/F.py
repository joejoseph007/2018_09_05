import random, sys, os, math, numpy
#Schaffer Function N4
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return 0.5+((numpy.cos(numpy.sin(numpy.fabs(x**2-y**2))))**2-0.5)/(1+0.001*(x**2+y**2))**2
#print run (0,1.25313)

def check(Arr,T,Z=[0]):
	xmax=100
	xmin=-100
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range

