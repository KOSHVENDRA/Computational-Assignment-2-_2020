# date 20/04/2020
# solving an IVP for very large value of independent variable by RK4 method
# diff. eqn :   x'(t)=1/(x*x+ t*t)    0 <= t< inf    ,x(0)=1   , x(3500000)=?

import numpy as np
import matplotlib.pyplot as plt

def func(t,x):
    return( 1/ (x*x +t*t))            # r.h.s. of differential equation

def adap_rk4(t,x,h):
    k1= func(t,x)
    k2= func(t+(h/2),x+(0.5*h*k1) )
    k3= func(t+(h/2),x+(0.5*h*k2) )
    k4= func(t+h , x+ (h*k3))
    return(x+ (h/6)*(k1+ (2*k2) +(2*k3) +k4))




x = 1
x_sol=[x]                           # solution array with initial element
t_i =  0                              # initial value of t
err= 0.001
t_arr=[0]
h=0.5                             # initial mess point interval
t=1                                  # initialing t

while(t<=3500000):
    k=adap_rk4(t,x,h)  
    x_sol.append(k)              # updating solution array
    m=x_sol[-1] -x_sol[-2]
    ab_err=np.absolute(m)
    
    if ab_err > err :                 # if condition doesn't satisfies, we return to original status with reduced step size
        t=t
        x_sol=x_sol[:-1]
        h=h/2
    else:
        
        h=2*h
        t=t+h
        t_arr.append(t)             # updating time array
        x=x_sol[-1]

x_ans=x_sol[-1]
print('the value of x at t = 3500000 :',x_ans)

