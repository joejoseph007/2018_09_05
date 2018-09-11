import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree

Row=1
Col=2
Func=2

def randf(r,c,min1,max1):
	R=np.zeros((r,c))
	for i in range(len(R)):
		for j in range(len(R[0])):
			R[i][j]=random.uniform(min1,max1)
	#random.choice()
	return R

sys.path.append("../Multiobjective_Functions")
import F1
    


def Cost(X):
    return F1.run(X)
	



#X1=randf(Row,Col,-10,10)


def Range_chk_slic(X,T):
	#sys.path.append("../Multiobjective_Functions")
	#import F16
	
	if T==0:
		if F1.check(X,T):
			return 1
		else: 
			return 0
	if T==1:
		Range=F1.check(X,T,[Row,Col])
		for i in range(len(X)):
			for j in range(len(X[0])):
				X[i][j]=max(X[i][j],Range[i][j][0])
				X[i][j]=min(X[i][j],Range[i][j][1])

def new(mu,sigma):	
	X=np.zeros((Row,Col))
	while 1:
		#print("here",self.X)
		X=X+np.random.normal(mu,sigma,(len(X),len(X[0])))
		Range_chk_slic(X,1)
		if Range_chk_slic(X,0):
			return X[0]
			break


Row1=10
A=np.zeros((Row1,Col))
for i in range(Row1):
	A[i]=(new(2,0.1))

print(A)