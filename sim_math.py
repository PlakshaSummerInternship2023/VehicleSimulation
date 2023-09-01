import numpy as np

def rotmatrix (theta):
    r = np.array([[np.cos(theta), np.sin(theta)],[-np.sin(theta), np.cos(theta)]])
    return r
