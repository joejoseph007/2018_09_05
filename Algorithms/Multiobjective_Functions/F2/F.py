import random, sys, os, math, numpy
#Chakong and Haimes function

def run(x,y):
    result=[0,0]        
    
    def function1(x,y):
        value = 2+(x-2)**2+(y-1)**2
        return value

    #Second function to optimize
    def function2(x,y):
        value = 9*x**2+(y-1)**2
        return value
    
    result=[-function1(x,y),-function2(x,y)]

    return result


def check(x,y):
    xmax=20
    xmin=-20
    ymax=20
    ymin=-20

    def constraint1(x,y): 
        value = x**2+y**2
        if value<=225:
            return 1
        else:
            return 0

    #Second function to optimize
    def constraint2(x,y):
        value = x-3*y+10**2+(y+3)**2
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

#'''
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
    X.append(randf(-1,1))
    Y.append(randf(-1,1))
    res.append(run(X[i],Y[i]))
    res1.append(res[i][0])
    res2.append(res[i][1])

plt.scatter(res1,res2)
plt.show()


#'''