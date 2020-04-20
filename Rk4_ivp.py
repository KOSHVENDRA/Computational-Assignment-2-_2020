# date 20/04/2020
# solving simultaneous differential equations by RK4 method
#  x'= x+2y -2z +exp(-t)
#  y'= y+z-2 *exp(-t)
#  z'= x+2y +exp(-t)
#  0<= t<= 1        ; x(0)=3  , y(0)=-1   ,z(0) = 1


import numpy as np
import matplotlib.pyplot as plt

h=0.1
t=np.arange(0,1,h)                        # mess points

x =[3]
y =[-1]                                # solution array with initial values
z =[1]

def func1(x,y,z,t):
    return( x+2*y -2*z +np.exp(-t))       # functions from r.h.s. of diff. eqn

def func2(x,y,z,t):
    return(y+z-2 *np.exp(-t))

def func3(x,y,z,t):
    return(x+2*y+np.exp(-t))

for i in range(len(t)-1):

    k1_x = func1(x[i],y[i],z[i],t[i])
    k1_y = func1(x[i],y[i],z[i],t[i])
    k1_z = func1(x[i],y[i],z[i],t[i])

    k2_x =func1(x[i]+0.5*h*k1_x,y[i]+0.5*h*k1_y,z[i]+0.5*h*k1_z,t[i]+0.5*h)
    k2_y =func1(x[i]+0.5*h*k1_x,y[i]+0.5*h*k1_y,z[i]+0.5*h*k1_z,t[i]+0.5*h)
    k2_z =func1(x[i]+0.5*h*k1_x,y[i]+0.5*h*k1_y,z[i]+0.5*h*k1_z,t[i]+0.5*h)

    k3_x =func1(x[i]+0.5*h*k2_x,y[i]+0.5*h*k2_y,z[i]+0.5*h*k2_z,t[i]+0.5*h)
    k3_y =func1(x[i]+0.5*h*k2_x,y[i]+0.5*h*k2_y,z[i]+0.5*h*k2_z,t[i]+0.5*h)
    k3_z =func1(x[i]+0.5*h*k2_x,y[i]+0.5*h*k2_y,z[i]+0.5*h*k2_z,t[i]+0.5*h)

    k4_x =func1(x[i]+h*k3_x,y[i]+h*k3_y,z[i]+h*k3_z,t[i]+h)
    k4_y =func1(x[i]+h*k3_x,y[i]+h*k3_y,z[i]+h*k3_z,t[i]+h)
    k4_z =func1(x[i]+h*k3_x,y[i]+h*k3_y,z[i]+h*k3_z,t[i]+h)

    x_s =x[i] + (h/6)*(k1_x +2*k2_x +2*k3_x +k4_x)
    y_s =y[i] + (h/6)*(k1_y +2*k2_y +2*k3_y +k4_y)
    z_s =z[i] + (h/6)*(k1_z +2*k2_z +2*k3_z +k4_z)

    x.append(x_s)
    y.append(y_s)
    z.append(z_s)


plt.plot(t,x,'g',label='x-solution')
plt.plot(t,y,'r',label='y-solution')
plt.plot(t,z,'b',label='z-solution')
plt.xlabel('t')
plt.ylabel('solution')
plt.legend()
plt.show()
