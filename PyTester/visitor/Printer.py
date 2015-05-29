from overload import overload

from data.Test import Test
from data.Category import Category
import data.Msg as Msg
from visitor.Visitor import Visitor


class Printer(Visitor):
    @staticmethod
    @overload
    def accept(obj):
        pass

    @staticmethod
    @overload
    def accept(obj: Category):
        print("  " * obj.depth + Msg.cat + obj.name)

    @staticmethod
    @overload
    def accept(obj: Test):
        print("  " * obj.depth + Msg.status_ko + obj.name)
