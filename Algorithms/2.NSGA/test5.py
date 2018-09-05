import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si


sigma =1
mu=100


z=np.random.normal(mu,sigma,100000)

x=np.random.normal(z,sigma,100000)

y=np.random.normal(100,sigma,100000)

print (np.mean(z),np.std(z))
print (np.mean(x),np.std(x))
print (np.mean(y),np.std(y))

#a=np.random.rand(2,4)*mu   #randf(len(self.X),len(self.X[0]
a=np.ones((2,4))
b=np.random.normal(0,sigma,(len(a),len(a[0])))
a1=a+b
a2=a*b

c=np.random.normal(mu,sigma,1)

print (a)
print (a1)
print(b)
print(a2)
'''
plt.plot(a[0],a[1])
plt.plot(a1[0],a1[1])

plt.show()
'''
'''

plt.scatter(z,[0 for i in range(len(z))])
plt.scatter(x,[1 for i in range(len(z))])
plt.show()


count,bins,ignored=plt.hist(z,100)
#plt.xlim(-100,100)
plt.plot(bins,10/sigma*np.sqrt(2*np.pi)*np.exp(-(bins-mu)**2/(2*sigma**2)))
#plt.scatter(z,[1 for i in range(len(z))],s=3,c='black')
plt.show()
'''