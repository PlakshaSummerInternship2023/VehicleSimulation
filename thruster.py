import numpy as np

from utils import SimObject, testbanner
from regressor import pwm_regressor

class Thruster(SimObject):
    def __init__(self, dimension:int,direction:np.ndarray,
            location:np.ndarray):
        super().__init__(dimension)

        self.direction = direction
        self.location = location

    def __call__ (self, pwm):
        return self.location * pwm_regressor(pwm)

if __name__ == "__main__":
    testbanner("thruster.py")

    #####
    # write tests for __call__
    
