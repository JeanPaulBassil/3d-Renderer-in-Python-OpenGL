""" This module contains the Primitive class, which is a subclass of the Node class. """
import OpenGL.GL as gl
from Node import Node

class Primitive(Node):
    """ Represents a primitive in the scene graph """
    def __init__(self):
        super(Primitive, self).__init__()
        self.call_list = None # Initialize the call list

    def render_self(self):
        gl.glCallList(self.call_list) # Render the primitive
