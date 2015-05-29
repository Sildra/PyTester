class Root(object):
    """description of class"""

    def __init__(self, path, name, depth=0):
        self.name = name
        self.path = path
        self.depth = depth
        self.categories = {}

    def visit(self, visitor):
        visitor.node(self)
        if len(self.categories) > 0:
            for node in self.categories.values():
                node.visit(visitor)
