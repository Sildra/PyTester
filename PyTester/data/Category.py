import os
from data.Element import Element


class Category(Element):
    """description of class"""

    def __init__(self, path, name, depth=0, parent=''):
        super().__init__(path, name, depth, parent)
        self.categories = {}
        self.tests = {}

    def accept(self, visitor):
        """"""
        visitor.visit(self)
        self.passed = 0
        self.passed = 0
        if len(self.categories) > 0:
            for node in self.categories.values():
                node.accept(visitor)
                self.passed += node.passed
                self.tested += node.tested
        if len(self.tests) > 0:
            for leaf in self.tests.values():
                leaf.accept(visitor)
                self.passed += leaf.passed
                self.tested += leaf.tested
        return self

    def add_category(self, category):
        self.categories[category.name] = category

    def add_test(self, test):
        self.tests[test.name] = test
