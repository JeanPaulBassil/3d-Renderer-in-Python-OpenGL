class Scene():
    """ Represents a scene """
    PLACE_DEPTH = 15.0  # The depth at which the object is placed

    def __init__(self):
        self.node_list = list()  # Initialize the node list
        self.selected_node = None  # Initialize the selected node

    def add_node(self, node):
        """ Adds a node to the scene """
        self.node_list.append(node)  # Add the node to the node list

    def render(self):
        """ Renders the scene """
        for node in self.node_list:
            # node.render()
            pass