import random, sys, os, math, numpy
#Bukin function N.6
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return 100*(numpy.fabs(y-0.01*x**2))**0.5+0.01*numpy.fabs(x+10)
	 
def check(Arr,T,Z=[0]):
	xmax=-5
	xmin=-15
	ymax=3
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


