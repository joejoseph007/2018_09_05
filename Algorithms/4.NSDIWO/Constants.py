import os,sys

global Row,Col,Func,Iter
global Specie_List

Row=1
Col=3
Func=2

t=1
Popn=20*t

Popn2=10*t
#Popn3=20*t

Smin=3
Smax=0.5

Exponent = 4

aSigma_init=0.1
aSigma_final=0.00001

Social_factor=0.3


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
sys.path.append("../Multiobjective_Functions/F5")
import F

