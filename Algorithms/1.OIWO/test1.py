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


y = Pool()
y.map(Run_parallel,range(Popn))
y.close()
y.join()    


for i in range(len(Specie_List)):
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),1)

Iter+=1

while Iter<=Iter_max:

	Cost=Specie_List[0].Lists(Specie_List,1)

	Specie_List[0].Rank_Assign(Specie_List)
	Rank_List=Specie_List[0].Lists(Specie_List,2)
	print('Generation',Iter)
	print(Specie_List[0].X,Specie_List[0].Cost)

	#assign number of offspring and sigma
	for i in range(len(Specie_List)):
		ratio = (max(Rank_List)-Specie_List[i].Rank)/(max(Rank_List))
		S = int(Smin + (Smax - Smin)*ratio)
		sigma = (((Iter_max - float(Iter))/(Iter_max - 1))**Exponent )* (sigma_initial - sigma_final) + sigma_final
		sigma = (((Iter_max - float(Iter))/(Iter_max - 1))**Exponent )* (sigma_initial - sigma_final) + sigma_final
		sigma1=(((max(Rank_List) - float(Specie_List[i].Rank))/max(Rank_List))**Exponent1 )* (sigma_best - sigma_worst) + sigma_worst;
		sigma = sigma +sigma1
		Specie_List[i].Offspring=np.array([S,sigma])

	g=0
	for i in range(len(Specie_List)):
		S,sigma=int(Specie_List[i].Offspring[0]),Specie_List[i].Offspring[1]

		if S>0:
			for j in range(S):
				Specie_Offspring=Specie()

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

	Cost1=Specie_List[0].Lists(Specie_List1,1)

	xy=Specie_List[0].Lists(Specie_List,0)
	#print(xy)
	xy1=Specie_List[0].Lists(Specie_List1,0)

	
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	#plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	#plt.scatter(Cost[0],Cost[1])
	#print (xy1)

	delta = 1
	X = np.arange(-100.0, 100.0, delta)
	Y = np.arange(-100.0, 100.0, delta)
	x, y = np.meshgrid(X, Y)

	#Z=(X**2 + Y**2)/4000-np.cos(X/2**(0.5))*np.cos(Y/2**(0.5))+1
	#Z=-20*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*Y)))+np.e+20
	Z=0.5+((np.sin(x**2-y**2))**2-0.5)/(1+0.001*(x**2+y**2))**2
	#Z1 = np.exp(-X**2 - Y**2)
	#Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)

	#Z = (Z1 - Z2) * 2

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z,5,linewidths=0.3)
	
	#ax.clabel(CS, inline=1, fontsize=10)
	
	#ax.set_title('Simplest default with labels')
	plt.scatter(xy1[0],xy1[1],s=1.5,c='black')
	plt.scatter(xy[0],xy[1],s=3.5,c='blue')
	plt.scatter(xy[0][0],xy[1][0],s=10,c='red')
	plt.xlim(-100,100)
	plt.ylim(-100,100)
	
	#plt.show()

	plt.savefig('Pics/0/%i.0.svg'%Iter)
	plt.close()
	
	
	

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

