class HierarchicalNode(Node):
    """ A node comprised of children nodes. """
    def __init__(self):
        super(HierarchicalNode, self).__init__()
        self.children = []

    def render_self(self):
        """ Render the node itself. """
        for child in self.children:
            child.render()

            