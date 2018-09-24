import random, sys, os, math, numpy
#Eggholder Function
def run([x,y]):
	return -(y+47)*numpy.sin(numpy.sqrt(numpy.fabs(x/2+y+47)))-x*numpy.sin(numpy.sqrt(numpy.fabs(x-y-47)))
#print run(512,404.2319)


def check(Arr,T,Z=[0]):
	xmax=512
	xmin=-512
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range

