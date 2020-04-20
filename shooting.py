# date 20/04/2020
# shooting method for solving boundary value problem
# diff. eqn : x''(t) = -10   ,x(0)=0 ,x(10)=0

import numpy as np
import matplotlib.pyplot as plt

h=0.1
t=np.arange(0,10,h)                   # mess points

x_ini =0
x_fin =0

def fun_1(u,v,w):
    return(-10)                      # function from decoupling the diff. eqn
def fun_2(u,v,w):
    return(v)

r_guess=[47,48,49,50,51,52,53]        # initial points guess of r=x'(t)
last_elem=[]                          # to contain the last element of each solution

for i in range(len(r_guess)):
    r_sol=[r_guess[i]]
    x_sol=[0]
    
    for j in range(len(t)-1):
        k1_r=fun_1(x_sol[j],r_sol[j],t[i])
        k1_x=fun_2(x_sol[j],r_sol[j],t[i])
        
        k2_r=fun_1(x_sol[j]+0.5*h*k1_x,r_sol[j]+0.5*h*k1_r,t[i]+0.5*h)
        k2_x=fun_2(x_sol[j]+0.5*h*k1_x,r_sol[j]+0.5*h*k1_r,t[i]+0.5*h)
        
        k3_r=fun_1(x_sol[j]+0.5*h*k2_x,r_sol[j]+0.5*h*k2_r,t[i]+0.5*h)
        k3_x=fun_2(x_sol[j]+0.5*h*k2_x,r_sol[j]+0.5*h*k2_r,t[i]+0.5*h)
        
        k4_r=fun_1(x_sol[j]+h*k3_x,r_sol[j]+h*k3_r,t[i]+h)
        k4_x=fun_2(x_sol[j]+h*k3_x,r_sol[j]+h*k3_r,t[i]+h)

        x= x_sol[j]+(h/6)*(k1_x+ 2*k2_x + 2*k3_x +k4_x)
        r= r_sol[j]+(h/6)*(k1_r+ 2*k2_r + 2*k3_r +k4_r)

        x_sol.append(x)                  # updating solution array
        r_sol.append(r)

    last_elem.append( np.absolute(x_sol[len(t)-1]) )
    plt.plot(t,x_sol,'g')

j= np.argmin(last_elem)        # x(10)=0, so it is not subtracted from last_elem
print(j)
#  j gives 3 (running the code), means fourth element of r_guess corresponds to correct answer 

x_exact= -5* t**2 + 50*t

plt.plot(t,x_exact,'r',label='exact solution')
plt.xlabel('t')
plt.ylabel('x')
plt.legend()
plt.show()
