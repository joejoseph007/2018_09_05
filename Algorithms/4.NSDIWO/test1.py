import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si


from mpl_toolkits.mplot3d import axes3d

Time=time.time()


from Constants import *
from NSGA2 import *
from Specie import *

global Specie_List,sigma
Specie_List=[]


#if __name__ == "__main__":




#Generation 0 // Uniformly random
for i in range(Popn):	
	Spc=Specie()
	#Specie_List.append(Spc.New())
	Specie_List[i].New(0)
Iter+=1





def Run_parallel(i):
	global Iter,Specie_List
	
	Specie_List1=[]#Specie_List
	#sigma=0.5/Iter**0.5
	Specie_List1.append(Specie(Specie_List[i].X))
	
	if Iter ==0:
		Specie_List[i].Cost_run(Results_Directory %(Iter,i))
		Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)
		
	else:
		Specie_List1[0].New(1,Specie_List[i].Offspring[1])
		
		Specie_List1[0].Cost_run(Results_Directory %(Iter,i))
		Specie_List1[0].Read_Write(Results_Directory %(Iter,i),0)
		
	return Specie_List1[0].X,Specie_List1[0].Cost#Roundoff(Specie_List1[0].X),Roundoff(Specie_List1[0].Cost)
  

Specie_List[0].Rank_Assign(Specie_List)


while Iter<=Iter_max:
	#import F
	#print(Iter)
	#for i in range(len(Specie_List)):
	
	    
	#sigma=0.5/Iter**0.5
	
	
	print('Generation',Iter)
	print(Specie_List[0].X,Specie_List[0].Cost)

	Cost=Specie_List[0].Lists(Specie_List,1)
	Rank_List=Specie_List[0].Lists(Specie_List,2)
	Specie_List[0].Rank_Assign(Specie_List)

	#assign number of offspring and sigma
	for i in range(len(Specie_List)):
		ratio = (max(Rank_List)-Specie_List[i].Rank)/(max(Rank_List))
		S = int(Smin + (Smax - Smin)*ratio)
		sigma = (((Iter_max - float(Iter))/(Iter_max - 1))**Exponent )* (sigma_initial - sigma_final) + sigma_final
		sigma1=(((max(Rank_List) - float(Specie_List[i].Rank))/max(Rank_List))**Exponent1 )* (sigma_best - sigma_worst) + sigma_worst;
		sigma = sigma +sigma1
		Specie_List[i].Offspring=np.array([S,sigma])
		#print(Specie_List[i].Rank,Specie_List[i].Offspring)
	
	#plt.close()

	#print(NDSa)
	
    
	y = Pool()
	Results = y.map(Run_parallel,range(Popn2))
	y.close()
	y.join()    
    






	
	Specie_List1=[]#Specie_List
	
	for i in range(len(Results)):
		Specie_List1.append(Specie(Results[i][0],Results[i][1]))


	Specie_List1=Specie_List+Specie_List1




	Cost1=Specie_List[0].Lists(Specie_List1,1)
	#'''
	xy=Specie_List[0].Lists(Specie_List,0)
	xy1=Specie_List[0].Lists(Specie_List1,0)

	
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	#plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	#plt.scatter(Cost[0],Cost[1])
	#print (xy1)
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(xy1[0],xy1[1],xy1[2],s=1.5,c='black')
	ax.scatter(xy[0],xy[1],xy[2],s=1.5,c='black')
	plt.ylim(-2,2)
	plt.xlim(-2,2)
	#plt.zlim(-2,2)
	#plt.zlim(-10,10)
	
	#plt.scatter(xy1[0],xy1[1],s=1.5,c='black')
	#plt.scatter(xy[0],xy[1],s=3.5,c='blue')
	

	plt.savefig('Pics/0/%i.0.svg'%Iter)
	plt.close()
	#'''
	#F1
	#plt.ylim(-60,10)
	#plt.xlim(-140,10)
	
	#F5
	plt.ylim(-14,14)
	plt.xlim(4,20)


	#F11
	#plt.ylim(-5,0)
	#plt.xlim(-1.2,0.1)


	#F13
	#plt.ylim(-10,9)
	#plt.xlim(-1.1,-0.8)

	#F16
	#plt.ylim(-10,0)
	#plt.xlim(-1,0)



	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	plt.scatter(Cost1[0],Cost1[1],s=1.5,c='black')
	plt.scatter(Cost[0],Cost[1],s=3.5,c='blue')
	plt.savefig('Pics/1/%i.1.svg'%Iter)
	plt.close()

	#'''

	Rank_List=Specie_List[0].Rank_Assign(Specie_List1)

	Specie_List = [Specie_List1[i] for i in Rank_List]

	
	Iter+=1
