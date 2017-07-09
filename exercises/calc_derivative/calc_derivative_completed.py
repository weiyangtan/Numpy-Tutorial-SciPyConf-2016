# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Calculate Derivative
--------------------

Topics: NumPy array indexing and array math.

Use array slicing and math operations to calculate the
numerical derivative of ``sin`` from 0 to ``2*pi``.  There is no
need to use a 'for' loop for this.

Plot the resulting values and compare to ``cos``.

Bonus
~~~~~

Implement integration of the same function using Riemann sums or the
trapezoidal rule.

See :ref:`calc-derivative-solution`.
"""
from numpy import linspace, pi, sin, cos, cumsum
from matplotlib.pyplot import plot, show, subplot, legend, title, close, savefig

close('all')

# calculate the sin() function on evenly spaced data.
x = linspace(0,2*pi,101)
y = sin(x)
deriv2 = cos(x) #mathematical derivative of sine x is cosine x

dy = y[1:] - y[:-1]
dx = x[1:] - x[:-1]
deriv1 = dy / dx

ax1 = subplot(1,1,1)
plot(x, y, label='sin(x)')
plot(x[:-1], deriv1, label='linear approx.')
plot(x, deriv2, label='cos(x)')
# adjust the box to fit 
box1 = ax1.get_position()
ax1.set_position([box1.x0, box1.y0, box1.width * 0.8, box1.height])

title('derivative sin(x)')
legend(loc='center left', bbox_to_anchor=(1, 0.5))

#show()
savefig('derivative.png', bbox_inches='tight')
