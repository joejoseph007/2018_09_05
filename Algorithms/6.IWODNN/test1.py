import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil,copy
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from threading import Thread as Th
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
	Specie_List1.Read_Write(Results_Directory %(Iter,i),'r')
	Specie_List1.Cost_run(Results_Directory %(Iter,i))
	Specie_List1.Read_Write(Results_Directory %(Iter,i),'w')
	Obj_call+=1
	return Specie_List1.X,Specie_List1.Cost#Roundoff(Specie_List1[0].X),Roundoff(Specie_List1[0].Cost)



def Ann(Specie_List,t):
	import ArtiNN
	Genes=[];	Cost=[]
	i=0;j=0
	while j<=Iter:
		while 1:
			try:
				Sp=Specie()
				if t==0:
					Sp.Read_Write(Results_Directory %(j,i),'r')
				if t==1:
					Sp=Specie_List[i]
				Genes.append(Sp.X)
				Cost.append(Sp.Cost)
				i+=1
				continue
			except:
				break
		j+=1
	Genes1=np.array([i for i in Genes])
	Cost1=np.array([i for i in Cost])
	#print(Genes1)
	if t==0:
		#print(Cost1)
		ArtiNN.Deep_neural_net(Genes1,Cost1,'T')
	if t==1:	
		return ArtiNN.Deep_neural_net(Genes1,Cost1,'P',Genes1)	


#Generation 0 // Uniformly random

for i in range(Popn):
	B=copy.deepcopy(Specie())
	Specie_List.append(B)
	Specie_List[i].New(0)
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),'w')
	

'''
A=Specie()
for i in range(Popn):	
	
	
	A.New(0)
	A.Read_Write(Results_Directory %(Iter,i),'w')
	B=copy.deepcopy(A)
	Specie_List.append(B)
	
	for j in range(len(Specie_List)):
		print(Specie_List[j].X)
	print('====')
	#if i>=Popn/2:
	#	break
	#print(Specie_List[i].X)
'''

#sys.exit()


#Cost_Evaluation
y = Pool()
Results=y.map(Run_parallel,range(Popn))
y.close()
y.join()    


#Write the results  
for i in range(len(Specie_List)):
	#Specie_List[i].Cost=Results[i][1]
	Specie_List[i].Read_Write(Results_Directory %(Iter,i),'r')
	#print(Specie_List[i].X,Specie_List[i].Cost)

#sys.exit()

#ANN 1st Training on a parallel thread to save computational time
#Training_thread=Th(target = Ann, args = (Specie_List,0))
#Training_thread.start()
#Can be done without threads 
#Ann(Specie_List,0)

#sys.exit() #To force terminate the program 
print('Generation',Iter)
print(Specie_List[0].X,Specie_List[0].Cost)


Iter+=1

while Iter<=Iter_max:
	Ann(Specie_List,0)
	
	
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


	#Training_thread.join()
	Specie_Offspring_List=[]
	a=[]
	g=0
	for i in range(len(Specie_List)):
		S=int(Specie_List[i].Offspring[0])
		sigma=Specie_List[i].Offspring[1]
		if S>0:
			for j in range(S):
				B=copy.deepcopy(Specie())
				Specie_Offspring_List.append(B)
				Specie_Offspring_List[g].New(1,Specie_List[i].X,sigma)
				#Specie_Offspring_List[g].Read_Write(Prediction_Directory %(Iter,g),'w')				
				#a.append(Specie())
				#a[g].New(1,Specie_List[i].X,sigma)
				#print(a[g].X)
				#print(i,Specie_Offspring_List[i].X)
				#Specie_Offspring_List.append(Specie(Specie_Offspring.X,Specie_Offspring.Cost))
				#del Specie_Offspring
				#print(i,j,Specie_Offspring.X)
				#print(Specie_List[i].X)
				#Specie_Offspring.Read_Write(Results_Directory %(Iter,g),'w')
				g+=1
	#print(g)
	#print(Specie_Offspring_List)
	#print(a[2].X)
	
	#for t in range(g):
		#continue
		#print(a[t].X,a[t].Cost)
		#print(t,Specie_Offspring_List[t].X,Specie_Offspring_List[t].Cost)
	
	#sys.exit()

	Predictions=Ann(Specie_Offspring_List,1)
	
	
	
	#'''
	#sys.exit()
	Specie_Offspring_List1=copy.deepcopy(Specie_Offspring_List)
	Check=[]
	for i in range(len(Specie_Offspring_List1)):
		Specie_Offspring_List1[i].Cost_run('qwe')
		Check.append(Specie_Offspring_List1[i].Cost)	
	
		#print(Specie_Offspring_List1[i].X)
		#print(Specie_List[i].X)
	
	plt.plot(Predictions)
	plt.plot(Check)
	plt.show()
	sys.exit()
	#'''
	
	for i in range(len(Predictions)):
		Specie_Offspring_List[i].Cost=Predictions[i]
	





	Rank_List=Specie_List[0].Rank_Assign(Specie_Offspring_List)
	Specie_List1 = [Specie_Offspring_List[i] for i in Rank_List]
	
	del Specie_List1[Popn1:]
	
	for i in range(len(Specie_List1)):
		Specie_List1[i].Read_Write(Results_Directory %(Iter,i),'w')



	y = Pool()
	Results = y.map(Run_parallel,range(len(Specie_List1)))
	y.close()
	y.join()    
   
    #'''
	Specie_List2=[]#Specie_List
	for i in range(len(Results)):
		Specie_List2.append(Specie(Results[i][0],Results[i][1]))
		Specie_List2[i].Read_Write(Results_Directory %(Iter,g),'w')

	#'''

	Specie_List2=Specie_List+Specie_List2

	Cost1=Specie_List[0].Lists(Specie_List2,1)

	xy=Specie_List[0].Lists(Specie_List,0)
	#print(xy)
	xy1=Specie_List[0].Lists(Specie_List2,0)

	
	#plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')

	#plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
	#plt.scatter(Cost[0],Cost[1])
	#print (xy1)

	delta = 10
	X = np.arange(-20.0, 20.0, delta)
	Y = np.arange(-20.0, 20.0, delta)
	x, y = np.meshgrid(X, Y)

	#Z=(x**2 + y**2)/4000-np.cos(x/2**(0.5))*np.cos(y/2**(0.5))+1
	#Z=(X**2 + Y**2)/4000-np.cos(X/2**(0.5))*np.cos(Y/2**(0.5))+1
	Z=-20*np.exp(-0.2*np.sqrt(0.5*(X**2+Y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*Y)))+np.e+20
	#Z=#-np.fabs(np.sin(x)*np.cos(y)*np.exp(1-np.sqrt(x**2+y**2)/np.pi))#-0.0001*((np.fabs(np.sin(x)*np.sin(y)*np.exp(np.fabs(100-np.sqrt(x**2+y**2)/np.pi)))+1)**0.1)#(np.sin(3*np.pi*x))**2+((x-1)**2)*(1+(np.sin(3*np.pi*y))**2)+((y-1)**2)*(1+(np.sin(2*np.pi*y))**2)#-20*np.exp(-0.2*np.sqrt(0.5*(x**2+y**2)))-np.exp(0.5*(np.cos(2*np.pi*x)+np.cos(2*np.pi*y)))+np.e+20#0.5+((np.sin(x**2-y**2))**2-0.5)/(1+0.001*(x**2+y**2))**2
	#Z1 = np.exp(-X**2 - Y**2)
	#Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)

	#Z = (Z1 - Z2) * 2

	fig, ax = plt.subplots()
	CS = ax.contour(X, Y, Z,10,linewidths=0.3)
	
	#ax.clabel(CS, inline=1, fontsize=10)
	
	#ax.set_title('Simplest default with labels')
	plt.scatter(xy1[0],xy1[1],s=1.5,c='black')
	plt.scatter(xy[0],xy[1],s=3.5,c='blue')
	plt.scatter(xy[0][0],xy[1][0],s=10,c='red')
	
	plt.grid(color='black', linestyle='-', linewidth=0.1)
	plt.xlim(-20,20)
	plt.ylim(-20,20)
	
	#plt.show()

	plt.savefig('Pics/0/%i.0.svg'%Iter)
	plt.close()
	
	
	

	Rank_List=Specie_List[0].Rank_Assign(Specie_List1)

	Specie_List = [Specie_List2[i] for i in Rank_List]

	#Temp=Specie_List[Popn2:]
	
	del Specie_List[Popn2:]
	
	Cost=Specie_List[0].Lists(Specie_List,1)

	#Rank_List=Specie_List[0].Lists(Specie_List,2)
	Specie_List[0].Rank_Assign(Specie_List)

	#To write the population (or parent) folder
	for i in range(len(Specie_List)):
		#Specie_List[i].Cost=Results[i][1]
		Specie_List[i].Read_Write(Parent_Directory %(Iter,i),'w')

	#Ann(Specie_List,0)
	
	Iter+=1




thefile = open('FinalCalls', 'w')
thefile.write("%i" %Obj_call)
thefile.close()    



