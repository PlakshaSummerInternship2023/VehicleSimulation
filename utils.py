import numpy as np

"""A super class for all the classes in this project, it has
    inherent dimension checks and can house other comfort
    features

    Attributes:
        - dimension : int
"""
class SimObject(object):
    def __init__ (self, dimension:int):
        self.dimension = dimension

    # this checks if the assignment of any vectors has incorrect dim
    def __setattr__ (self,item,value):
        if type(value) == np.ndarray:
            if value.shape != (self.dimension,):
                raise DimError(value.shape, value)
        return super().__setattr__(item, value)



class DimError (Exception):
    """Exception to be raised in case of a dimension
    mismatch

    Attributes:
        - shape : tuple
        - expected_shape : tuple
    """
    def __init__ (self,shape,expected_shape):
        self.shape = shape
        self.expected_shape = expected_shape
        self.message=f"""\
        expected shape to be {expected_shape}, got shape {shape}"""

        super().__init__(self.message)

def testbanner(fname):
    print("\n"*7)
    print("#"*80)
    print(f"running tests for {fname}")

if __name__ == "__main__":
    testbanner("utils.py")

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

