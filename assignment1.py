
from neuron import h

from neuron.units import ms, mV

h.load_file('stdrun.hoc')

get_ipython().run_line_magic('matplotlib', 'notebook')

soma =h.Section(name='soma')
dend =h.Section(name='dend')

soma.insert('hh')
dend.insert('hh')

dend.connect(soma)

syn1 = h.ExpSyn(soma(0.5)
syn1.tau = 1 * ms

s1= h.NetStim()
s1.number = 1
s1.start = 10 * ms

con1= h.NetCon(s1, syn1)
con1.delay = 0
con1.weight[0] = 1

syn2 = h.Exp2Syn(soma(0.5))
syn2.tau1 = 1 * ms
syn2.tau2 = 2 * ms
syn2.e = 0

s2= h.NetStim()
s2.number = 1
s2.start = 10 * ms

con2 = h.NetCon(s2, syn2)
con2.delay = 2 * ms
con2.weight[0] = 0.432

v = h.Vector().record(soma(0.5)._ref_v)          
t = h.Vector().record(h._ref_t)   

h.finitialize(-65 * mV)
h.continuerun(25 * ms)

from bokeh.io import output_notebook
import bokeh.plotting as plt
output_notebook()

f = plt.figure(x_axis_label='v', y_axis_label='t')
f.line(t, v, line_width=2)
plt.show(f)





