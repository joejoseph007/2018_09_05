import os,sys

global Row,Col,Func,Iter
global Specie_List

Row=2
Col=2
Func=3

t=1
Popn=20*t

Popn2=20*t
#Popn3=20*t

Smin=4
Smax=1

Exponent = 3

aSigma_init=0.2
aSigma_final=0.05

Social_factor=0.0003


sigma_initial = aSigma_init*(1-Social_factor)
sigma_final = aSigma_final*(1-Social_factor)

Exponent1 = 1/Exponent

sigma_best = aSigma_final*(Social_factor)
sigma_worst = aSigma_init*(Social_factor)



Iter=0
Iter_max=100

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'
Parent_Directory='Results/Generation_%i/Population/Specie_%i'
sys.path.append("../Multiobjective_Functions/F1")
import F

