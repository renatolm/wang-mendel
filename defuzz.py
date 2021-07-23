from __future__ import division
import numpy as np
import warnings

        
def centroid(x, f_x):
    if len(x) != len(f_x):
        raise ValueError("Argument arrays must have the same size")	
        
    num = 0
    den = 0
    
    for i in range(len(x)):
        num = num + (x[i] * f_x[i])
        den = den + f_x[i]
        
    if den>0:
        return num/den
    else:
        return 0