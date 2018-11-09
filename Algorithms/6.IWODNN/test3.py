import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil,copy
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *
from Specie import *





Specie_List=[]
for i in range(10):
    A=Specie()
    #Specie_List.append(Specie())
    #Specie_List[i].X=np.random.random([Row,Col])*100
    #Specie_List[i].New(0)
    A.New(0)
    B=copy.deepcopy(Specie())
    #B.New(0)
    Specie_List.append(B)
    Specie_List[i].New(0)

for i in range(len(Specie_List)):
    print(Specie_List[i].X)


