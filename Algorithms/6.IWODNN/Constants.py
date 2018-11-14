import os,sys

global Row,Col,Func,Iter
global Specie_List

Row=2
Col=2
Func=1

t=1
Popn=40*t
Popn1=20*t
Popn2=30*t
#Popn3=20*t


Smax=10
Smin=2

Exponent = 3

aSigma_init=0.1
aSigma_final=0.0001

Social_factor=0.000001


sigma_initial = aSigma_init*(1-Social_factor)
sigma_final = aSigma_final*(1-Social_factor)

Exponent1 = 1/Exponent

sigma_best = aSigma_final*(Social_factor)
sigma_worst = aSigma_init*(Social_factor)




Iter=0
Iter_max=20

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'
Parent_Directory='Results/Generation_%i/Population/Specie_%i'
Prediction_Directory='Results/Generation_%i/Predictions/Specie_%i'
sys.path.append("../Functions/F7")
import F

