import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
import multiprocessing #import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si

Time=time.time()

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'

global Row,Col,Func

Row=5
Col=3
Func=2

Popn=100
Popn2=50

Iter=0
Iter_max=2

global Specie_List

	

class Specie(object):

	def __init__(self,X=np.zeros((Row,Col)),Cost=np.zeros(Func)) :
		self.X = X
		self.Cost = Cost
	
	def Cost_run(self,Directory):
		#from Multiobjective_Functions.F5 import run
		sys.path.append("../Multiobjective_Functions")
		import F5 
		self.Cost=F5.run(self.X[0])
	
	def New(self,sigma):
		self.X=self.X+randf(len(self.X),len(self.X[0]))*sigma



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

	def L2(self,Spc1):
		#self.X=np.loadtxt('Genes')
		#self.Cost=np.loadtxt('Cost')
		#os.chdir(Current_Working_Directory)
        pass
        #return [[Spc1[i].Cost[0] for i in range(len(Spc1))],[Spc1[i].Cost[1] for i in range(len(Spc1))]]
    #def l2(self, parameter_list):
    #    pass
        #self.X=self.X+randf(len(self.X),len(self.X[0]))*sigma






    

		

def randf(r=1,c=1):
	R=np.zeros((r,c))
	for i in range(len(R)):
		for j in range(len(R[0])):
			R[i][j]=random.uniform(-5,5)
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
    
while Iter<Iter_max:

    Cost=Specie.Cost_list(Specie_List)

    NDSa=fast_non_dominated_sort(Cost[0],Cost[1])

    #print(NDSa)

    CDv=[]
    for i in range(0,len(NDSa)):
        CDv.append(crowding_distance(Cost[0],Cost[1],NDSa[i][:]))

    #print(CDv)

    Specie_List1=[]
    for i in range(Popn):
        X1=randf(Row,Col)	
        Specie_List1.append(Specie(X1))
        Specie_List1[i].Cost_run(Results_Directory %(Iter,i))
        Specie_List1[i].Write(Results_Directory %(Iter,i))
        

    Cost1=Specie.Cost_list(Specie_List)
    
    NDSa1=fast_non_dominated_sort(Cost1[0],Cost1[1])

    CDv1=[]
    for i in range(0,len(NDSa)):
        CDv1.append(crowding_distance(Cost1[0],Cost1[1],NDSa1[i][:]))

    
    
    Specie_List2=[]

    for i in range(0,len(NDSa1)):
        NDSa2 = [index_of(NDSa1[i][j],NDSa1[i] ) for j in range(0,len(NDSa1[i]))]
        front22 = sort_by_values(NDSa2[:], CDv1[i][:])
        front = [NDSa1[i][front22[j]] for j in range(0,len(NDSa1[i]))]
        front.reverse()
        for value in front:
            Specie_List2.append(value)
            if(len(Specie_List2)==Popn2):
                break
        if (len(Specie_List2) == Popn2):
            break
    Specie_List = [Specie_List1[i] for i in Specie_List2]

    
    Iter+=1



'''

'''

#plt.scatter ([specie[i].Cost[0] for i in range(len(specie))],[specie[i].Cost[1] for i in range(len(specie))])
#plt.savefig("Fig.svg")
#plt.show()
'''
specie2=[Pop(randf(Row,Col)) for i in range(10)]

print (specie2[0].Cost)

#specie2=Pool_handler(specie2)

np.savetxt('file',specie2[0].X)
abs1=np.loadtxt('file')
print(abs1)
abs1.sort(axis=0)
print(abs1)
print ('CPUS',multiprocessing.cpu_count())
os.chdir(Results_Directory)


np.savetxt('file',specie2[0].X)

print(os.getcwd())
os.chdir(Current_Working_Directory)
print(os.getcwd())

thefile=open('Generation','w')
thefile.write('1')
thefile.close()





'''





'''
#Main program starts here


pop_size = 50
max_gen = 921

#Initialization
min_x=-55
max_x=55
solution=[min_x+(max_x-min_x)*random.random() for i in range(0,pop_size)]
gen_no=0

while(gen_no<max_gen):
    function1_values = [function1(solution[i])for i in range(0,pop_size)]
    function2_values = [function2(solution[i])for i in range(0,pop_size)]
    
    non_dominated_sorted_solution = fast_non_dominated_sort(function1_values[:],function2_values[:])
    
	
	print("The best front for Generation number ",gen_no, " is")
    for valuez in non_dominated_sorted_solution[0]:
        print(round(solution[valuez],3)," ")
    
	print("\n")
    crowding_distance_values=[]
    for i in range(0,len(non_dominated_sorted_solution)):
        crowding_distance_values.append(crowding_distance(function1_values[:],function2_values[:],non_dominated_sorted_solution[i][:]))
    solution2 = solution[:]
    
    #Generating offsprings
    while(len(solution2)!=2*pop_size):
        a1 = random.randint(0,pop_size-1)
        b1 = random.randint(0,pop_size-1)
        solution2.append(crossover(solution[a1],solution[b1]))
    function1_values2 = [function1(solution2[i])for i in range(0,2*pop_size)]
    function2_values2 = [function2(solution2[i])for i in range(0,2*pop_size)]
    
    NDSa1 = fast_non_dominated_sort(function1_values2[:],function2_values2[:])
    crowding_distance_values2=[]
    for i in range(0,len(NDSa1)):
        crowding_distance_values2.append(crowding_distance(function1_values2[:],function2_values2[:],NDSa1[i][:]))
    new_solution= []
    
    for i in range(0,len(NDSa1)):
        NDSa3 = [index_of(NDSa1[i][j],NDSa1[i] ) for j in range(0,len(NDSa1[i]))]
        front22 = sort_by_values(NDSa3[:], crowding_distance_values2[i][:])
        front = [NDSa1[i][front22[j]] for j in range(0,len(NDSa1[i]))]
        front.reverse()
        for value in front:
            new_solution.append(value)
            if(len(new_solution)==pop_size):
                break
        if (len(new_solution) == pop_size):
            break
    solution = [solution2[i] for i in new_solution]
    gen_no = gen_no + 1



#Lets plot the final front now
function1 = [i * -1 for i in function1_values]
function2 = [j * -1 for j in function2_values]
plt.xlabel('Function 1', fontsize=15)
plt.ylabel('Function 2', fontsize=15)
plt.scatter(function1, function2)
plt.show()

'''


'''
R=random.choice([-1,1])
#R1=randf(X,Y)

print(spc.X)

spc.Cost_run(0)
print(spc.Cost)

specie=[]
for i in range(10000):
	X1=randf(Row,Col)	
	specie.append(Pop(X1))
	specie[i].Cost_run(i)

plt.scatter ([specie[i].Cost[0] for i in range(len(specie))],[specie[i].Cost[1] for i in range(len(specie))])
plt.show()

#print Arra

'''
'''
X=[]
Y=[]
res=[]
res1=[]
res2=[]
for i in range(1000):
	X.append(randf(0,5))
	Y.append(randf(0,3))
	res.append(F1.run(X[i],Y[i]))
	res1.append(res[i][0])
	res2.append(res[i][1])

plt.scatter(res1,res2)
plt.show()



Z1=[i for i in range(100)]

def run(Z):
	
	t=time.time()
	A=np.array([Z])
	R=np.random.rand(len(A))
	A=A+R*10
	t1=time.time()-t

	t=time.time()
	A=Z
	for i in range(len(A)):
		A[i]=A[i]+random.random()*10
	t2=time.time()-t

	return t2-t1

print run(Z1)


Arra=np.zeros((Row,Col))

#R=random.random()
R=np.random.rand(len(Arra),len(Arra[0]))
	
X1=Arra+R

print Arra[0]
print X1[0]
'''