import random, sys, os, math, numpy
#Levi Function N13
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return (numpy.sin(3*numpy.pi*x))**2+((x-1)**2)*(1+(numpy.sin(3*numpy.pi*y))**2)+((y-1)**2)*(1+(numpy.sin(2*numpy.pi*y))**2)

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

