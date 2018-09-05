import random, sys, os, math, numpy

#Binh and Korn function
def run(Arr):
	result=[0,0]		
	
	def function1(Arr):
	    value = 4*Arr[0]**2+4*Arr[1]**2
	    return value

	#Second function to optimize
	def function2(Arr):
	    value = (Arr[0]-5)**2+(Arr[1]-5)**2
	    return value
	
	result=[-function1(Arr),-function2(Arr)]

	return result


def check(Arr):

	def constraint1(Arr): 
		value = (Arr[0]-5)**2+Arr[1]**2
		if value<=25:
			return 1
		else:
			return 0

	#Second function to optimize
	def constraint2(Arr):
		value = (Arr[0]-8)**2+(Arr[1]+3)**2
		if value>=7.7:
			return 1
		else:
			return 0
	if constraint1(Arr) and constraint2(Arr):
		if Arr[0]<=5 and Arr[0]>=0:
			if Arr[1]<=3 and Arr[1]>=0:
				return 1
	else:
		return 0

'''
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
	X.append(randf(0,5))
	Y.append(randf(0,3))
	res.append(run(X[i],Y[i]))
	res1.append(res[i][0])
	res2.append(res[i][1])

plt.scatter(res1,res2)
plt.show()
'''
