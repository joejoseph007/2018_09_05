import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si

Time=time.time()

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'

global Row,Col,Func,Iter
global Specie_List

Row=1
Col=2
Func=2

t=2
Popn=20*t

Popn2=10*t
Popn3=20*t

Iter=0
Iter_max=50

global Specie_List

sys.path.append("../Multiobjective_Functions/F1")
import F

class Specie(object):

	def __init__(self,X=np.zeros((Row,Col)),Cost=np.zeros(Func),Rank=-1) :
		self.X = X
		self.Cost = Cost
		self.Rank = Rank
		#from Multiobjective_Functions.F import run
		
	def Range_chk_slic(self,T):
		#sys.path.append("../Multiobjective_Functions")
		#import F
		
		if T==0:
			if F.check(self.X,T):
				return 1
			else: 
				return 0
		if T==1:
			Range=F.check(self.X,T,[Row,Col])
			for i in range(len(self.X)):
				for j in range(len(self.X[0])):
					self.X[i][j]=max(self.X[i][j],Range[i][j][0])
					self.X[i][j]=min(self.X[i][j],Range[i][j][1])
			#return 1
					
		
	def Cost_run(self,Directory):
		#sys.path.append("../Multiobjective_Functions")
		#import F
		self.Cost=F.run(self.X[0])
	
	def New(self,T,sigma=1,Specie=[]):
		#sys.path.append("../Multiobjective_Functions")
		#import F
		Temp=self.X
		#print(Temp,self.X)
		self.X=np.where(self.X>0,0.0,0.0)				
		
		Range=F.check(self.X,1,[Row,Col])
		for i in range(len(self.X)):
			for j in range(len(self.X[0])):
				while 1:
					if T==0:
						self.X[i][j]=random.uniform(Range[i][j][0],Range[i][j][1])
						if self.Range_chk_slic(0):
							break
					if T==1:
						self.X[i][j]=np.random.normal(Temp[i][j],(Range[i][j][1]-Range[i][j][0])*sigma)
						if self.Range_chk_slic(0):
							break
					if T==2:
						self.X[i][j]=Specie[0].X[i][j]
						if self.Range_chk_slic(0):
							break
		
		self.Range_chk_slic(1)
		
	def Write(self,Directory):
		if(not os.path.isdir(Directory)):
			os.makedirs(Directory)

		os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))

		np.savetxt('Genes',self.X)
		np.savetxt('Cost',self.Cost)
		os.chdir(Current_Working_Directory)
	
	def Read(self,Directory):
		os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))
		self.X=np.loadtxt('Genes')
		self.Cost=np.loadtxt('Cost')
		os.chdir(Current_Working_Directory)

	def Cost_list(self,Spc1):
		return [[Spc1[i].Cost[0] for i in range(len(Spc1))],[Spc1[i].Cost[1] for i in range(len(Spc1))]]

	def XY_list(self,Spc1):
		return [[Spc1[i].X[0][0] for i in range(len(Spc1))],[Spc1[i].X[0][1] for i in range(len(Spc1))]]





def Cost_Key(Element):
	return Element.Cost[1]

#if __name__ == "__main__":


def index_of(a,list):
    for i in range(len(list)):
        if list[i] == a:
            return i
    return -1

def sort_by_values(l, V):
    SL = []
    while(len(SL)!=len(l)):
        if index_of(min(V),V) in l:
            SL.append(index_of(min(V),V))
        V[index_of(min(V),V)] = math.inf
    return SL

def fast_non_dominated_sort(V1, V2):
    S=[[] for i in range(0,len(V1))]
    F = [[]]
    n=[0 for i in range(0,len(V1))]
    rank = [0 for i in range(0, len(V1))]

    for p in range(0,len(V1)):
        S[p]=[]
        n[p]=0
        for q in range(0, len(V1)):
            if (V1[p] > V1[q] and V2[p] > V2[q]) or (V1[p] >= V1[q] and V2[p] > V2[q]) or (V1[p] > V1[q] and V2[p] >= V2[q]):
                if q not in S[p]:
                    S[p].append(q)
            elif (V1[q] > V1[p] and V2[q] > V2[p]) or (V1[q] >= V1[p] and V2[q] > V2[p]) or (V1[q] > V1[p] and V2[q] >= V2[p]):
                n[p] = n[p] + 1
        if n[p]==0:
            rank[p] = 0
            if p not in F[0]:
                F[0].append(p)

    i = 0
    while(F[i] != []):
        Q=[]
        for p in F[i]:
            for q in S[p]:
                n[q] =n[q] - 1
                if( n[q]==0):
                    rank[q]=i+1
                    if q not in Q:
                        Q.append(q)
        i = i+1
        F.append(Q)

    del F[len(F)-1]
    return F

def crowding_distance(V1, V2, F):
    D = [0 for i in range(0,len(F))]
    sorted1 = sort_by_values(F, V1[:])
    sorted2 = sort_by_values(F, V2[:])
    D[0] = 2**100#math.inf
    D[len(F) - 1] = 2**100 #math.inf
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted1[k+1]] - V2[sorted1[k-1]])/(max(V1)-min(V1))
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted2[k+1]] - V2[sorted2[k-1]])/(max(V2)-min(V2))
    return D


Specie_List=[]

  
for i in range(Popn):	
	Specie_List.append(Specie())
	#print ("here")
	Specie_List[i].New(0)
	#Specie_List[i].New(5)
	Specie_List[i].Cost_run(Results_Directory %(Iter,i))
	Specie_List[i].Write(Results_Directory %(Iter,i))
Iter+=1

while Iter<=Iter_max:

	#print(Iter)
	#for i in range(len(Specie_List)):
	sigma=1/Iter**0.5
	print(Iter,sigma)
	print(Specie_List[0].X,Specie_List[0].Cost)

	Cost=Specie_List[0].Cost_list(Specie_List)

	#plt.close()

	NDSa=fast_non_dominated_sort(Cost[0],Cost[1])

	#print(NDSa)

	CDv=[]
	for i in range(0,len(NDSa)):
		CDv.append(crowding_distance(Cost[0],Cost[1],NDSa[i][:]))

	Specie_List1_2=[]
	for i in range(0,len(NDSa)):
		NDSa2 = [index_of(NDSa[i][j],NDSa[i] ) for j in range(0,len(NDSa[i]))]
		front22 = sort_by_values(NDSa2[:], CDv[i][:])
		front = [NDSa[i][front22[j]] for j in range(0,len(NDSa[i]))]
		front.reverse()
		#print(front)
		for value in front:
			Specie_List1_2.append(value)
			if(len(Specie_List1_2)==len(Specie_List)):
				break
		if (len(Specie_List1_2) == len(Specie_List)):
			break


	def Run_parallel(i):
		global Iter,Specie_List
		
		Specie_List1=[]#Specie_List
		sigma=1/Iter**0.5
		Specie_List1.append(Specie(Specie_List[i].X))
		Specie_List1[0].New(1,sigma)
		Specie_List1[0].Cost_run(Results_Directory %(Iter,i))
		Specie_List1[0].Write(Results_Directory %(Iter,i))
		
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
	plt.ylim(-60,10)
	plt.xlim(-140,10)
	
	#F16
	#plt.ylim(-10,0)
	#plt.xlim(-1,0)

	#F5
	#plt.ylim(-10,14)
	#plt.xlim(0,20)

	#F11
	#plt.ylim(-5,5)
	#plt.xlim(-2,2)
	
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
