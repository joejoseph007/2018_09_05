import csv, random, re, sys, os, math, numpy as np, time, subprocess, shutil
import matplotlib.pyplot as plt 
from multiprocessing import Pool
from distutils.dir_util import copy_tree
#import scipy.interpolate as si

Time=time.time()



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
    D[0] = 400000#math.inf
    D[len(F) - 1] = 400000#math.inf
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted1[k+1]] - V2[sorted1[k-1]])/(max(V1)-min(V1))
    for k in range(1,len(F)-1):
        D[k] = D[k]+ (V1[sorted2[k+1]] - V2[sorted2[k-1]])/(max(V2)-min(V2))
    return D

X1=np.random.rand(1,10)
Y1=np.random.rand(1,10)

#print(X[0])
#print(Y[0])

X=[int(100*X1[0][i]**0.5) for i in range(len(X1[0]))]
Y=[int(100*Y1[0][i]**3) for i in range(len(X1[0]))]


NDSa=fast_non_dominated_sort(X,Y)


List=[]
for j in range(len(NDSa)):
    for t in range(len(NDSa[j])):
        List.append(NDSa[j][t])


CDv=[]
for i in range(0,len(NDSa)):
    CDv.append(crowding_distance(X,Y,NDSa[i][:]))

print(X)
print(Y)

print(NDSa)
#print (List)
print (CDv)


plt.scatter(X,Y)
plt.savefig('check2/A.svg')

n=[str(List[i]) for i in range(len(X))]
#print (n)
for j, txt in enumerate(n):
    plt.annotate(txt,(X,Y),fontsize=5)
#plt.show()


Popn3=10

Specie_List2=[]
for i in range(len(NDSa)):
    NDSa2 = [index_of(NDSa[i][j],NDSa[i] ) for j in range(0,len(NDSa[i]))]
    print('NDSa',NDSa2)    s
    front22 = sort_by_values(NDSa2[:], CDv[i][:])
    print('front22',front22)
    front = [NDSa[i][front22[j]] for j in range(0,len(NDSa[i]))]
    
    front.reverse()
    print('front',front)
    for value in front:
        Specie_List2.append(value)
        if(len(Specie_List2)==Popn3):
            break
    if (len(Specie_List2) == Popn3):
        break

print ('Specie_List2',Specie_List2)

X2=[X[i] for i in Specie_List2]
Y2=[Y[i] for i in Specie_List2]

print(X2)
print(Y2)

