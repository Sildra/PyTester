from data.Category import Category


class Root(Category):
    """description of class"""

    def __init__(self, path, name, depth=0):
        super().__init__(path, name, depth)

    def accept(self, visitor):
        visitor.visit(self)
        if len(self.categories) > 0:
            for node in self.categories.values():
                node.accept(visitor)
