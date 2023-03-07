#!/usr/bin/env python
# coding: utf-8

# In[14]:


import numpy as np
import matplotlib.pyplot as plt

#initial conditions
beta = 1
d_beta = 0
x = 0 # x=mu^2(M/M_s)
dx = 10**-2 #step size

beta1 = [beta]
d_beta1 = [d_beta]
x1 = [x]

while x <= 100000 and beta >= 0:
    
    x = x + dx
    beta = beta + dx * d_beta
    d_beta = -0.006 * x * beta ** 4 / (0.012 * x**2 * beta ** 3 + 1)
    
    x1.append(x)
    beta1.append(beta)
    d_beta1.append(d_beta)


# In[19]:


#Plot of beta against log(mu^2(M/M_s))
log_x = [np.log10(i) for i in x1]
plt.plot(log_x,beta1)
plt.xlabel('log(μ^2 M/M_☉)')
plt.ylabel('β')
plt.xlim(0.0,1.05)
plt.ylim(0.0,1.05)
plt.show()


# In[20]:


#log-log plot of beta against mu^2(M/M_s)
plt.plot(x1,beta1)
plt.xlabel('μ^2(M/M_☉)')
plt.ylabel('β')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1,)
plt.ylim(0.01,1.0)
plt.show()


# In[22]:


#log-log plot of 1-beta against mu^2(M/M_s)
beta_minus = [1-i for i in beta1]
plt.plot(x1,beta_minus)
plt.xlabel('μ^2(M/M_☉)')
plt.ylabel('1-β')
plt.xscale('log')
plt.yscale('log')
plt.xlim(0.1,)
plt.ylim(0.00001,)
plt.show()

