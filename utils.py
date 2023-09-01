import numpy as np
import sys

"""A super class for all the classes in this project, it has
    inherent dimension checks and can house other comfort
    features

    Attributes:
        - dimension : int
"""


class SimObject(object):
    def __init__(self, dimension: int):
        self.dimension = dimension

    # this checks if the assignment of any vectors has incorrect dim
    def __setattr__(self, item, value):
        if type(value) == np.ndarray:
            if value.shape != (self.dimension,):
                raise DimError(value.shape, value)
        return super().__setattr__(item, value)


class DimError(Exception):
    """Exception to be raised in case of a dimension
    mismatch

    Attributes:
        - shape : tuple
        - expected_shape : tuple
    """

    def __init__(self, shape, expected_shape):
        self.shape = shape
        self.expected_shape = expected_shape
        self.message = f"""\
        expected shape to be {expected_shape}, got shape {shape}"""

        super().__init__(self.message)


def testbanner():
    print("\n")
    print("#" * 80)
    print(f"running tests for {sys.argv[0]}")



def can_eval(expr): # DOES NOT THROW EXCEPTION FOR ERRORS
    try:
        return eval(expr)
    except NameError:
        return expr

def input_error_check(coords):
    error_val = ""
    try:
        for error_val in coords:
            float(error_val)
        return
    except ValueError:
        raise ValueError("There is a mistake in the file input, search term: ", error_val)


if __name__ == "__main__":
    testbanner()

    # testing if incorrect dimensions throw DimError
    so = SimObject(3)
    try:
        so.attr = np.zeros(5)
        print("SimObject incorrect DimError [failed]")
    except DimError as de:
        print("SimObject incorrect DimError [passed]")

    # testing if correction dimensions throw DimError
    try:
        so.attr = np.zeros(3)
        print("SimObject incorrect DimError [passed]")
    except DimError as de:
        print("SimObject incorrect DimError [failed]")
