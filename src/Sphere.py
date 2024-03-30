""" Sphere.py: Contains the Sphere class """
from Primitive import Primitive

class Sphere(Primitive):
    """ Represents a sphere in the scene graph """
    def __init__(self):
        super(Sphere, self).__init__()
        # self.call_list = G_OBJ_SPHERE  # Initialize the call list
