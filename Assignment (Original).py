#!/usr/bin/env python
# coding: utf-8

# In[17]:


from neuron import h


# In[18]:


from neuron.units import ms, mV


# In[19]:


h.load_file('stdrun.hoc')


# In[20]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[21]:


soma =h.Section(name='soma')
dend =h.Section(name='dend')


# In[22]:


soma.insert('hh')
dend.insert('hh')


# In[23]:


dend.connect(soma)


# In[24]:


syn = h.Exp2Syn(soma(0.3))
syn.tau1 = 0
syn.tau2 = 0
syn.e = 0


# In[25]:


s= h.NetStim()
s.number = 2
s.start = 0


# In[26]:


nc = h.NetCon(s, syn)
nc.delay = 1 * ms
nc.weight[0] = 0.04


# In[27]:


v = h.Vector().record(soma(0.5)._ref_v)          
t = h.Vector().record(h._ref_t)   


# In[28]:


h.finitialize(-65 * mV)
h.continuerun(25 * ms)


# In[29]:


from bokeh.io import output_notebook
import bokeh.plotting as plt
output_notebook()


# In[30]:


f = plt.figure(x_axis_label='v', y_axis_label='t')
f.line(t, v, line_width=2)
plt.show(f)


# In[ ]:




