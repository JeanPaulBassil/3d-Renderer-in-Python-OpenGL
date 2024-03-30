""" This file contains the Viewer class which is responsible for rendering the scene and handling user interaction. """

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu
import numpy as np


class Viewer():
    """ Viewer class which is responsible for rendering the scene and handling user interaction. """

    def __init__(self):
        self.init_interface()  # Initializes the interface
        self.init_opengl()  # Initializes OpenGL
        self.init_scene()  # Initializes the scene
        self.init_interaction()  # Initializes the interaction
        # init_primitives() # Initializes the primitives from 
        # the Primitives.py file (to be implemented)

    def init_interface(self):
        """ Initializes the interface """
        glut.glutInit()  # Initializes glutInstance which allows us to customize the window
        # Sets the window size to 640x480 pixels
        glut.glutInitWindowSize(640, 480)
        # Creates the window with the title "3D Modeller"
        glut.glutCreateWindow("3D Modeller")
        # Sets the display mode to single and RGB
        glut.glutInitDisplayMode(glut.GLUT_SINGLE | glut.GLUT_RGB)
        # Calls the render function to display the screen
        # glut.glutDisplayFunc(self.render)

    def init_opengl(self):
        """ Initializes OpenGL """
        # Initialize the inverse model view matrix
        self.inverse_model_view = np.identity(4)
        self.model_view = np.identity(4)  # Initialize the model view matrix

        # Enable back face culling which is the removal of back facing polygons
        # i.e polygons facing away from the camera
        gl.glEnable(gl.GL_CULL_FACE)
        gl.glCullFace(gl.GL_BACK)  # Remove back facing polygons
        # Enable depth testing for the removal of hidden surfaces
        gl.glEnable(gl.GL_DEPTH_TEST)
        gl.glDepthFunc(gl.GL_LESS)  # Specify the depth comparison function

        gl.glEnable(gl.GL_LIGHT0)  # Enable light 0
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_POSITION, gl.GLfloat_4(
            0, 0, 1, 0))  # Set the position of light 0
        gl.glLightfv(gl.GL_LIGHT0, gl.GL_SPOT_DIRECTION, gl.GLfloat_3(
            0, 0, -1))  # Set the direction of light 0

        # Set the material color to ambient and diffuse
        gl.glColorMaterial(gl.GL_FRONT_AND_BACK, gl.GL_AMBIENT_AND_DIFFUSE)
        gl.glEnable(gl.GL_COLOR_MATERIAL)  # Enable color material
        gl.glClearColor(0.4, 0.4, 0.4, 0.0)  # Set the clear color to grey

    def init_scene(self):
        """ Initializes the scene """
        # self.scene = Scene()  # Create a scene object (to be implemented)
        # self.create_sample_scene()  # Create a sample scene

    def create_sample_scene(self):
        """ Creates a sample scene """
        # cube_node = Cube()  # Create a cube node (to be implemented)
        # cube_node.translate(2, 0, 2) # Translate the cube node
        # cube_node.color_index = 2 # Set the color index of the cube node
        # self.scene.add_node(cube_node) # Add the cube node to the scene

        # sphere_node = Sphere()  # Create a sphere node (to be implemented)
        # sphere_node.translate(-2, 0, 2) # Translate the sphere node
        # sphere_node.color_index = 3 # Set the color index of the sphere node
        # self.scene.add_node(sphere_node) # Add the sphere node to the scene

        # hierarchical_node = SnowFigure()  # Create a snow figure node (to be implemented)
        # hierarchical_node.translate(-2, 0, -2) # Translate the snow figure node
        # self.scene.add_node(hierarchical_node)

    def init_interaction(self):
        """ Initializes the interaction """
        # self.interaction = Interaction() # Create an interaction object (to be implemented)
        # self.interaction.register_callback("pick", self.pick) # Register the pick callback
        # self.interaction.register_callback("move", self.move) # Register the move callback
        # self.interaction.register_callback("place", self.place) # Register the place callback
        # Register the rotate color callback
        # self.interaction.register_callback("rotate_color", self.rotate_color)
        # self.interaction.register_callback("scale", self.scale) # Register the scale callback

    def main_loop(self):
        """ Main loop of the viewer """
        glut.glutMainLoop()

    def render(self):
        self.init_view()

        gl.glEnable(gl.GL_LIGHTING)  # Enable lighting
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)  # Clear the color and depth buffer

        gl.glMatrixMode(gl.GL_MODELVIEW)  # Set the model view matrix
        gl.glPushMatrix()  # Push the current matrix onto the stack
        gl.glLoadIdentity()  # Load the identity matrix
        # loc = self.interaction.translation  # Get the translation
        # gl.glTranslated(lo[0], loc[1], loc[2])  # Translate the scene based on the translation
        # gl.glMultMatrixf(self.interaction.trackball.matrix) # Multiply the current matrix by the trackball matrix

        current_model_view = np.array(gl.glGetFloatv(gl.GL_MODELVIEW_MATRIX)) # Get the current model view matrix
        # self.model_view = np.transpose(current_model_view) # Transpose the current model view matrix
        # self.inverse_model_view = inv(np.transpose(current_model_view)) # Calculate the inverse model view matrix

        # self.scene.render()  # Render the scene

        gl.glDisable(gl.GL_LIGHTING)  # Disable lighting
        gl.glCallList(gl.GL_OBJECT_PLANE) # Call the object plane
        gl.glPopMatrix()  # Pop the current matrix from the stack

        gl.glFlush()  # Flush the OpenGL pipeline to the viewport


    def init_view(self):
        """ Initializes the view """
        xSize, ySize = glut.glutGet(glut.GLUT_WINDOW_WIDTH), glut.glutGet(
            glut.GLUT_WINDOW_HEIGHT) # Get the window size
        aspect_ratio = float(xSize) / float(ySize) # Calculate the aspect ratio

        gl.glMatrixMode(gl.GL_PROJECTION) # Set the projection matrix
        gl.glLoadIdentity() # Load the identity matrix

        gl.glViewport(0, 0, xSize, ySize) # Set the viewport size to the window size
        glu.gluPerspective(70, aspect_ratio, 0.1, 1000.0) # Set the perspective projection matrix
        gl.glTranslated(0, 0, -15) # Translate the scene along the z-axis

    

if __name__ == "__main__":
    viewer = Viewer()
    viewer.main_loop()
