# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Dow Selection
-------------

Topics: Boolean array operators, sum function, where function, plotting.

The array 'dow' is a 2-D array with each row holding the
daily performance of the Dow Jones Industrial Average from the
beginning of 2008 (dates have been removed for exercise simplicity).
The array has the following structure::

       OPEN      HIGH      LOW       CLOSE     VOLUME      ADJ_CLOSE
       13261.82  13338.23  12969.42  13043.96  3452650000  13043.96
       13044.12  13197.43  12968.44  13056.72  3429500000  13056.72
       13046.56  13049.65  12740.51  12800.18  4166000000  12800.18
       12801.15  12984.95  12640.44  12827.49  4221260000  12827.49
       12820.9   12998.11  12511.03  12589.07  4705390000  12589.07
       12590.21  12814.97  12431.53  12735.31  5351030000  12735.31

0. The data has been loaded from a .csv file for you.
1. Create a "mask" array that indicates which rows have a volume
   greater than 5.5 billion.
2. How many are there?  (hint: use sum).
3. Find the index of every row (or day) where the volume is greater
   than 5.5 billion. hint: look at the where() command.

Bonus
~~~~~

1. Plot the adjusted close for *every* day in 2008.
2. Now over-plot this plot with a 'red dot' marker for every
   day where the volume was greater than 5.5 billion.

See :ref:`dow-selection-solution`.
"""

from numpy import loadtxt, sum, where, arange
from matplotlib.pyplot import figure, hold, plot, show, savefig, title, xlabel, ylabel, grid

# Constants that indicate what data is held in each column of
# the 'dow' array.
OPEN = 0
HIGH = 1
LOW = 2
CLOSE = 3
VOLUME = 4
ADJ_CLOSE = 5

# 0. The data has been loaded from a .csv file for you.

# 'dow' is our NumPy array that we will manipulate.
dow = loadtxt('dow.csv', delimiter=',')

# 1. Create a "mask" array that indicates which rows have a volume
#    greater than 5.5 billion.
print 'shape of data array:', dow.shape
print 'type of data array:', dow.dtype
mask = dow[:,4] > (5.5 * (10**9))
#print 'mask for volume > 5.5b:'
#print mask
print

# 2. How many are there?  (hint: use sum).
print 'total rows with volume > 5.5b:', mask.sum()
print

# 3. Find the index of every row (or day) where the volume is greater
#    than 5.5 billion. hint: look at the where() command.
index_mask = where(mask == True)
print 'index of rows with volume > 5.5b:', index_mask
print
#verification if indexes are correct
#print index_mask[0].shape
#mask[index_mask] = False
#print mask

# BONUS:
# a. Plot the adjusted close for EVERY day in 2008.
adj_close = dow[:,5]
r = arange(len(adj_close))
#print r
plot(r, adj_close)

# b. Now over-plot this plot with a 'red dot' marker for every
#    day where the volume was greater than 5.5 billion.
plot(index_mask[0], adj_close[mask], 'ro')
title('Dow Index, volume > 5.5 billion')
xlabel('Day')
ylabel('Adjusted Closing Price')
grid()

savefig('dow_chart.png')
show()