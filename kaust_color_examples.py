#!/usr/bin/python

import numpy
import matplotlib.pyplot
import matplotlib.colors
import pylab

import kaust_colors

pylab.figure()
xs = pylab.linspace(-2,2,200)
colors = ('blue','orange','yellow','green')
for n in range(0,len(colors)):
    pylab.plot(xs,xs**n,'k-',color=kaust_colors.KAUSTColor(colors[n]),label='x^%d'%(n,))
pylab.grid(True)
pylab.legend()
pylab.title('powers of x in kaust colors')
pylab.savefig('example 1.pdf')

matplotlib.pyplot.figure()
c = matplotlib.colors.ColorConverter().to_rgb
rvb = kaust_colors.KAUSTColorMap()
N = 1000
array_dg = numpy.random.uniform(0, 10, size=(N, 2))
colors = numpy.random.uniform(-2, 2, size=(N,))
matplotlib.pyplot.scatter(array_dg[:, 0], array_dg[:, 1], c=colors, cmap=rvb)
matplotlib.pyplot.colorbar()
matplotlib.pyplot.title('scatter plot with the kaust colors')
matplotlib.pyplot.savefig('example 2.pdf')
