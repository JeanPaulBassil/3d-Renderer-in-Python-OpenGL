from HierarchicalNode import HierarchicalNode
from Sphere import Sphere
import numpy as np

class SnowFigure(HierarchicalNode):
    """ A snow figure comprised of snowballs. """
    def __init__(self):
        super(SnowFigure, self).__init()
        self.child_nodes = [Sphere(), Sphere(), Sphere()]
        self.child_nodes[0].translate(0, -.6, 0)
        self.child_nodes[1].translate(0, 0.1, 0)
        # self.child_nodes[1].scaling_matrix = np.dot(
        #     self.scaling_matrix, scaling([0.8, 0.8, 0.8]))
        self.child_nodes[2].translate(0, 0.75, 0)
        self.child_nodes[2].scaling_matrix = np.dot(
            # self.scaling_matrix, scaling([0.7, 0.7, 0.7]))
        for child_node in self.child_nodes:
            pass
            # child_node.color_index = color.MIN_COLOR
        self.aabb = AABB([0.0, 0.0, 0.0], [0.5, 1.1, 0.5])
    