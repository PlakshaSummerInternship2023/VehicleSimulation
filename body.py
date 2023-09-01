import numpy as np
import matplotlib.pyplot as plt

from utils import SimObject, testbanner
from utils import can_eval, input_error_check
from physics import PhysicsAttributes
from render_engine import RenderEngine


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
        self.render_engine = RenderEngine(dimension)

    def __call__(self, delta: np.float32, pwm_values: list, simulate=False):
        tnp = zip(self.thrusters, pwm_values)
        forces = [thrust(pwm) for thrust, pwm in tnp]

        if simulate:
            phys_attributes.simulate(self.thrusters, self.forces)

    def __str__(self):
        # impl
        pass

    def show(self):
        self.render_engine.render(self)

    @staticmethod
    def from_config(file_name: str):
        with open(file_name) as f:
            file = [i.strip() for i in f.readlines() if i != '\n']

        dimension = int(file[0])
        edges = {}
        vertices = {}
        for line in file:
            marker, *other = line.split(" ") # marker is to check whether it is a vertex or edge
            # "other" stores the point_name and coords

            other = [can_eval(i) for i in other] # evaluates any strings into floats 
            if marker == "v":
                point_name, *coord = other[-4:] 
                # -4 is the index where the point name starts, followed by any coordinates 
                input_error_check(coord)
                # checks for any unforseen values amongst the coordinates

                vertices[point_name] = np.array(coord)
            elif marker == "e":
                edges[other[-2]] = other[-1] # point 1 and point 2

        return Body(dimension, vertices, edges)

    def polygon_generator(self): # TAKES FUNCTION AS ARGUEMENT, PUT YOUR DRAWING FUNCTION HERE
        vertices = self.phys_attributes.global_vertices(self.vertices)
        edges = self.edges

        for i in edges:
            base_coords = vertices[i]
            connected_coords = vertices[edges[i]]

            yield (base_coords, connected_coords)

def __2dtests__():
    from thruster import Thruster

    thruster = Thruster(2, np.array([0, -1]), np.array([3, 0]))
    body = Body.from_config("./assets/pentagon.obj")
    print("creating Body object [PASSED]")
    print("testing show for 2d model")

    while 1:
        body.show()


if __name__ == "__main__":
    testbanner()
    print("testing 2 dimensions\n")
    __2dtests__()

    #####
    # write tests for physics process

    # write tests for show

    # write tests for from_config
