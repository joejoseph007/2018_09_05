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


def check(Arr,T,Z=[0]):
	xmax=5
	xmin=0
	ymax=3
	ymin=0
	
	if T==0:
		def constraint1(Arr): 
			value = (Arr[0][0]-5)**2+Arr[0][1]**2
			if value<=25:
				return 1
			else:
				return 0

		#Second function to optimize
		def constraint2(Arr):
			value = (Arr[0][0]-8)**2+(Arr[0][1]+3)**2
			if value>=7.7:
				return 1
			else:
				return 0
		if constraint1(Arr) and constraint2(Arr):
			if Arr[0][0]<=5 and Arr[0][0]>=0:
				if Arr[0][1]<=3 and Arr[0][1]>=0:
					return 1
		else:
			return 0

	elif T==1:
		Range=numpy.zeros((Z[0],Z[1],2))
		Range[0][0][0]=xmin
		Range[0][1][0]=ymin
		Range[0][0][1]=xmax
		Range[0][1][1]=ymax
		return Range

print (check([0,0],1,[1,2]))
'''
#print check(0,5)

print (check([],1,[1,2]))

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
	res.append(run([X[i],Y[i]]))
	res1.append(res[i][0])
	res2.append(res[i][1])

plt.scatter(res1,res2)
plt.show()
'''
