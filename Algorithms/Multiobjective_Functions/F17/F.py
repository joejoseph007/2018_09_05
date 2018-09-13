import random, sys, os, math, numpy
#Viennet function

def run(x,y):
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

    result=[function1(x,y),function2(x,y),function3(x,y)]

    return result


def check(x,y):
    xmax=3
    xmin=-3
    ymax=3
    ymin=-3

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