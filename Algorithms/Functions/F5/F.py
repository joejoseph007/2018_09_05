import random, sys, os, math, numpy
#Beale function
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return (1.5-x+x*y)**2+(2.25-x+x*y)**2+(2.625-x+xy**3)**2

def check(Arr,T,Z=[0]):
	xmax=4.5
	xmin=-4.5
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range


