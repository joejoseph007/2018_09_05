import random, sys, os, math, numpy
#Goldstein–Price function
def run([x,y]):
	a=(1+((x+y+1)**2)*(19-14*x+3*x**2-14*y+6*x*y+3*y**2))
	b=(30+((2*x-3*y)**2)*(18-32*x+12*x**2+48*y-36*x*y+27*y**2))
	return a*b

def check(Arr,T,Z=[0]):
	xmax=2
	xmin=-2	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range


