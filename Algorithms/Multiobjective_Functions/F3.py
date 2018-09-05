import random, sys, os, math, numpy
#Fonseca  Fleming function

def run(x,y):
    result=[0,0]        
    Xi=[x,y]
    n=len(Xi)
    def function1(x,y):
        sum1=0
        for i in range(n):
        	sum1=sum1+(Xi[i]-1/(n)**0.5)**2
        value = 1-numpy.exp(-sum1)
        return value

    #Second function to optimize
    def function2(x,y):
    	sum1=0
    	for i in range(n):
        	sum1=sum1+(Xi[i]+1/(n)**0.5)**2
        value = 1-numpy.exp(-sum1)
    	return value
    
    result=[function1(x,y),function2(x,y)]

    return result


def check(x,y):
    xmax=4
    xmin=-4
    ymax=4
    ymin=-4

    def constraint1(x,y): 
        value = 0
        if value<=225:
            return 1
        else:
            return 0

    #Second function to optimize
    def constraint2(x,y):
        value = 0
        if value<=0:
            return 1
        else:
            return 0
    if constraint1(x,y) and constraint2(x,y):
        if x<=xmax and x>=xmin:
            if y<=ymax and y>=ymin:
                return 1
    else:
        return 0


print check(0,5)


import matplotlib.pyplot as plt 

def randf(x,y):
    a=1000
    return float(random.randrange(x*a,y*a))/a

X=[]
Y=[]
res=[]
res1=[]
res2=[]
for i in range(1000):
    X.append(randf(-4,4))
    Y.append(randf(-4,4))
    res.append(run(X[i],Y[i]))
    res1.append(res[i][0])
    res2.append(res[i][1])

plt.scatter(res1,res2)
plt.show()


