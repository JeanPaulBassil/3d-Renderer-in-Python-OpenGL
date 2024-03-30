"""
This module initializes an OpenGL window and displays a blank screen.
"""

import OpenGL.GL as gl
import OpenGL.GLUT as glut
import OpenGL.GLU as glu


def show_screen():
    """Displays the screen."""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT |
               gl.GL_DEPTH_BUFFER_BIT)  # Removes everything from the screen (displays all black)

glut.glutInit()  # Initializes glutInstance which allows us to customize the window
glut.glutInitDisplayMode(glut.GLUT_RGBA)  # Sets the display mode to RGBA
glut.glutInitWindowSize(500, 500)  # Sets the window size to 500x500 pixels
# Sets the window position to the top left corner
glut.glutInitWindowPosition(0, 0)
# Creates the window with the title "OpenGL"
window = glut.glutCreateWindow("OpenGL")
# Calls the show_screen function to display the screen
glut.glutDisplayFunc(show_screen)
# Calls the show_screen function when the screen is idle
glut.glutIdleFunc(show_screen)
glut.glutMainLoop()  # Keeps the window open
