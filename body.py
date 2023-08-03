import numpy as np
import matplotlib.pyplot as plt

from utils import SimObject, testbanner
from physics import PhysicsAttributes


class Body(SimObject):
    def __init__(
        self,
        dimension: int,
        vertices: list,
        edges: list,
        thrusters: list = [],
        mass: float = -1.0,
        scale: float = 1.0,
        line_width: float = 3.0,
    ):
        super().__init__(dimension)

        self.vertices = vertices
        self.edges = edges

        self.center_of_mass = np.zeros(dimension)
        self.phys_attributes = PhysicsAttributes(dimension, mass, scale)
        self.thrusters = thrusters

        self.line_width = line_width

    def __call__(self, delta: np.float32, pwm_values: list, simulate=False):
        tnp = zip(self.thrusters, pwm_values)
        forces = [thrust(pwm) for thrust, pwm in tnp]

        if simulate:
            phys_attributes.simulate(self.thrusters, self.forces)

    def __str__(self):
        # impl
        pass

    def show(self):
        for i, j in self.edges:
            (x1, y1), (x2, y2) = tuple(self.vertices[i]), tuple(self.vertices[j])

            line = plt.Line2D((x1, x2), (y1, y2), lw=self.line_width)
            plt.gca().add_line(line)
        for thruster in self.thrusters:
            (x, y), (dx, dy) = tuple(thruster.location), tuple(thruster.direction)
            plt.arrow(x, y, dx, dy, width=self.line_width / 25, color="red")
        plt.axis("scaled")
        plt.show()

    @staticmethod
    def from_config(cls, fname):
        pass


def __2dtests__():
    from thruster import Thruster

    thruster = Thruster(2, np.array([0, -1]), np.array([3, 0]))
    body = Body(
        2,
        vertices=[np.array([0, 0]), np.array([3, 3]), np.array([6, 0])],
        edges=[(0, 1), (1, 2), (2, 0)],
        thrusters=[thruster],
    )
    print("creating Body object [PASSED]")
    print("testing show for 2d model")

    body.show()


if __name__ == "__main__":
    testbanner()
    print("testing 2 dimensions\n")
    __2dtests__()

    #####
    # write tests for physics process

    # write tests for show

    # write tests for from_config
