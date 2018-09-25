import random, sys, os, math, numpy
#McCormick function
def run(Arr):
	sum1=0	
	for i in range(len(X)):
		sum1=sum1+(Arr[i]**4-16*Arr[i]**2+5*Arr[i])/2
	return sum1

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

