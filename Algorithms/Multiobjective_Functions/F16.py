import random, sys, os, math, numpy
#Constr-Ex problem

def run(Arr):
    x=Arr[0]
    y=Arr[1]
    result=[0,0]        
    def function1(x,y):
        value = x
        return value

    #Second function to optimize
    def function2(x,y):
    	value=(1+y)/x
    	return value

    result=[-function1(x,y),-function2(x,y)]

    return result


def check(Arr,T,Z=[0]):
    x=Arr[0]
    y=Arr[1]
    xmax=1
    xmin=0.1
    ymax=5
    ymin=0
    if T==0:
        def constraint1(x,y): 
            value = y+9*x
            if value>=6:
                return 1
            else:
                return 0

        #Second function to optimize
        def constraint2(x,y):
            value = -y+9*x
            if value>=1:
                return 1
            else:
                return 0
        if constraint1(x,y) and constraint2(x,y):
            if x<=xmax and x>=xmin:
                if y<=ymax and y>=ymin:
                    return 1
        else:
            return 0
    elif T==1:
        Range=numpy.zeros((Z[0],Z[1],2))
        Range[0][:][0]=xmin
        Range[1][:][0]=ymin
        Range[0][:][1]=xmax
        Range[1][:][1]=ymax
        return Range
#print([[check(i/10,j/10) for i in range(10) ] for j in range(50)])


#Range=numpy.zeros((3,4,2))
#Range[:][:][0]=2
#print (Range)
#print (check(1,0,1,[2,2]))






'''


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
    X.append(randf(0.1,1))
    Y.append(randf(0,5))
    res.append(run([X[i],Y[i]]))
    res1.append(res[i][0])
    res2.append(res[i][1])



plt.scatter(res1,res2)
plt.show()


'''
