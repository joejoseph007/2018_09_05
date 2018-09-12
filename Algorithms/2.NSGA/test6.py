import numpy as np
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt
import random

x = np.array([ 0. ,  1.2,  1.9,  3.2,  4. ,  6.5])
y = np.array([ 0. ,  2.3,  3. ,  4.3,  2.9,  3.1])

number=10

x=np.zeros(number)
y=np.zeros(number)
for i in range(number):
	y[i]=random.uniform(-10,10)
	x[i]=i+random.uniform(-0.5,0.5)

t, c, k = interpolate.splrep(x, y, s=0, k=4)


#'''
print('''\
t: {}
c: {}
k: {}
'''.format(t, c, k))
#'''
N = 100
xmin, xmax = x.min(), x.max()
xx = np.linspace(xmin, xmax, N)
spline = interpolate.BSpline(t, c, k, extrapolate=False)

plt.plot(x, y, 'bo', label='Original points')
plt.plot(xx, spline(xx), 'r', label='BSpline')
plt.grid()
plt.legend(loc='best')
plt.show()
