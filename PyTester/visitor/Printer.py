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
        print("  " * obj.depth + Msg.cat + obj.name)

    @staticmethod
    def visit_root(obj: Root):
        print("  " * obj.depth + Msg.blue + "[ROOT] " + Msg.reset + obj.name)

    @staticmethod
    def visit_test(obj: Test):
        print("  " * obj.depth + obj.status + " " + obj.name)
