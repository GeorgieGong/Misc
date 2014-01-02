#!/usr/bin/python

import numpy
import matplotlib.pyplot
import matplotlib.colors
import pylab
import mpl_toolkits.mplot3d.axes3d
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

# the following stolen from http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb
alpha = 0.7
phi_ext = 2 * pylab.pi * 0.5
def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * pylab.cos(phi_p)*pylab.cos(phi_m) - alpha * pylab.cos(phi_ext - 2*phi_p)

phi_m = pylab.linspace(0, 2*pylab.pi, 50)
phi_p = pylab.linspace(0, 2*pylab.pi, 50)
X,Y = pylab.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T

fig = matplotlib.pyplot.figure()

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 1, 1, projection='3d')

# surface_plot with color grading and color bar
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=kaust_colors.KAUSTColorMap(), linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
ax.set_title('A weird 2D potential field in KAUST colors')
ax.set_ylabel('y')
ax.set_xlabel('x')
ax.set_zlabel('V(x,y)')
matplotlib.pyplot.savefig('example 3.pdf')
