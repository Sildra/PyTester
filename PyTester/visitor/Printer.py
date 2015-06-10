from data.Root import Root

from data.Test import Test
from data.Category import Category
import data.Msg as Msg
from visitor.Visitor import Visitor


class Printer(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Root):
            Printer.visit_root(obj)
        elif isinstance(obj, Category):
            Printer.visit_category(obj)
        elif isinstance(obj, Test):
            Printer.visit_test(obj)

    @staticmethod
    def visit_category(obj: Category):
        Msg.cat(obj.name, "  " * obj.depth)

    @staticmethod
    def visit_root(obj: Root):
        Msg.blue("[ROOT]", obj.name, "  " * obj.depth)

    @staticmethod
    def visit_test(obj: Test):
        if obj.tested == 0:
            Msg.violet("[UNK]", obj.name, "  " * obj.depth)
        elif obj.passed == 0:
            Msg.red("[KO]", obj.name, "  " * obj.depth)
        else:
            Msg.green("[KO]", obj.name, "  " * obj.depth)
        for item in obj.diffs:
            print(item) """ TODO """
