from __future__ import division
import numpy as np

class Triangular:
    def __init__(self, ini, top, end):
        self.ini = ini
        self.top = top
        self.end = end
        
    def __repr__(self):
        return "triang(x, {}, {}, {})".format(self.ini, self.top, self.end)
    
    def __str__(self):
        return "triang(x, {}, {}, {})".format(self.ini, self.top, self.end)
        
    def pertinence(self, x):
        if (x > self.ini) and (x < self.top):
            return (x / (self.top - self.ini)) - (self.ini / (self.top - self.ini))
        elif (x > self.top) and (x < self.end):
            return (-x / (self.end - self.top)) + (self.end / (self.end - self.top))
        elif x == self.top:
            return 1
        else:
            return 0

class Trapezoidal:
    def __init__(self, ini, top1, top2, end):
        self.ini = ini
        self.top1 = top1
        self.top2 = top2
        self.end = end
        
    def __repr__(self):
        return "trap(x, {}, {}, {}, {})".format(self.ini, self.top1, self.top2, self.end)
    
    def __str__(self):
        return "trap(x, {}, {}, {}, {})".format(self.ini, self.top1, self.top2, self.end)
        
    def pertinence(self, x):
        if (x > self.ini) and (x < self.top1):
            return (x / (self.top1 - self.ini)) - (self.ini / (self.top1 - self.ini))
        elif (x > self.top2) and (x < self.end):
            return (-x / (self.end - self.top2)) + (self.end / (self.end - self.top2))
        elif (x >= self.top1) and (x <= self.top2):
            return 1
        else:
            return 0

class InferiorBorder:
    def __init__(self, top, end):
        self.top = top
        self.end = end
        
    def __repr__(self):
        return "inf_border(x, {}, {})".format(self.top, self.end)
    
    def __str__(self):
        return "inf_border(x, {}, {})".format(self.top, self.end)
        
    def pertinence(self, x):
        if x <= self.top:
            return 1
        elif (x > self.top) and (x < self.end):
            return (-x / (self.end - self.top)) + (self.end / (self.end - self.top))
        else:
            return 0

class SuperiorBorder:
    def __init__(self, ini, top):
        self.ini = ini
        self.top = top
        
    def __repr__(self):
        return "sup_border(x, {}, {})".format(self.ini, self.top)
    
    def __str__(self):
        return "sup_border(x, {}, {})".format(self.ini, self.top)
    
    def pertinence(self, x):
        if x <= self.ini:
            return 0
        elif (x > self.ini) and (x < self.top):
            return (x / (self.top - self.ini)) - (self.ini / (self.top - self.ini))
        else:
            return 1

# def gaussian(entrada, mu, sig):
# 	return np.exp(-np.power(entrada - mu, 2.) / (2 * np.power(sig, 2.)))

# def alpha_cut_triang(alpha, ini, topo, fim):
# 	corte = []
# 	for i in np.arange(ini, fim, 0.1):
# 		if triang(i, ini, topo, fim) >= alpha:
# 			corte.append(i)

# 	return corte

# def alpha_cut_trap(alpha, ini, topo1, topo2, fim):
# 	corte = []
# 	for i in np.arange(ini, fim, 0.1):
# 		if trap(i, ini, topo1, topo2, fim) >= alpha:
# 			corte.append(i)

# 	return corte

# def crisp(entrada, topo):
# 	if entrada == topo:
# 		return 1
# 	else:
# 		return 0