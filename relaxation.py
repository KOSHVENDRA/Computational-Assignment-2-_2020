# date 20/04/2020
# solving boundary value problem by relaxation method
# differential equation :  x''(t)=-10   , 0 <=t<= 10     , x(0)=0  ,x(10) =10

import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse.linalg as sl
import numpy.linalg as nul
from scipy.sparse import csc_matrix

h = 0.1                             # mess point interval
t = np.arange(0,10,h)               # mess points
x_0 = 0                             # initial value
x_f = 0                             # final value
t_f = 10

num= int((t_f-t[0])/h) +1            # defining a number for further use

I1_mat=np.identity(num-3)             # an identity matrix
I2_mat=np.identity(num-2)
I1_mat=(-2*I1_mat)+I2_mat[1:num-2,0:num-3] + I2_mat[0:num-3,1:num-2]
I1_mat=I1_mat/ h**2
I1_mat=csc_matrix(I1_mat,dtype =float)   # creates compressed sparse coulum matrix
f = -10*np.ones(num-3)
f[0]=f[0] - x_0
f[num-4] = f[num-4] - x_f
x = np.zeros(num-1)
x[1:num-2]=sl.spsolve(I1_mat,f)
x[0] = x_0
x[num-2] = x_f

# for getting family curves

num2=np.linspace(-16,0,12)               # an array,here minus sign is used otherwise famil curves are inverted
for i in num2:
    g=i*np.ones(num-3)
    h=np.zeros(num-1)
    h[1:num-2]=sl.spsolve(I1_mat,g)
    h[0] = x_0
    h[num-2]= x_f
    plt.plot(t,h,'g')

x_exact = -5*(t**2) + 50*t             # exact solution

plt.plot(t,x_exact,'r--',label='exact solution')
plt.xlabel('t')
plt.ylabel('x')
plt.title('boundary value problem by relaxation method')
plt.legend()
plt.show()
