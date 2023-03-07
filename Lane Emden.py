#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

n1 = [0,1,2,3,3.25,4,5]
for n in n1 :
    u = 1
    v = 0
    xi = 10**-8 # not 0 to prevent the problem of dividing by 0
    delta_xi = 10**-3 # step size
   
    u1  = [u]
    xi1 = [xi]
    v1 = [v]

    while xi < 30 and u >= 0:

        xi = xi + delta_xi
        u = u + delta_xi * v
        dv = -2 * v / xi - u ** n
        v = v + delta_xi * dv
               
        u1.append(u)
        xi1.append(xi)
        v1.append(v)

    # Estimate the x-intercept using interpolation
    if u < 0 :
        v = v + delta_xi * dv  
        xi2 = xi + delta_xi                                 
        xi3 = xi2 + delta_xi                                
        u2 = u + delta_xi * v        
        u3 = u2 + delta_xi * v       

        def interpolation(x):          
            inter = ((-u2*(xi3-xi2)) / (u3-u2)) + xi2  
            return inter          
        xi_r = interpolation(0)   
        v = v + delta_xi * dv
        print('The value of ξ1 is = {:.3f} when n = {} and v is {}.'.format(xi_r, n, v))

    plt.plot(xi1,u1, label='n=%s'%n)
    plt.xlabel('ξ')
    plt.ylabel('θ')
    plt.legend()
    plt.ylim(0.0,1.0)
    plt.xlim(0,30)  
plt.show()


# In[2]:


n1 = [3.25]
for n in n1 :
    u = 1
    v = 0
    xi = 10**-8 # not 0 to prevent the problem of dividing by 0
    delta_xi = 10**-3 # step size
   
    u1  = [u]
    xi1 = [xi]
    v1 = [v]

    while xi < 30 and u >= 0:

        xi = xi + delta_xi
        u = u + delta_xi * v
        dv = -2 * v / xi - u ** n
        v = v + delta_xi * dv
               
        u1.append(u)
        xi1.append(xi)
        v1.append(v)

    # Estimate the x-intercept using interpolation
    if u < 0 :
        v = v + delta_xi * dv  
        xi2 = xi + delta_xi                                 
        xi3 = xi2 + delta_xi                                
        u2 = u + delta_xi * v        
        u3 = u2 + delta_xi * v       

        def interpolation(x):          
            inter = ((-u2*(xi3-xi2)) / (u3-u2)) + xi2  
            return inter          
        xi_r = interpolation(0)   
        v = v + delta_xi * dv
        print('The value of ξ1 is = {:.3f} when n = {} and v is {}.'.format(xi_r, n, v))

    plt.plot(xi1,u1, label='n=%s'%n)
    plt.xlabel('ξ')
    plt.ylabel('θ')
    plt.legend()
    plt.ylim(0.0,1.0)
    plt.xlim(0,30)  
plt.show()


# In[3]:


M_s = 1.99 * 10**33
R_s = 6.96 * 10**10
n = 3.25
xi_1 = 8.024
v_1 = -0.03024
G = 6.67 * 10**-8
rho_c = -M_s/(4*np.pi*R_s**3/3) * (xi_1/3/v_1)
P_c = G*M_s**2/R_s**4 * (4*np.pi*(n+1)*v_1**2)**-1
K = 4*np.pi*G/(n+1) * 1/rho_c**((1-n)/n) * (R_s/xi_1)**2
print('The central density is {} g cm^-3.'.format(rho_c))
print('The central pressure is {} dyne cm^-2'.format(P_c))
print('The polytropic constant K is {}'.format(K))


# In[4]:


r = [i*((n+1)*K*rho_c**((1-n)/n)/(4*np.pi*G))**0.5 for i in xi1]
x = [i/R_s for i in r]
rho = [rho_c*i**n for i in u1]

plt.plot(x,rho)
plt.xlabel('r/R☉')
plt.ylabel('ρ')
plt.ylim(0.0,130.0)
plt.xlim(0,1.1)
plt.show()


# In[5]:


m = [4*np.pi*((n+1)*K/(4*np.pi*G))**1.5 * rho_c**((3-n)/(2*n)) * -i1**2*i2 for i1,i2 in zip(xi1,v1)]
plt.plot(x,m)
plt.xlabel('r/R☉')
plt.ylabel('m')
plt.xlim(0,1.1)
plt.ylim(0,)
plt.show()


# In[6]:


P = [K * rho_c**((n+1)/n) * i**(n+1) for i in u1]
plt.plot(x,P)
plt.xlabel('r/R☉')
plt.ylabel('P')
plt.xlim(0,1.1)
plt.ylim(0,)
plt.show()

