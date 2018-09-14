import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si




Time=time.time()


from Constants import *
from NSGA2 import *
from Specie import *

global Specie_List,sigma


#if __name__ == "__main__":



Specie_List=[]

#Generation 0 // Uniformly random
  
for i in range(Popn):	
	Specie_List.append(Specie())
	#print ("here")
	Specie_List[i].New(0)
	#Specie_List[i].New(5)
	Specie_List[i].Cost_run(Results_Directory %(Iter,i))
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)
Iter+=1

Specie_List[0].Rank_Assign(Specie_List)


while Iter<=Iter_max:

	#print(Iter)
	#for i in range(len(Specie_List)):
	sigma=1/Iter**0.5
	print(Iter,sigma)
	print(Specie_List[0].X,Specie_List[0].Cost)

	Cost=Specie_List[0].Lists(Specie_List,1)

	#plt.close()

	#print(NDSa)


	def Run_parallel(i):
		global Iter,Specie_List
		
		Specie_List1=[]#Specie_List
		sigma=1/Iter**0.5
		Specie_List1.append(Specie(Specie_List[i].X))
		Specie_List1[0].New(1,sigma)
		Specie_List1[0].Cost_run(Results_Directory %(Iter,i))
		Specie_List1[0].Read_Write(Results_Directory %(Iter,i),0)
		
		return Specie_List1[0].X,Specie_List1[0].Cost
    
	y = Pool(Popn2)
	Results = y.map(Run_parallel,range(Popn2))
	y.close()
	y.join()    
    
	Specie_List1=[]#Specie_List
	
	for i in range(len(Results)):
		Specie_List1.append(Specie(Results[i][0],Results[i][1]))


	Specie_List1=Specie_List+Specie_List1




	Cost1=Specie_List[0].Cost_list(Specie_List1)
	#'''
	xy=Specie_List[0].XY_list(Specie_List)
	xy1=Specie_List[0].XY_list(Specie_List1)

	
	plt.ylim(-10,10)
	plt.xlim(-10,10)
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	#plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	#plt.scatter(Cost[0],Cost[1])

	plt.scatter(xy1[0],xy1[1],s=1,c='black')
	plt.scatter(xy[0],xy[1],s=15,c='blue')
	

	plt.savefig('Pics/0/%i.0.svg'%Iter)
	plt.close()
	#'''
	#F1
	#plt.ylim(-60,10)
	#plt.xlim(-140,10)
	
	#F16
	#plt.ylim(-10,0)
	#plt.xlim(-1,0)

	#F5
	#plt.ylim(-10,14)
	#plt.xlim(0,20)

	#F11
	plt.ylim(-5,5)
	plt.xlim(-2,2)
	
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	plt.scatter(Cost[0],Cost[1],s=15,c='blue')
	plt.savefig('Pics/1/%i.1.svg'%Iter)
	plt.close()

	#'''

	NDSa1=fast_non_dominated_sort(Cost1[0],Cost1[1])

	CDv1=[]
	for i in range(0,len(NDSa1)):
		CDv1.append(crowding_distance(Cost1[0],Cost1[1],NDSa1[i][:]))



	Specie_List2=[]

	for i in range(0,len(NDSa1)):
		NDSa2 = [index_of(NDSa1[i][j],NDSa1[i] ) for j in range(0,len(NDSa1[i]))]
		front22 = sort_by_values(NDSa2[:], CDv1[i][:])
		front = [NDSa1[i][front22[j]] for j in range(0,len(NDSa1[i]))]
		front.reverse()
		#print(front)
		for value in front:
			Specie_List2.append(value)
			if(len(Specie_List2)==Popn3):
				break
		if (len(Specie_List2) == Popn3):
			break

	#Specie_List =[]
	#print(Specie_List2)
	Specie_List = [Specie_List1[i] for i in Specie_List2]


	Iter+=1
