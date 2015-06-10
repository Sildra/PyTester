from data.Element import Element

from data import Msg


class Test(Element):
    """description of class"""

    def __init__(self, path, name, depth=0, parent=''):
        super().__init__(path, name, depth, parent)
        self.diffs = {}
        self.empty_files = []

    def accept(self, visitor):
        visitor.visit(self)

    def add_diff(self, name, diff):
        self.diffs[name] = diff

    def add_empty(self, name):
        self.empty_files.append(name)
