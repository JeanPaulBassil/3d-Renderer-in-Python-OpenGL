"""
This module initializes an OpenGL window and displays a blank screen.
"""

import OpenGL.GL as gl
import OpenGL.GLUT as glut

w, h = 500, 500  # Width and height of the window

def square():
    """Draw a square"""
    gl.glBegin(gl.GL_QUADS)  # Start drawing a square
    gl.glVertex2f(100, 100)  # Bottom left corner of the square
    gl.glVertex2f(200, 100)  # Bottom right corner of the square
    gl.glVertex2f(200, 200)  # Top right corner of the square
    gl.glVertex2f(100, 200)  # Top left corner of the square
    gl.glEnd()  # Finish drawing the square

def iterate():
    """Iterate through the window."""
    gl.glViewport(0, 0, w, h)  # Set the viewport to the current window specifications
    gl.glMatrixMode(gl.GL_PROJECTION)  # Set the matrix mode to projection
    gl.glLoadIdentity()  # Reset the matrix to identity
    gl.glOrtho(0.0, w, 0.0, h, 0.0, 1.0)  # Multiply the current matrix with an orthographic matrix
    gl.glMatrixMode(gl.GL_MODELVIEW)  # Set the matrix mode to modelview
    gl.glLoadIdentity()  # Reset the matrix to identity

def show_screen():
    """Displays the screen."""
    gl.glClear(gl.GL_COLOR_BUFFER_BIT |
               gl.GL_DEPTH_BUFFER_BIT)  # Removes everything from the screen (displays all black)
    gl.glLoadIdentity()  # Resets the view back to the origin
    iterate()  # Calls the iterate function to set the window specifications
    gl.glColor3f(1.0, 0.0, 3.0)  # Sets the color to pink
    square() # Calls the square function to draw the square
    glut.glutSwapBuffers()  # Swaps the buffers of the current window

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
