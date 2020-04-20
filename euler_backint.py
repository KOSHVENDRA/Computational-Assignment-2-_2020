#    date :05-04-2020
#  SOLVING DIFFERENTIAL EQUATION BY BACKWARD EULER METHOD
# 1.) Diff. equation :  dy/dx = -9y

import numpy as np
import matplotlib.pyplot as plt

h=0.01                    # distancebetween consecutive mesh points
w=np.exp(1)               # initial condition
x=np.arange(0,1.01,h)     # creating meshpoints on x axis
y_euler=[np.exp(1)]       # an array for y values at meshpoints,includes initial point
for i in range(100):
    w=w/(1+9*h)
    y_euler.append(w)     # updating y values at meshpoints

y_exact=np.exp(1-9*x)     # exact solution of given diff eqn

plt.plot(x,y_exact,'g',label='exact solution')
plt.plot(x,y_euler,'ro',label='sol by backward euler method')
plt.legend()
plt.show()


# 2.) Diff. equation : dy/dx = -20*(y-x)**2 + 2*x   ; 0<= x <=1

from scipy.optimize import newton 

h=0.01
x_0=0
y_0=1/3
sol=[y_0]
def func(u,v,w):
    return(u - v - 0.02*w + 0.2*((u-w)**2))
for i in range(len(x)-1):
    x_0=x_0 +h
    y_0= newton(func,y_0,args=(y_0,x_0))
    sol.append(y_0)

plt.plot(x,sol,'yo')
plt.show()
    
