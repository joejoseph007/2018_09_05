import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *

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
print(X)
print(Z)

print(Z[0])
print(A)


T=np.zeros(2)
T=np.array([1.2,0.90123])
print('T',T)