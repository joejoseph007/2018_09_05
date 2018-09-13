import random, sys, os, math, numpy
#Constr-Ex problem

def run(Arr):
	result=[0.,0.]        

	def function1(Arr):
		value = Arr[0]
		return value

    
	def function3(Arr):
		value=0

		for i in range(1,len(Arr)):
			value=value+Arr[i]
		value=1+9/29*value
		return value
    
	def function4(Arr):
		value=1-(function1(Arr)/function3(Arr))**0.5-(function1(Arr)/function3(Arr))*math.sin(10*math.pi*function1(Arr))
		return value

    #Second function to optimize
	def function2(Arr):
		value=function3(Arr)*function4(Arr)
		return value
	
	#print(function4(Arr))
	result=[-function1(Arr),-function2(Arr)]

	return result

X=numpy.random.rand(1,30)

run(X[0])

def check(Arr,T,Z=[0]):
    #print(Arr)
	xmax=1
	xmin=0
	if T==0:
		return 1
	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		for i in range(len(Range[0])):
			Range[0][i][0]=xmin
			Range[0][i][1]=xmax
		return Range
#print([[check(i/10,j/10) for i in range(10) ] for j in range(50)])


#Range=numpy.zeros((3,4,2))
#Range[:][:][0]=2
#print (Range)
#print (check([1,0],1,[2,2]))


'''

X=numpy.zeros((1,2))
sigma=10

def Range_chk_slic(T):    
    if T==0:
        if check(X,T):
            return 1
        else: 
            return 0
    if T==1:
        Range=check(X,T,[1,2])
        for i in range(len(X)):
            for j in range(len(X[0])):
                X[i][j]=max(X[i][j],Range[i][j][0])
                X[i][j]=min(X[i][j],Range[i][j][1])
        return 1


while 1:
    X=X+numpy.random.normal(0,sigma,(len(X),len(X[0])))
    if Range_chk_slic(X,1):
        if Range_chk_slic(X,0):
            break
'''



'''

import matplotlib.pyplot as plt 

def randf(x,y):
    a=1000
    return float(random.randrange(x*a,y*a))/a


res=[]
res1=[]
res2=[]

for i in range(10000):
	X=numpy.random.rand(1,30)
	#Y.append(randf(0,5))
	res.append(run(X[0]))
	#print (res)
	res1.append(-res[i][0])
	res2.append(-res[i][1])



plt.scatter(res1,res2)
plt.show()

'''

