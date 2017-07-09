# Copyright 2016 Enthought, Inc. All Rights Reserved
"""
Structured Array
----------------

In this exercise you will read columns of data into a structured array using
loadtxt and combine that array to a regular array to analyze the data and learn
how the pressure velocity evolves as a function of the shear velocity in sound
waves in the Earth.

1. The data in 'short_logs.crv' has the following format::

       DEPTH          CALI       S-SONIC   ...
       8744.5000   -999.2500   -999.2500   ...
       8745.0000   -999.2500   -999.2500   ...
       8745.5000   -999.2500   -999.2500   ...

   Here the first row defines a set of names for the columns
   of data in the file.  Use these column names to define a
   dtype for a structured array that will have fields 'DEPTH',
   'CALI', etc.  Assume all the data is of the float64 data
   format.

2. Use the 'loadtxt' method from numpy to read the data from
   the file into a structured array with the dtype created
   in (1).  Name this array 'logs'

3. The 'logs' array is nice for retrieving columns from the data.
   For example, logs['DEPTH'] returns the values from the DEPTH
   column of the data.  For row-based or array-wide operations,
   it is more convenient to have a 2D view into the data, as if it
   is a simple 2D array of float64 values.

   Create a 2D array called 'logs_2d' using the view operation.
   Be sure the 2D array has the same number of columns as in the
   data file.

4. -999.25 is a "special" value in this data set.  It is
   intended to represent missing data.  Replace all of these
   values with NaNs.  Is this easier with the 'logs' array
   or the 'logs_2d' array?

5. Create a mask for all the "complete" rows in the array.
   A complete row is one that doesn't have any NaN values measured
   in that row.

   HINT: The ``all`` function is also useful here.

6. Plot the VP vs VS logs for the "complete" rows.

See :ref:`structured-array-solution`.
"""
from numpy import dtype, loadtxt, float64, NaN, isfinite, all, logical_not
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, savefig

# Open the file.
log_file = open('short_logs.crv')

# The first line is a header that has all the log names.
header = log_file.readline()
log_names = header.split()
#print log_names

# 1. Preparing the data structure
pairing = []
for i in log_names:
    pairing.append((i, float64))
#print pairing
fmt = dtype(pairing)

# 2. reading the data
logs = loadtxt('short_logs.crv', dtype=fmt, skiprows=1)
#print logs

# 3. 2D view
logs_2d = logs.view(float64)
#print logs_2d
logs_2d = logs_2d.reshape(-1, len(log_names)) # -1 means "as many rows as necessary"
#print logs_2d

# 4. replace -999.25 with NaN
mask = logs_2d == -999.25
logs_2d[mask] = NaN
#print logs

# 5. mask of all rows without NaN
inv_mask = logical_not(mask)
mask_all = inv_mask.all(axis=1)
#print mask_all

# 6. plot VP vs VS for complete rows
complete_vp = logs['VP'][mask_all]
complete_vs = logs['VS'][mask_all]
plot(complete_vp, complete_vs, 'o', markersize=1)
title('VP against VS plot')
xlabel('VP values')
ylabel('VS values')
savefig('vp_vs.png')
show()