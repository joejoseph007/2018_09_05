import random, sys, os, math, numpy
#Himmelblau's Function 
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return (x**2+y**2-11)**2+(x+y**2-7)**2

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

