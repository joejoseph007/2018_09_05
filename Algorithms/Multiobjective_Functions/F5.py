import random, sys, os, math, numpy
#Kursawe function

def run(Arr):
    result=[0,0]        
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


def check(Arr):
    xmax=20
    xmin=-20
    ymax=20
    ymin=-20

    def constraint1(Arr): 
        value = Arr[0]**2+Arr[1]**2
        if value<=225:
            return 1
        else:
            return 0

    #Second function to optimize
    def constraint2(Arr):
        value = Arr[0]-3*Arr[1]+10**2+(Arr[1]+3)**2
        if value<=0:
            return 1
        else:
            return 0
    if constraint1(Arr) and constraint2(Arr):
        if Arr[0]<=xmax and Arr[0]>=xmin:
            if Arr[1]<=ymax and Arr[1]>=ymin:
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
Z=[]
res=[]
res1=[]
res2=[]

for i in range(20000):
	X.append(randf(-5,5))
	Y.append(randf(-5,5))
	Z.append(randf(-5,5))
	res.append(run([X[i],Y[i],Z[i]]))
	res1.append(res[i][0])
	res2.append(res[i][1])


plt.scatter(res1,res2)
plt.xlim(-20,-14)
plt.ylim(-12,0)
plt.show()


'''
