

import matplotlib.pyplot as plt
import numpy as np

class SpaceTime:
    def __init__(self, xdim, ydim):
        self.xdim = xdim
        self.ydim = ydim
        self.space = np.zeros((xdim,ydim))
