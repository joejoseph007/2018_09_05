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

global Specie_List,sigma,Obj_call

Specie_List=[]
Obj_call=0


def Run_parallel(i):
	global Iter,Obj_call
	Specie_List1=Specie()#Specie_List
	Specie_List1.Read_Write(Results_Directory %(Iter,i),1)
	Specie_List1.Cost_run(Results_Directory %(Iter,i))
	Specie_List1.Read_Write(Results_Directory %(Iter,i),0)
	Obj_call+=1
	return Specie_List1.X,Specie_List1.Cost#Roundoff(Specie_List1[0].X),Roundoff(Specie_List1[0].Cost)



#Generation 0 // Uniformly random
for i in range(Popn):	
	Specie_List.append(Specie())
	Specie_List[i].New(0)
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)



#time.sleep(100)
y = Pool()
y.map(Run_parallel,range(Popn))
#Results = y.map(Run_parallel,range(Popn))
y.close()
y.join()    


for i in range(len(Specie_List)):
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),1)
	
	#Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)
	#print (Specie_List[i].X,Specie_List[i].Cost)


'''
for i in range(len(Specie_List)):
	print(Specie_List[i].X,Specie_List[i].Cost,Specie_List[i].Rank)
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)
	
	#Specie_List[i].Read_Write(Results_Directory %(Iter,i),0)
	#print (Specie_List[i].X,Specie_List[i].Cost)
'''

Iter+=1

while Iter<=Iter_max:
	#import F
	#print(Iter)
	#for i in range(len(Specie_List)):

	Cost=Specie_List[0].Lists(Specie_List,1)
	Specie_List[0].Rank_Assign(Specie_List)
	Rank_List=Specie_List[0].Lists(Specie_List,2)
	
	    
	#sigma=0.5/Iter**0.5
	
	
	print('Generation',Iter)
	print(Specie_List[0].X,Specie_List[0].Cost)

	#assign number of offspring and sigma
	for i in range(len(Specie_List)):
		ratio = (max(Rank_List)-Specie_List[i].Rank)/(max(Rank_List))
		S = int(Smin + (Smax - Smin)*ratio)
		#print (S)
		sigma = (((Iter_max - float(Iter))/(Iter_max - 1))**Exponent )* (sigma_initial - sigma_final) + sigma_final
		sigma1=(((max(Rank_List) - float(Specie_List[i].Rank))/max(Rank_List))**Exponent1 )* (sigma_best - sigma_worst) + sigma_worst;
		sigma = sigma +sigma1
		Specie_List[i].Offspring=np.array([S,sigma])
		
		#print(Specie_List[i].Rank,Specie_List[i].Offspring)
	
	#plt.close()

	#print(NDSa)
	#print(len(Specie_List))

	g=0
	for i in range(len(Specie_List)):
		S,sigma=int(Specie_List[i].Offspring[0]),Specie_List[i].Offspring[1]
		#print('S',S)
		if S>0:
			for j in range(S):
				Specie_Offspring=Specie()
				#print(Specie_List[i].X)
				Specie_Offspring.New(1,Specie_List[i].X,sigma)
				Specie_Offspring.Read_Write(Results_Directory %(Iter,g),0)
				g+=1
    


	
	y = Pool()
	Results = y.map(Run_parallel,range(g))
	y.close()
	y.join()    
    
	





	
	Specie_List1=[]#Specie_List
	
	for i in range(len(Results)):
		Specie_List1.append(Specie(Results[i][0],Results[i][1]))
		Specie_List1[i].Read_Write(Results_Directory %(Iter,g),0)



	Specie_List1=Specie_List+Specie_List1
	
	#print(g)
	#print(len(Specie_List))
	#print(len(Specie_List1))

	Cost1=Specie_List[0].Lists(Specie_List1,1)
	#print('Here')
	#print(len(Specie_List))
	#'''
	
	xy=Specie_List[0].Lists(Specie_List,0)
	#print(xy)
	xy1=Specie_List[0].Lists(Specie_List1,0)

	
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	#plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	#plt.scatter(Cost[0],Cost[1])
	#print (xy1)
	'''
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(xy1[0],xy1[1],xy1[2],s=1.5,c='black')
	ax.scatter(xy[0],xy[1],xy[2],s=1.5,c='black')
	plt.ylim(-2,2)
	plt.xlim(-2,2)
	#plt.zlim(-2,2)
	#plt.zlim(-10,10)
	'''

	

	
	
	plt.scatter(xy1[0],xy1[1],s=1.5,c='black')
	plt.scatter(xy[0],xy[1],s=3.5,c='blue')
	
	plt.xlim(-10,10)
	plt.ylim(-10,10)
	
	plt.savefig('Pics/0/%i.0.svg'%Iter)
	plt.close()
	#'''
	#'''
	#F1
	#plt.ylim(-60,10)
	#plt.xlim(-140,10)
	
	plt.ylim(-10,60)
	plt.xlim(-10,140)
	
	#F5
	#plt.ylim(-14,14)
	#plt.xlim(4,20)


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
	#'''
	plt.scatter(Cost1[0],Cost1[1],s=1.5,c='black')
	plt.scatter(Cost[0],Cost[1],s=3.5,c='blue')
	plt.savefig('Pics/1/%i.1.svg'%Iter)
	plt.close()
	#'''
	
	
	'''
	
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.scatter(Cost1[0],Cost1[1],Cost1[2],s=1.5,c='black')
	ax.scatter(Cost[0],Cost[1],Cost[2],s=1.5,c='black')
	plt.xlim(-17,-14)
	plt.ylim(-8,0)
	plt.savefig('Pics/1/0.%i.svg'%Iter)
	plt.close()
	

	plt.scatter(Cost1[0],Cost1[1],s=1.5,c='black')
	plt.scatter(Cost[0],Cost[1],s=3.5,c='blue')
	plt.xlim(-17,-14)
	plt.ylim(-8,0)
	plt.savefig('Pics/1/1.%i.svg'%Iter)
	plt.close()
	
	
	plt.scatter(Cost1[1],Cost1[2],s=1.5,c='black')
	plt.scatter(Cost[1],Cost[2],s=3.5,c='blue')
	plt.xlim(-8,0)
	plt.ylim(-0.2,0.2)
	plt.savefig('Pics/1/2.%i.svg'%Iter)
	plt.close()
	
	plt.scatter(Cost1[2],Cost1[0],s=1.5,c='black')
	plt.scatter(Cost[2],Cost[0],s=3.5,c='blue')
	plt.ylim(-17,-14)
	plt.xlim(-0.2,0.2)
	plt.savefig('Pics/1/3.%i.svg'%Iter)
	plt.close()
	
	'''
	Rank_List=Specie_List[0].Rank_Assign(Specie_List1)

	Specie_List = [Specie_List1[i] for i in Rank_List]

	del Specie_List[Popn2:]

	Cost=Specie_List[0].Lists(Specie_List,1)

	Rank_List=Specie_List[0].Lists(Specie_List,2)
	Specie_List[0].Rank_Assign(Specie_List)

	for i in range(len(Specie_List)):
		#Specie_List[i].Cost=Results[i][1]
		Specie_List[i].Read_Write(Parent_Directory %(Iter,i),0)


	Iter+=1




thefile = open('FinalCalls', 'w')
thefile.write("%i" %Obj_call)
thefile.close()    

