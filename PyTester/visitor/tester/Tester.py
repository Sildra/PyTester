from visitor.Visitor import Visitor

from data.Test import Test
from data.Category import Category
from visitor.tester.Diff import Diff
from visitor.tester.Visual import Visual


class Tester(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Test):
            Tester.visit_test(obj)
        elif isinstance(obj, Category):
            Tester.visit_category(obj)

    @staticmethod
    def visit_category(obj: Category):
        obj.passed = 0
        obj.tested = 0

    @staticmethod
    def visit_test(obj: Test):
        getattr(globals().get(obj.get_option("Tester", "Diff")), "start")(obj)

    @staticmethod
    def start(obj):
        pass
