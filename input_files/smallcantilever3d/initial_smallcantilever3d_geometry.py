# def initial_cantilever2d_geometry():
## Initial design input file 
#
# *** THIS SCRIPT HAS TO BE CUSTOMIZED BY THE USER ***
#
# In this file, you must create two matrices that describe the initial
# design of bars.
#
# The first matrix contains the IDs (integer) and coordinates of the
# endpoints of the bars (point_matrix).
#
# The second matrix defines the IDs of the points that make up each bar.
# This matrix also sets the initial value of each bar's size variable, and
# the initial bar radius (half-width of the bar in 2-d).
#
# Note that this way of defining the bars allows for bars to be 'floating'
# (if the endpoints of a bar are not shared by any other bar) or
# 'connected' (if two or more bars share the same endpoint).
#

# *** Do not modify the line below ***
import numpy as np
# global FE, GEOM 

# Format of point_matrix is [ point_id, x, y] for 2-d problems, and 
# [ point_id, x, y, z] for 3-d problems)

point_matrix = np.array( (
    ( 0 , 2.4 , 2.5 , 1.0 ) ,
    ( 1 , 2.6 , 2.5 , 1.0 ) ,
    ( 2 , 2.4 , 2.5 , 4.0 ) ,
    ( 3 , 2.6 , 2.5 , 4.0 ) ) )

# Format of bar_matrix is [ bar_id, pt1, pt2, alpha, w/2 ], where alpha is
# the initial value of the bar's size variable, and w/2 the initial radius
# of the bar.

bar_matrix = np.array( (
    ( 0 , 0 , 1 , 0.5, 0.75 ) ,
    ( 1 , 2 , 3 , 0.5, 0.75 ) ) )

# *** Do not modify the code below ***
GEOM['initial_design']['point_matrix'] = point_matrix
GEOM['initial_design']['bar_matrix'] = bar_matrix

print('initialized ' + str(FE['dim']) + 'd initial design with ' + 
    str( GEOM['initial_design']['point_matrix'].shape[0] ) + ' points and ' +
    str( GEOM['initial_design']['bar_matrix'].shape[0] ) + ' bars\n' )