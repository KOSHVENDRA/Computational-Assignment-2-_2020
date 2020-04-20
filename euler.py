#  date 11/04/2020
#  Diff. equation : dy/dt = y/t - (y/t)**2  ,  1 <= t <= 2

import numpy as np
import matplotlib.pyplot as plt

h=0.1                               # distance between mess points
t=np.arange(1,2.1,h)                # an array of mess points
t_0=1
y_1=1                               # initial condition
y=[y_1]                             # solution array

def func(u,v):
    return(h*(u/v)*(1-(u/v)))       # h*dy/dt

for i in range(len(t)-1):          
    k= y[i] + func(y[i],t[i])       # euler method's approximated value at alternate mess points
    y.append(k)                     # updating solution arange

y_exact= t/(1+np.log(t))            # exact solution

plt.plot(t,y,'b',label='numerically approximated solution')
plt.plot(t,y_exact,'r',label='exact solution')
plt.title("solving by euler's method ")
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

error =0                             # initiating the error term
for i in range(len(t)):
    error=error+(y_exact[i]-y[i])    # error in corresponding terms

absolut_error=(np.absolute(error))/11     # 11 mess points

erro_r=0
for i in range(len(t)):
    erro_r=erro_r + ((y_exact[i]-y[i])/y_exact[i])

relat_error=(np.absolute(erro_r))/11

print('absolute error is :', absolut_error)
print('relative error is :', relat_error)
