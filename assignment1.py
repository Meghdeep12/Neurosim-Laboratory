
from neuron import h

from neuron.units import ms, mV

h.load_file('stdrun.hoc')

get_ipython().run_line_magic('matplotlib', 'notebook')

soma =h.Section(name='soma')
dend =h.Section(name='dend')

soma.insert('hh')
dend.insert('hh')

dend.connect(soma)

syn = h.Exp2Syn(soma(0.3))
syn.tau1 = 0
syn.tau2 = 0
syn.e = 0

s= h.NetStim()
s.number = 2
s.start = 0

nc = h.NetCon(s, syn)
nc.delay = 1 * ms
nc.weight[0] = 0.04

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





