import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si

Time=time.time()

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'

global Row,Col,Func

Row=1
Col=3
Func=2

Popn=120

Popn2=120
Popn3=120

Iter=0
Iter_max=100

global Specie_List

	

class Specie(object):

	def __init__(self,X=np.zeros((Row,Col)),Cost=np.zeros(Func)) :
		self.X = X
		self.Cost = Cost

	def Cost_run(self,Directory):
		#from Multiobjective_Functions.F5 import run
		sys.path.append("../Multiobjective_Functions")
		import F16
		self.Cost=F16.run(self.X[0])
	
	def New(self,sigma):
		
        
        
        while 1:
            X=self.X+np.random.normal(0,sigma,(len(self.X),len(self.X[0])))
            
            if 
            
            Range=np.zeros((Row,Col,2))

            for i in range(len(X)):
                for j in range(len(X[0])):
                    X[i][j]=max(X[i][j],Range[i][j][0])
                    X[i][j]=min(X[i][j],Range[i][j][1])
                    #print('yes') 
            return X


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




def randf(r=1,c=1,min1,max1):
	R=np.zeros((r,c))
	for i in range(len(R)):
		for j in range(len(R[0])):
			R[i][j]=random.uniform(min1,max1)
	#random.choice()
	return R

def Cost_Key(Element):
	return Element.Cost[1]

#if __name__ == "__main__":


def index_of(a,list):
    for i in range(0,len(list)):
        if list[i] == a:
            return i
    return -1

def sort_by_values(l, V):
    SL = []
    while(len(SL)!=len(l)):
        if index_of(min(V),V) in l:
            SL.append(index_of(min(V),V))
        V[index_of(min(V),V)] = float('inf')
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
    D[0] = 4444444444444444
    D[len(F) - 1] = 4444444444444444
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted1[k+1]] - V2[sorted1[k-1]])/(max(V1)-min(V1))
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted2[k+1]] - V2[sorted2[k-1]])/(max(V2)-min(V2))
    return D


Specie_List=[]

  
for i in range(Popn):
    X1=randf(Row,Col)	
    Specie_List.append(Specie(X1))
    Specie_List[i].Cost_run(Results_Directory %(Iter,i))
    Specie_List[i].Write(Results_Directory %(Iter,i))
Iter+=1

while Iter<=Iter_max:
    
    print(Iter)
    #for i in range(len(Specie_List)):
    print(Specie_List[0].X,Specie_List[0].Cost)

    Cost=Specie_List[0].Cost_list(Specie_List)
    
    #plt.close()
    
    NDSa=fast_non_dominated_sort(Cost[0],Cost[1])

    #print(NDSa)

    CDv=[]
    for i in range(0,len(NDSa)):
        CDv.append(crowding_distance(Cost[0],Cost[1],NDSa[i][:]))

    #print(CDv)
    #offsprings
    '''
    Specie_List1=[]
    for i in range(Popn2):
        X1=randf(Row,Col)	
        Specie_List1.append(Specie(X1))
        
        Specie_List1[i].Cost_run(Results_Directory %(Iter,i))
        #Specie_List1[i].Write(Results_Directory %(Iter,i))
    
    '''    
    
    Specie_List1=[]#Specie_List
    for i in range(len(Specie_List)):
        Specie_List1.append(Specie(Specie_List[i].New(1/Iter**0.5)))
        Specie_List1[i].Cost_run(Results_Directory %(Iter,i))
        Specie_List1[i].Write(Results_Directory %(Iter,i))
    
    #'''




    Specie_List1=Specie_List+Specie_List1
    
    
    
    #print(Iter,len(Specie_List1))

    Cost1=Specie_List[0].Cost_list(Specie_List1)

    xy=Specie_List[0].XY_list(Specie_List)
    xy1=Specie_List[0].XY_list(Specie_List1)

    #'''
    plt.ylim(-10,10)
    plt.xlim(-10,10)
    #plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')
    
    #plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
    #plt.scatter(Cost[0],Cost[1])
    
    plt.scatter(xy1[0],xy1[1],s=1,c='black')
    plt.scatter(xy[0],xy[1],s=15,c='blue')
    

    #plt.ylim(-150,25)
    #plt.xlim(-150,25)
    plt.savefig('Pics/0/%i.0.svg'%Iter)
    plt.close()
    
    plt.ylim(-60,10)
    plt.xlim(-2,0)
    #plt.savefig('Pics/%i.0.svg'%Iter,s=20,c='red')
    
    plt.scatter(Cost1[0],Cost1[1],s=5,c='black')
    plt.scatter(Cost[0],Cost[1],s=15,c='blue')
    

    #plt.ylim(-150,25)
    #plt.xlim(-150,25)
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
        for value in front:
            Specie_List2.append(value)
            if(len(Specie_List2)==Popn3):
                break
        if (len(Specie_List2) == Popn3):
            break
    
    #Specie_List =[]
    
    Specie_List = [Specie_List1[i] for i in Specie_List2]

    
    Iter+=1
