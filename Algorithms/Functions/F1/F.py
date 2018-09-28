import random, sys, os, math, numpy
#Griewank Function
def run(Arr):
	x=Arr[0]
	y=Arr[1]
	return (x**2 + y**2)/4000-numpy.cos(x/2**(0.5))*numpy.cos(y/2**(0.5))+1

def check(Arr,T,Z=[0]):
	xmax=600
	xmin=-600
	ymax=600
	ymin=-600
	
	if T==0:
		return 1

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		Range[0][0][0]=xmin
		Range[0][1][0]=ymin
		Range[0][0][1]=xmax
		Range[0][1][1]=ymax
		Range[1][0][0]=xmin
		Range[1][1][0]=ymin
		Range[1][0][1]=xmax
		Range[1][1][1]=ymax
		
		return Range


#print(run([-10,10]))