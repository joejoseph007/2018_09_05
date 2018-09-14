import random, sys, os, math, numpy
#Viennet function

def run(x,y):
    result=[0,0]        
    def function1(x,y):
        value = x
        return value

    #Second function to optimize
    def function2(x,y):
    	value=y
    	return value


    result=[function1(x,y),function2(x,y)]

    return result


def check(x,y):
    xmax=math.pi
    xmin=0
    
    if T==0:
    def constraint1(x,y): 
        value = x**2+y**2-1-0.1*math.cos(16*math.tanh(x/y))
        if value>=0:
            return 1
        else:
            return 0

    #Second function to optimize
    def constraint2(x,y):
        value = (x-0.5)**2+(y-0.5)**2
        if value<=0.5:
            return 1
        else:
            return 0
    if constraint1(x,y) and constraint2(x,y):
        return 1
    else:
        return 0
    
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