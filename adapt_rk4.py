# date 20/04/2020
# solving differential equation using adaptive size Rk4 method
# diff. equn :  y' = (y*y +y)/t     ,1 <=t<= 3     ,y(1)= -2

import numpy as np
import matplotlib.pyplot as plt

def func(t,y):
    return((y*y + y) / t)            # r.h.s. of differential equation

def adap_rk4(t,y,h):
    k1= func(t,y)
    k2= func(t+(h/2),y+(0.5*h*k1) )
    k3= func(t+(h/2),y+(0.5*h*k2) )
    k4= func(t+h , y+ (h*k3))
    return(y+ (h/6)*(k1+ (2*k2) +(2*k3) +k4))




y = -2
y_sol=[y]                           # solution array with initial element
t_i = 1                                # initial value of t
err= 0.0001
t_arr=[1]
h=0.01                             # initial mess point interval
t=1                                  # initialing t

while(t<=3):
    k=adap_rk4(t,y,h)
    t=t+h
    t_arr.append(t)
    y_sol.append(k)
    m=y_sol[-1] -y_sol[-2]
    ab_err=np.absolute(m)
    
    if ab_err > err :  # if condition doesn't satisfies, we return to original status
        t_arr=t_arr[:-1]
        y_sol=y_sol[:-1]
        h=h/2
    else:
        h=2*h
        y=y_sol[-1]
        

plt.plot(t_arr,y_sol,'r--',label='numerical solution')
plt.xlabel('t')
plt.ylabel('y')
plt.title('solution by adaptive size control in RK4 method')
plt.legend()
plt.show()        
        
        

    
    
    
    
    
    
    
