import random, sys, os, math, numpy
#McCormick function
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return math.sin(x+y)+(x-y)**2-1.5*x+2.5*y+1

def check(Arr,T,Z=[0]):
	xmax=4
	xmin=-1.5
	ymax=4
	ymin=-3
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		Range[0][0][0]=xmin
		Range[0][1][0]=ymin
		Range[0][0][1]=xmax
		Range[0][1][1]=ymax
		return Range

