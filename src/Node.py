""" This module contains the Node class, which is the base class for all the nodes in the scene graph. """
import random
import numpy as np
import OpenGL.GL as gl


class Node():
    """ Represents a node in the scene graph """
    def __init__(self):
        # self.color_index = random.randint(color.MIN_COLOR, color.MAX_COLOR)
        # Initialize the axis aligned bounding box
        # self.aabb = AABB([0.0, 0.0, 0.0], [.5, .5, .5])
        # Initialize the translation matrix
        self.translation_matrix = np.identity(4)
        self.scaling_matrix = np.identity(4)  # Initialize the scaling matrix
        self.selected = False  # Initialize the selected flag

    def render(self):
        """ Renders the node """
        gl.glPushMatrix()
        # Multiply the current matrix by the translation matrix
        gl.glMultMatrixf(np.transpose(self.translation_matrix))
        # Multiply the current matrix by the scaling matrix
        gl.glMultMatrixf(np.transpose(self.scaling_matrix))
        # cur_color = color.COLORS[self.color_index]
        # gl.glColor3f(cur_color[0], cur_color[1], cur_color[2])  # Set the color

        if self.selected:
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_EMISSION, [.3, .3, .3]) # Set the emission color

        self.render_self()  # Render the node

        if self.selected:
            gl.glMaterialfv(gl.GL_FRONT, gl.GL_EMISSION, [0, 0, 0]) # Reset the emission color
        
        gl.glPopMatrix()
    
    def render_self(self):
        """ Renders the node """
        raise NotImplementedError("The render_self method is not implemented")
