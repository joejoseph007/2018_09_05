import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *
from Specie import *


'''
Specie_List=[]
Specie_List.append(Specie.New(0,0))
Specie_List1=Specie()
Specie_List1.New(0,0)
Specie_List[0].New(0,0)
'''
def takeSecond(elem):
    return elem[1]


'''
a=[10,9,8,7,6,5,4,3,2,1,1,2,3,4,5,6,7,8,9,0]

b=[[i,a[i]]for i in range(len(a))]

print (b)


c=sorted(b,key=takeSecond)#Specie.Cost_run('Pics')


print (c)

'''

z=[2,3,4,5,6,7,8,9,10]


sigma=0.5

'''
while 1:
    T=random.random()*10
    time.sleep(1)
    print(T)
    for i in range(len(z)):
        print("Range",z[i]-sigma,z[i]+sigma)
        if T<=z[i]+sigma and T>=z[i]-sigma: 
            print(i)            
'''
qwe1=[]
for qwe in range(100):
    while 1:
        t=1
        T=random.random()*10
        for i in range(len(z)):
            if (T>=z[i]-sigma and T<=z[i]+sigma):
                t=0
                break       
        if t==1:
            break
    qwe1.append(T)
    print(T)

#plt.plot(qwe1)
#plt.show()


print(len([]))

'''
T=-1

if T>z[i] for i in range(len(z)):
    print(T) 

'''

'''
delta = 5
X = np.arange(-600.0, 600.0, delta)
Y = np.arange(-600.0, 600.0, delta)
x, y = np.meshgrid(X, Y)

#Z=(X**2 + Y**2)/4000-np.cos(X/2**(0.5))*np.cos(Y/2**(0.5))+1
#Z=-20*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*Y)))+np.e+20
Z=-(y+47)*np.sin(np.sqrt(np.fabs(x/2+y+47)))-x*np.sin(np.sqrt(np.fabs(x-y-47)))
#Z1 = np.exp(-X**2 - Y**2)
#Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)

#Z = (Z1 - Z2) * 2

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z,50)
#ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')
'''
#plt.show()


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