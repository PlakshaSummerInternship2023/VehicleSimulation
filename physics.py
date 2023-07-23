import numpy as np

from utils import SimObject, testbanner

"""
Physics attributes is the heart of the physics engine
in this project, it contains all kinds of physical orientation
of the body, and calculates the next orientations based
on the deltas

dimension : int
mass      : float
scale     : np.ndarray
    this attribute shows the scale of the object in
    each direction

location  : np.ndarray
    this attribute shows the location of the object
rotation  : np.ndarray
    this attribute shows the rotation of the object

net_force : np.ndarray
    this attribute represents the net force on the object
net_torque : np.ndarray
    this attribute represents the net torque on the object

raw_forces : list[tuple(np.ndarray)]
    this attribute represents each force on the object
    [ (location, force) ... ], where location and force
    are np.ndarray
raw_momentums : list[np.ndarray]
    this attribute represents each momentum on the obejct
    [ (location, momentum) ... ], where location and momentum
    are np.ndarray

"""
class PhysicsAttributes(SimObject):
    def __init__(self, dimension:int, mass:float, 
            scale:np.ndarray):
        super().__init__(dimension)

        self.mass = mass
        self.scale = scale

        self.location = np.zeros(dimension)
        self.rotation = np.zeros(dimension)

        self.net_force = np.zeros(dimension)
        self.net_torque = np.zeros(dimension)

        self.raw_forces = []
        self.raw_momentums = []

    def __call__ (self, delta:np.float32, forces:list):
        self.net_force = np.sum(forces)*delta


if __name__ == "__main__":
    testbanner("physics.py")

    #####
    # write tests
