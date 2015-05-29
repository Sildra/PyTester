import os
# import data.Options as Options
from overload import overload
from visitor.Visitor import Visitor
from data.Category import Category


class Tester(Visitor):
    @staticmethod
    @overload
    def accept(obj):
        pass

    @staticmethod
    @overload
    def accept(obj: Category):
        if os.path.isfile(os.path.join(obj, "_options")):
            for line in open(os.path.join(obj, "_options"), 'r'):
                args = line.replace(" ", "").split("=")
                if len(args) == 2:
                    obj.options[args[0]] = args[1]
