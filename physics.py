import numpy as np

from utils import SimObject, testbanner
from sim_math import rotmatrix
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
    def __init__(self, dimension: int, mass: float, scale: np.ndarray):
        super().__init__(dimension)

        self.mass = mass
        self.scale = scale

        self.global_location = np.array([128,128])
        self.global_rotation = 0.6

        self.net_force = np.zeros(dimension)
        self.net_torque = np.zeros(dimension)

        self.raw_forces = []
        self.raw_momentums = []

    def __call__(self, delta: np.float32, forces: list):
        self.net_force = np.sum(forces) * delta

    def global_vertices (self, vertices):
        global_vertices = {}
        for key, point in vertices.items():
            global_vertices[key] = np.matmul(rotmatrix(self.global_rotation), point)
            global_vertices[key] *= 128
            global_vertices[key] = global_vertices[key] + self.global_location

        return global_vertices

    def simulate(self, thrusters, forces):
        # todo
        pass


if __name__ == "__main__":
    testbanner()

    #####
    # write tests
