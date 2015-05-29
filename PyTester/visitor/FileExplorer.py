import os

from overload import overload

from visitor.Visitor import Visitor
from data.Category import Category
from data.Test import Test


class FileExplorer(Visitor):
    @staticmethod
    @overload
    def accept(obj):
        pass

    @staticmethod
    @overload
    def accept(obj: Category):
        for directory in os.listdir(obj.path):
            path = os.path.join(obj.path, directory)
            if os.path.isdir(os.path.join(path, "_test")):
                obj.add_test(Test(path, directory, obj.depth + 1))
            elif os.path.isdir(path):
                obj.add_category(Category(path, directory, obj.depth + 1))
