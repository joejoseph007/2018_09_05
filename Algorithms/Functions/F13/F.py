import random, sys, os, math, numpy
#Easom Function
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return -numpy.cos(x)*numpy.cos(y)*numpy.exp(-((x-numpy.pi)**2+(y-numpy.pi)**2))

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


#print run (numpy.pi,numpy.pi)
