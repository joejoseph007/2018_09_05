import random, sys, os, math, numpy
#Viennet function

def run(Arr):
    x=Arr[0]
    y=Arr[1]
    result=[0,0]        
    def function1(x,y):
        value = 0.5*(x**2+y**2)+math.sin(x**2+y**2)
        return value

    #Second function to optimize
    def function2(x,y):
    	value=((3*x-2*y+4)**2)/8+((x-y+1)**2)/27+15
    	return value

    def function3(x,y):
        value = 1/(x**2+y**2+1)-1.1*math.exp(-(x**2+y**2))
        return value

    result=[-function2(x,y),-function1(x,y),-function3(x,y)]

    return result



def check(Arr,T,Z=[0]):
    xmax=3
    xmin=-3
    
    if T==0:
        return 1
    
    elif T==1:
        Range=numpy.zeros((Z[0],Z[1],2))
        for i in range(len(Range[0])):
            Range[0][i][0]=xmin
            Range[0][i][1]=xmax
        
        return Range


'''
#print check(0,5)


import matplotlib.pyplot as plt 

def randf(x,y):
    a=1000
    return float(random.randrange(x*a,y*a))/a

X=[]
Y=[]
res=[]
res1=[]
res2=[]
res3=[]

for i in range(1000):
    X.append(randf(-3,3))
    Y.append(randf(-3,3))
    res.append(run(X[i],Y[i]))
    res1.append(res[i][0])
    res2.append(res[i][1])
    res3.append(res[i][2])


plt.scatter(res3,res2)
plt.show()


'''