import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as plt

def scipy_bspline(cv,n,degree):
    """ bspline basis function
        c        = list of control points.
        n        = number of points on the curve.
        degree   = curve degree
    """
    # Create a range of u values
    c = cv.shape[0]
    kv = np.clip(np.arange(c+degree+1)-degree,0,c-degree)
    u  = np.linspace(0,c-degree,n)

    # Calculate result
    return np.array(si.splev(u, (kv,cv.T,degree))).T

cv = np.array([[ 50.,  25.,],
       [ 59.,  12., ],
       [ 50.,  10., ],
       [ 57.,   2., ],
       [ 40.,   4., ],
       [ 40.,   14.,]])


n = 100  # 100k Points
degree = 2 # Curve degree
points_scipy = scipy_bspline(cv,n,degree) #cProfile clocks this at 0.012 seconds

#print (points_scipy)
#print(cv[0:len(cv)][0],cv[0:len(cv)][1])

plt.plot(points_scipy)
plt.plot(cv)
#plt.scatter(cv[:][0],cv[:][1])
plt.show()