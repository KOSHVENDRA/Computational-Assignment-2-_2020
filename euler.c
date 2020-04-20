// date 20/04/ 2020
// euler's method for solving differential equation
// diff eqn : y' = t-t*t +1  ; 0<= t <=2    ,y(0) =0.5

#include<stdio.h>
#include<math.h>

float func(float t,float y)
{
  float f;
  f= t-t*t +1;                // r.h.s. of differential equation
  return f;
}

float funct(float t,float y)
{ float g;
  g= (t*t)/2-(t*t*t)/3 +t + 0.5;
  return g;
}

void main()
{
  float t,y,h,t_upper,k,l,diff;
  
  h=0.2;
  t=0;                                // initial value of t
  y=0.5 ;                             // since y(0)=0.5
  t_upper=2;                           // upper limit of t

  while(t<= t_upper)
    {
      l=funct(t,y);
      diff=l-y;                          // difference b/w exact and numerical sol
      k= h*func(t,y);
      y=y+k;
      t=t+h;
      printf("%0.3f\t %0.3f\t %0.3f\n",t,y,diff);
      
    }
}
