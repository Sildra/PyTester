from data.Root import Root

import os

import data.Msg as Msg
import data.Color as Color
from data.Test import Test
from data.Category import Category
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
        Msg.cat(obj.name + " " + obj.get_state(), "  " * obj.depth)

    @staticmethod
    def visit_root(obj: Root):
        Msg.blue("[ROOT]", obj.name + " " + obj.get_state(), "  " * obj.depth)

    @staticmethod
    def beautify_diff(string):
        return string.replace("\n", "").replace('-', Color.red('-') + " ") \
            .replace('+', Color.green('+') + " ")

    @staticmethod
    def print_good_diff(obj, string):
        if not (string.startswith("+++") or string.startswith("---") or string.startswith("@@")):
            print("  " * (obj.depth + 2) + Printer.beautify_diff(string))

    @staticmethod
    def visit_test(obj: Test):
        if obj.tested == 0:
            Msg.violet("[UNK]", obj.name, "  " * obj.depth)
        elif obj.passed == 1:
            Msg.green("[OK]", obj.name, "  " * obj.depth)
        else:
            Msg.red("[KO]", obj.name, "  " * obj.depth)
            for name in obj.empty_files:
                Msg.yellow(name, "", "  " * (obj.depth + 1))
                print("  " * (obj.depth + 2) + "Expected result is empty")
            for name, diff in obj.diffs.items():
                Msg.yellow(name, "", "  " * (obj.depth + 1))
                for line in diff:
                    Printer.print_good_diff(obj, line)
