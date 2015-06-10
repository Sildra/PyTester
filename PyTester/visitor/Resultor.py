from visitor.Visitor import Visitor


class Resultor(Visitor):
    @staticmethod
    def leave(parent, child):
        parent.passed += child.passed
        parent.tested += child.tested
