import os,sys

global Row,Col,Func,Iter
global Specie_List

Row=1
Col=30
Func=2

t=10
Popn=20*t

Popn2=10*t
Popn3=20*t

Iter=0
Iter_max=100

Current_Working_Directory=os.getcwd()
Results_Directory='Results/Generation_%i/Specie_%i'

sys.path.append("../Multiobjective_Functions/F11")
import F

