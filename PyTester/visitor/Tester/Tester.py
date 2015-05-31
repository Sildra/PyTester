from data.Test import Test
from visitor.Visitor import Visitor
from visitor.tester.Diff import Diff
from visitor.tester.Visual import Visual


class Tester(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Test):
            Tester.visit_test(obj)

    @staticmethod
    def visit_test(obj: Test):
        getattr(globals().get(obj.get_option("Tester", "Diff")), "start")(obj)

    @staticmethod
    def start(obj):
        pass
