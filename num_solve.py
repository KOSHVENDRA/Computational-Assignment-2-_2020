# date 20/04/2020
# solving differential equation using numpy functions

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# 1.)  y'= t*exp(3t) -2y    ; 0<=t<=1    ; y(0)=0

t1=np.linspace(0,1,30)
def fun1(t,y):
    return(t*np.exp(3*t)-2*y)

sol1=solve_ivp(fun1,[0,1],[0],t_eval=np.linspace(0,1,20))
sol1_exact= 0.04* ( np.exp(-2*t1) - np.exp(3*t1) +5*np.exp(3*t1)*t1  )

plt.plot(sol1.t,sol1.y[0],label='numerical solution')
plt.plot(t1,sol1_exact,'ro',label='exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()


#2.) y'= 1-(t-y)**2     ;2<=t<=3    ,y(2)=0

t2=np.linspace(2,3,30)
def fun2(t,y):
    return(1-(t-y)**2)

sol2=solve_ivp(fun2,[2,3],[0])
sol2_exact = (2- 5*t2 + 2*t2**2) / ( 2*t2  - 5)

plt.plot(sol2.t,sol2.y[0],'b',label='numerical solution')
plt.plot(t2,sol2_exact,'ro',label='exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()


# 3.)    y' =1+y/t   ; 1<= t <=2    ;y(1)=2

t3=np.linspace(1,2,30)
def fun3(t,y):
    return(1 + y/t)

sol3=solve_ivp(fun3,[1,3],[2],t_eval=np.linspace(1,2,20))
sol3_exact = 2*t3 + t3* np.log(t3)

plt.plot(sol3.t,sol3.y[0],label='numerical solution')
plt.plot(t3,sol3_exact,'ro',label='exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()

# 4.)   y'= cos(2t) +sin(3t)     ;0<= t<= 1  ;y(0) =1

t4=np.linspace(0,1,30)
def fun4(t,y):
    return(np.cos(2*t)+np.sin(3*t))

sol4=solve_ivp(fun4,[0,1],[1],t_eval=np.linspace(0,1,20))
sol4_exact = (1/6)* ( 8-2* np.cos(3*t4) + 3* np.sin(2*t4))

plt.plot(sol4.t,sol4.y[0],label='numerical solution')
plt.plot(t4,sol4_exact,'ro',label='exact solution')
plt.xlabel('t')
plt.ylabel('y')
plt.legend()
plt.show()
