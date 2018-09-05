import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si



arr=[[1,2],[2,3],[3,4]]


class Specie(object):

	def Cost_run(self,I,J,out):
		#print(I**2,J**2)
		T_start=time.time()-Time
		#print('parent process\t', os.getppid())
		r=random.randrange(0,100)
		time.sleep(r/50)
		#print('process \t', os.getpid())
		T_end=time.time()-Time
		out.put((I,r,T_start,T_end))
		algeb=1234*1234
		
		#return I

Time=time.time()
multiprocessing.set_start_method('fork')

out=multiprocessing.Queue()
p=[multiprocessing.Process(target=Specie.Cost_run,args=(i,i*i,out)) for i in range(100)]

for j in p:
	j.start() 
	#print ('Start')

for j in p:
	j.join() 
	#print ('End')


print('Time\t\t%.4f'%(time.time()-Time))

z=[out.get()for i in range(len(p))]
z1=np.array(z)

#z.sort(key=1)
#z1=np.sort(z1,axis=0)
print (z1)

for i in range(len(z1)):
	plt.plot([z1[i][2],z1[i][3]],[i,i],'ro-')
	
#plt.show()
plt.close()

Time_lag=[z1[i][3]-z1[i][2]-3 for i in range(len(z1))]
plt.plot([i for i in (z1)],Time_lag)
#plt.show()

print ("TIME",time.time()-Time)


#print(p)
#p.start()
#p.join()
'''
ypool= multiprocessing.Pool()
result = ypool.map(Cost_run,arr)
ypool.close()
ypool.join()
'''


#Cost=[[0],[0]]
        #Cost[0]=[Spc[i].Cost[0] for i in range(len(Spc))]
        #Cost[1]=[Spc[i].Cost[1] for i in range(len(Spc))]
        