import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
import scipy.interpolate as si

from Constants import *
from NSGA2 import *


class Specie(object):

	def __init__(self,X=np.zeros((Row,Col)),Cost=math.inf,Rank=-1,Offspring=np.zeros(2)) :
		self.X = X
		self.Cost = Cost
		self.Rank = Rank
		self.Offspring = Offspring #['Number of offspring','Sigma']
		self.Range=F.check(self.X,1,[Row,Col])
		#from Multiobjective_Functions.F import run


	def Read_Write(self,Directory,T):
		#T=r,w,rw correspond to read, write and read-write 

		if T=='w' or T=='rw': 
			if(not os.path.isdir(Directory)):
				os.makedirs(Directory)
			os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))
			np.savetxt('Genes',self.X)
			#print(self.Cost)
			np.savetxt('Cost',[self.Cost])
			np.savetxt('Rank',[self.Rank])
			np.savetxt('Offspring',self.Offspring)
		
		if T=='r' or T=='rw':
			os.chdir(Directory)#"../Results/Generation_%d/Specie_%d/CFD" %(r,e))
			self.X=np.loadtxt('Genes')
			self.Cost=float(np.loadtxt('Cost'))
		
		os.chdir(Current_Working_Directory)
	
					
		
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
	
	def New(self,T,Z=np.zeros((Row,Col)),sigma=1):
		
		
		
		Range=F.check(self.X,1,[Row,Col])
		
		
		for i in range(len(self.X)):
			for j in range(len(self.X[0])):
				while 1:
					if T==0:
						self.X[i][j]=np.random.rand()*(Range[i][j][1]-Range[i][j][0])+Range[i][j][0] #random.uniform(Range[i][j][0],Range[i][j][1])
						if self.Range_chk_slic(0):
							break
					
					if T==1:
						self.X[i][j]=np.random.normal(Z[i][j],(Range[i][j][1]-Range[i][j][0])*sigma)
						#print(self.X[i][j],Z[i][j])#,Taboo_list[k].X[i][j],sigma1)
						#time.sleep(5)
						if self.Range_chk_slic(0):
							break
					
						
		self.Range_chk_slic(1)
		#return X
		
	
	def Lists(self,Spc1,T):
		if T==0: # XY points
			x=[]#np.zero((Row,Col,len(Spc1)))
			y=[]
			z=[]
			#print(Spc1[0].X[0])
			#xy_list=[]
			for k in range(len(Spc1)):
				#print(k)
				x.append(Spc1[k].X[0][0])
				y.append(Spc1[k].X[0][1])
				#z.append(Spc1[k].X[0][2])
			
			#xy_list.append(x,y)
			#print (xy_list)
			return [x,y,z]
		
		if T==1: # Cost list
			#print(Spc1[0].Cost)
			Cost_list=[]
			for i in range(len(Spc1)):
				Cost_list.append(Spc1[i].Cost)
			return Cost_list
		
		if T==2: # Rank list
			return [Spc1[i].Rank for i in range(len(Spc1))]
			
	def Rank_Assign(self,Spc1):
		Cost1=Spc1[0].Lists(Spc1,1)
		Cost=[[i,Cost1[i]]for i in range(len(Cost1))]
		#print (Cost)
		def takeSecond(elem):
		    return elem[1]
		Rank_List1=sorted(Cost,key=takeSecond)

		
		Rank_List=[Rank_List1[i][0] for i in range(len(Rank_List1))]
		for i in range(len(Spc1)):
			Spc1[i].Rank=Rank_List[i] 
		
		return Rank_List




