import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *
from Specie import *



Specie_List=[]
Specie_List.append(Specie.New(0,0))
Specie_List1=Specie()
Specie_List1.New(0,0)
Specie_List[0].New(0,0)


'''
Row=2
Col=3

Z=[]
A=np.array([])
for i in range(3):
    X=np.random.rand(Row,Col)*100
    X=np.round(X,1)
    Z.append(X.tolist())
    #np.append(A,X)
    #print(A)
#print(X)
#print(Z)

#print(Z[0])
#print(A)

min1=100
max1=200

Range=[[[275,150,100],[100,250,150]],[[300,200,300],[300,300,200]]]

Range=np.array(Range)

X=np.random.rand(Row,Col)*(Range[1]-Range[0])+Range[0]
sigma=0.5
X1=np.random.normal(0,sigma,(Row,Col))*(Range[1]-Range[0])+X

#X=np.round(X,3)
print(X)
print(X1)
#print(Range[0])

'''