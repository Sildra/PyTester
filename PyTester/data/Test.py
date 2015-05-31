from data.Element import Element


class Test(Element):
    """description of class"""

    def __init__(self, path, name, depth=0, parent=''):
        super().__init__(path, name, depth, parent)

    def accept(self, visitor):
        visitor.visit(self)
