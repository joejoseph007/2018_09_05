import random, sys, os, math, numpy
#Kursawe function

def run(Arr):
    result=[0,0]        
    #Arr=Arr[0]
    #print( Arr)
    Xi=[Arr[0],Arr[1],Arr[2]]
    n=len(Xi)
    def function1(Arr):
        sum1=0
        for i in range(2):
        	sum1=sum1-10*numpy.exp(-0.2*(Xi[i]**2+Xi[i+1]**2)**0.5)
        value = sum1
        return value

    #Second function to optimize
    def function2(Arr):
        sum1=0
        for i in range(3):
            sum1=sum1+(abs(Xi[i])**0.8+5*math.sin(Xi[i]**3))
        value = sum1
        return value
    
    result=[-function1(Arr),-function2(Arr)]

    return result


def check(Arr,T,Z=[0]):
    xmax=5
    xmin=-5
    
    if T==0:
        return 1
    
    elif T==1:
        Range=numpy.zeros((Z[0],Z[1],2))
        for i in range(len(Range[0])):
            Range[0][i][0]=xmin
            Range[0][i][1]=xmax
        
        return Range



#Range=check([1,2,3],1,[1,3])
#print (Range)
#print check(0,5)
'''
import matplotlib.pyplot as plt 

def randf(x,y):
    a=1000
    return float(random.randrange(x*a,y*a))/a

X=[]
Y=[]
Z=[]
res=[]
res1=[]
res2=[]

for i in range(200000):
	X.append(randf(-5,5))
	Y.append(randf(-5,5))
	Z.append(randf(-5,5))
	res.append(run([X[i],Y[i],Z[i]]))
	res1.append(res[i][0])
	res2.append(res[i][1])


plt.scatter(res1,res2)
plt.xlim(14,20)
plt.ylim(-2,14)
plt.show()
'''


