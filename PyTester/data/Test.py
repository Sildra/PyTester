class Test(object):
    """description of class"""

    def __init__(self, path, name, depth=0):
        self.name = name
        self.path = path
        self.depth = depth

    def visit(self, visitor):
        visitor.accept(self)
