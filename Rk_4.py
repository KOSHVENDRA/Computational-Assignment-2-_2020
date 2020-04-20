# Solving 2nd differential equation by 4th order runge kutta method
# date 19/04/2020
# Differential Equation: y'' - 2y' + y = x*exp(x) - x
# y(0) = 0  , y'(0) = 0       ,    0<= x <=1

import numpy as np
import matplotlib.pyplot as plt

h=0.1                                   # step size of mess points
x = np.arange(0,1,h)                    # mess points
y_0=0                                   # initial condition
z_0=0                                   # initial condition  , (y' = z)

def fun_1(u,v,w):                       # functions after decopling diff. eqn
    return(u)
def fun_2(u,v,w):
    return(2*u-v+w*np.exp(w)-w)

y_sol=[0]
z_sol=[0]                                #  array for solution elements

for i in range(len(x)-1):
    k1_y=fun_1(z_sol[i],y_sol[i],x[i])
    k1_z=fun_2(z_sol[i],y_sol[i],x[i])
    k2_y=fun_1(z_sol[i]+h*k1_z*0.5 ,y_sol[i]+ 0.5*h*k1_y ,x[i]+h*0.5)
    k2_z=fun_2(z_sol[i]+h*k1_z*0.5 ,y_sol[i]+ 0.5*h*k1_y ,x[i]+h*0.5)
    k3_y=fun_1(z_sol[i]+h*k2_z*0.5 ,y_sol[i]+ 0.5*h*k2_y ,x[i]+h*0.5)
    k3_z=fun_2(z_sol[i]+h*k2_z*0.5 ,y_sol[i]+ 0.5*h*k2_y ,x[i]+h*0.5)
    k4_y=fun_1(z_sol[i]+h*k3_z ,y_sol[i]+ h*k3_y ,x[i]+h)
    k4_z=fun_2(z_sol[i]+h*k3_z ,y_sol[i]+ h*k3_y ,x[i]+h)

    y= y_sol[i] + (h/6)*(k1_y +2*k2_y +2*k3_y +k4_y)
    z= z_sol[i] + (h/6)*(k1_z +2*k2_z +2*k3_z +k4_z)

    y_sol.append(y)                     # updating solution array
    z_sol.append(z)
    
plt.plot(x,y_sol,'g',label='numerical solution')
plt.xlabel('x')
plt.xlabel('y')
plt.legend()
plt.show()
