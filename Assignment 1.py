#!/usr/bin/env python
# coding: utf-8

# In[129]:


from neuron import h


# In[130]:


from neuron.units import ms, mV


# In[131]:


h.load_file('stdrun.hoc')


# In[132]:


get_ipython().run_line_magic('matplotlib', 'notebook')


# In[133]:


soma =h.Section(name='soma')
dend =h.Section(name='dend')


# In[134]:


soma.insert('hh')
dend.insert('hh')


# In[135]:


dend.connect(soma)


# In[136]:


syn0 = h.ExpSyn(soma(0.5))
syn0.tau = 1
syn0.e = 0


# In[137]:


syn = h.Exp2Syn(soma(0.5))
syn.tau1 = 0
syn.tau2 = 0
syn.e = 0


# In[138]:


s= h.NetStim()
s.number = 2
s.start = 0


# In[139]:


nc = h.NetCon(s, syn)
nc.delay = 1 * ms
nc.weight[0] = 0.04


# In[140]:


nc = h.NetCon(s, syn0)
nc.delay = 1 * ms
nc.weight[0] = 0.04


# In[141]:


v = h.Vector().record(soma(0.5)._ref_v)          
t = h.Vector().record(h._ref_t)   


# In[142]:


h.finitialize(-65 * mV)
h.continuerun(25 * ms)


# In[143]:


from bokeh.io import output_notebook
import bokeh.plotting as plt
output_notebook()


# In[144]:


f = plt.figure(x_axis_label='v', y_axis_label='t')
f.line(t, v, line_width=2)
plt.show(f)


# In[ ]:




