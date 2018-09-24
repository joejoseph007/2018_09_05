
import random, sys, os, math, numpy
#Rosenbrock function
def run(Arr):
	sum=0	
	for i in range(len(Arr)-1):
		sum=sum+100*(Arr[i+1]-Arr[i]**2)-(1-Arr[i])**2
	return sum

def check(Arr,T,Z=[0]):
	xmax=2**1000
	xmin=-2**1000
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range


