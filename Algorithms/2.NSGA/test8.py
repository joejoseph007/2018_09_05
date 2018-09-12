import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt
import random



def B_spline(x,y,col,qwe=0,wid=0.5,numb=500):

    # uncomment both lines for a closed curve
    #x=np.append(x,[x[0]])  
    #y=np.append(y,[y[0]])

    l=len(x)  

    t=np.linspace(0,1,l-2,endpoint=True)
    t=np.append([0,0,0],t)
    t=np.append(t,[1,1,1])

    tck=[t,[x,y],3]
    u3=np.linspace(0,1,(max(l*2,numb)),endpoint=True)
    out = interpolate.splev(u3,tck)



    if qwe==1:
        plt.plot(x,y,'k--',label='Control polygon',marker='.',markerfacecolor='red')
    plt.ylim(-20,20)
    plt.xlim(-1,20)

    #plt.plot(x,y,'ro',label='Control points only')
    plt.plot(out[0],out[1],'%s'%col,linewidth=wid,label='B-spline curve')
    #plt.legend(loc='best')
    #plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    #plt.title('Cubic B-spline curve evaluation')
    #plt.show()


number=20
x=np.zeros(number)
y=np.zeros(number)
i=1
while i<(number):
    y[i]=random.uniform(-10,10)
    x[i]=i#+random.uniform(-0.5,0.5)
    i+=1
y[i-1]=0

B_spline(x,y,'black',1,2)

plt.savefig('check2/0.0.svg')
#plt.close()





#y1=np.zeros(number)
    
for j in range(100):
    i=1
    sigma=0.5/(j+1)**0.5
    #sigma=0.2
    #print (sigma)
    y1=y
    while i<(number-1):
        y1[i]=np.random.normal(y[i],(10+10)*sigma)
        i+=1
    
    #print(y[2],y1[2],np.random.normal(y[2],(10+10)*sigma))
    
    B_spline(x,y1,'blue')
    plt.savefig('check2/%i.svg'%j)
    #plt.close()


