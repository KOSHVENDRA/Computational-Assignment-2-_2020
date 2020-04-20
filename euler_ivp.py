# date 20/04/2020
# solving second order initial valued differential equation by euler method
# differential equation  : (t*t)y'' - 2ty' +2y = (t**3)ln(t)
# initial values  :   y(1)=1 ,y'(1)=0 ,      1<= t <= 2


import numpy as np
import matplotlib.pyplot as plt

h=0.001
t=np.arange(1,2,h)

# take y'= z     s.t   z(1)=0    &  z' = 2z/t -2y/(t*t) + (lnt)/t

def func1(u,v,w):
    return(v)
def func2(u,v,w):
    return( -2*u/(w*w) + (2*v)/w + (np.log(w))/w  )

y =[1]
z =[0]                     # solution array with initial values

for i in range(len(t)-1):
    y_next = y[i] + h*func1(y[i],z[i],t[i])       # solution at next mess point
    z_next = z[i] + h*func2(y[i],z[i],t[i])     

    y.append(y_next)                              # updating th solution array
    z.append(z_next)

y_exact = (7/4)*t + ((t**3)/2) * np.log(t) - (3/4)*(t**3)

plt.plot(t,y,'r',label='numerical solution')
plt.plot(t,y_exact,'g',label='exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
