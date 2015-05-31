import os

from visitor.Visitor import Visitor
from data.Category import Category
from data.Test import Test


class FileExplorer(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Category):
            FileExplorer.visit_category(obj)

    @staticmethod
    def visit_category(obj: Category):
        for directory in os.listdir(obj.path):
            path = os.path.join(obj.path, directory)
            if os.path.isdir(os.path.join(path, "_test")):
                obj.add_test(Test(path, directory, obj.depth + 1, obj))
            elif os.path.isdir(path):
                obj.add_category(Category(path, directory, obj.depth + 1, obj))
