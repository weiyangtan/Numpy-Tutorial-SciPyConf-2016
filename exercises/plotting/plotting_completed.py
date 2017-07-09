# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Plotting
--------

In PyLab, create a plot display that looks like the following:

.. image:: plotting/sample_plots.png

`Photo credit: David Fettig
<http://www.publicdomainpictures.net/view-image.php?image=507>`_


This is a 2x2 layout, with 3 slots occupied.

1. Sine function, with blue solid line; cosine with red '+' markers; the
   extents fit the plot exactly. Hint: see the axis() function for setting the
   extents.
2. Sine function, with gridlines, axis labels, and title; the extents fit the
   plot exactly.
3. Image with color map; the extents run from -10 to 10, rather than the
   default.

Save the resulting plot image to a file. (Use a different file name, so you
don't overwrite the sample.)

The color map in the example is 'winter'; use 'cm.<tab>' to list the available
ones, and experiment to find one you like.

Start with the following statements::

    from matplotlib.pyplot import imread

    x = linspace(0, 2*pi, 101)
    s = sin(x)
    c = cos(x)

    img = imread('dc_metro.jpg')

Tip: If you find that the label of one plot overlaps another plot, try adding
a call to `tight_layout()` to your script.

Bonus
~~~~~

4. The `subplot()` function returns an axes object, which can be assigned to
   the `sharex` and `sharey` keyword arguments of another subplot() function
   call.  E.g.::

       ax1 = subplot(2,2,1)
       ...
       subplot(2,2,2, sharex=ax1, sharey=ax1)

   Make this modification to your script, and explore the consequences.
   Hint: try panning and zooming in the subplots.

See :ref:`plotting-solution`.
"""


# The following imports are *not* needed in PyLab, but are needed in this file.
from numpy import linspace, pi, sin, cos
from matplotlib.pyplot import (plot, subplot, cm, imread, imshow, xlabel,
                               ylabel, title, grid, axis, show, savefig, gcf,
                               figure, close, tight_layout, colorbar, setp)

x = linspace(0, 2 * pi, 101)
s = sin(x)
c = cos(x)

img = imread('dc_metro.JPG')

close('all') # good practice to clear all plots

# plot 1: sine and cosine curve
ax1 = subplot(2,2,1)
plot(x, s, 'b', x, c, 'rx')
axis('tight')
setp(ax1.get_xticklabels(), visible=False)

# plot 2: sine curve with grids
ax2 = subplot(2,2,3, sharex=ax1)
plot(x, s)
title('Sine Curve of X')
xlabel('radians')
ylabel('amplitude')
grid()
axis('tight')

# plot 3: image
subplot(2,2,2)
imshow(img, extent=[-10,10,-1,10], cmap=cm.winter)
colorbar()

tight_layout()
#show()
savefig('my_plots.png', bbox_inches='tight')

