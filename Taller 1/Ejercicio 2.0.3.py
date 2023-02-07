#!/usr/bin/env python
# coding: utf-8

# In[47]:


import matplotlib.pyplot as plt


# In[48]:


succ = [0, 1]


# In[49]:


for i in range (2, 21):
    i_1 = succ[i-1]
    i_2 = succ[i-2]
    
    new = i_1 + i_2
    
    succ.append(new)


# In[50]:


plt.plot(succ, color = "green")
plt.legend(["Sucesión de Fibonacci"], loc=2)

plt.show()


# In[51]:


num_aur = 1.618033988749894
aur_est = []


# In[52]:


for i in range (1, len(succ)-1):
    next_f = succ[i+1]
    current_f = succ[i]
    
    est = next_f/current_f
    
    aur_est.append(est)


# In[41]:


plt.plot(aur_est)
plt.axhline(num_aur, color = "red", linestyle = "dashed")
plt.legend(["Estimación usando la serie", "Número áureo"], loc=0)

plt.show()

