import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree

Row=10
Col=2
Func=2

def randf(r=1,c=1):
	R=np.zeros((r,c))
	for i in range(len(R)):
		for j in range(len(R[0])):
			R[i][j]=random.uniform(-5,5)
	#random.choice()
	return R


X=np.zeros((Row,Col))

def Cost(X):
    sys.path.append("../Multiobjective_Functions")
    import F1
    return F1.run(X[0])
	



X1=randf(Row,Col)

print(X1)