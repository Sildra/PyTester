class Category(object):
    """description of class"""

    def __init__(self, path, name, depth=0):
        self.name = name
        self.path = path
        self.depth = depth
        self.categories = {}
        self.tests = {}

    def visit(self, visitor):
        """"""
        visitor.accept(self)
        if len(self.categories) > 0:
            for node in self.categories.values():
                node.visit(visitor)
        if len(self.tests) > 0:
            for leaf in self.tests.values():
                leaf.visit(visitor)
        return self

    def add_category(self, category):
        self.categories[category.name] = category

    def add_test(self, test):
        self.tests[test.name] = test
