import numpy as np

from utils import SimObject, testbanner
from physics import PhysicsAttributes

class Body(SimObject):
    def __init__(self,dimension:int, vertices:list,
            edges:list, thrusters:list=[]):
        super().__init__(dimension)

        self.vertices = vertices
        self.edges = edges

        self.center_of_mass = np.zeros(dimension)
        self.phys_attributes = PhysicsAttributes(dimension,
                mass, scale)
        self.thrusters = thrusters
    
    def __call__ (self, delta, pwm_values):
        tnp = zip(self.thrusters, pwm_values)
        forces = [thrust(pwm) for thrust, pwm in tnp]
    
    def __str__ (self):
        # impl
        pass

    def show(self):
        pass
    
    def from_config(cls, fname):
        pass

if __name__ == "__main__":
    testbanner("body.py")

    #####
    # write tests for physics process

    # write tests for show

    # write tests for from_config
