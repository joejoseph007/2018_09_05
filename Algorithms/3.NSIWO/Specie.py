	import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *


class Specie(object):

	def __init__(self,X=np.zeros((Row,Col)),Cost=np.zeros(Func),Rank=-1,Offspring=np.zeros(2)) :
		self.X = X
		self.Cost = Cost
		self.Rank = Rank
		self.Offspring = Offspring #['Number of offspring','Sigma']
		#from Multiobjective_Functions.F import run
		
					
		
	def Cost_run(self,Directory):
		#sys.path.append("../Multiobjective_Functions")
		#import F
		self.Cost=F.run(self.X[0])

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
	
	def New(self,T,sigma=1,Specie=[]):
		#sys.path.append("../Multiobjective_Functions")
		#import F
		Temp=self.X
		#print(Temp,self.X)
		self.X=np.where(self.X>0,0.0,0.0)				
		Range=F.check(self.X,1,[Row,Col])
		k=0
		#print(self.Offspring)
		#while k<=int(self.Offspring[0]):
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
		#k+=1	
		#self.X=np.round(self.X,3)
		self.Range_chk_slic(1)
		
	def Read_Write(self,Directory,T):
		#T=0 for only write
		#T=1 for only read
		#T=2 for both Write and Read		
		
		if T==0 or T==2: 
			if(not os.path.isdir(Directory)):
				os.makedirs(Directory)
			os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))
			np.savetxt('Genes',self.X)
			np.savetxt('Cost',self.Cost)
			#np.savetxt('Rank',self.Rank)
			#np.savetxt('Offspring',self.Offspring)
		
		if T==1 or T==2:
			os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))
			self.X=np.loadtxt('Genes')
			self.Cost=np.loadtxt('Cost')
		
		os.chdir(Current_Working_Directory)

	def Lists(self,Spc1,T):
		if T==0: # XY points
			x=[]#np.zero((Row,Col,len(Spc1)))
			y=[]
			z=[]
			#xy_list=[]
			for k in range(len(Spc1)):
				x.append(Spc1[k].X[0][0])
				y.append(Spc1[k].X[0][1])
				#z.append(Spc1[k].X[0][2])
			
			#xy_list.append(x,y)
			#print (xy_list)
			return [x,y,z]
		
		if T==1: # Cost list
			Cost_list=[]
			for j in range(len(Spc1[0].Cost)):
				Cost_list.append([Spc1[i].Cost[j] for i in range(len(Spc1))])
			return Cost_list
		
		if T==2: # Rank list
			return [Spc1[i].Rank for i in range(len(Spc1))]
			
	def Rank_Assign(self,Spc1):
		Cost=Spc1[0].Lists(Spc1,1)

		NDSa=fast_non_dominated_sort(Cost[0],Cost[1])

		#print(NDSa)

		CDv=[]
		for i in range(0,len(NDSa)):
			CDv.append(crowding_distance(Cost[0],Cost[1],NDSa[i][:]))

		Rank_List=[]
		for i in range(0,len(NDSa)):
			NDSa2 = [index_of(NDSa[i][j],NDSa[i] ) for j in range(0,len(NDSa[i]))]
			front22 = sort_by_values(NDSa2[:], CDv[i][:])
			front = [NDSa[i][front22[j]] for j in range(0,len(NDSa[i]))]
			front.reverse()
			#print(front)
			for value in front:
				Rank_List.append(value)
				if(len(Rank_List)==len(Spc1)):
					break
			if (len(Rank_List) == len(Spc1)):
				break

		for i in range(len(Spc1)):
			Spc1[i].Rank=Rank_List[i] 




