#!/usr/bin/python3

import os
import argparse

from data.Category import Category
from data.Root import Root
from visitor.tester.Tester import Tester
from visitor.FileExplorer import FileExplorer
from visitor.Printer import Printer
from visitor.Executor import Executor
from visitor.Resultor import Resultor

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("--8c", action="store_true", default=False,
        help="Change to 8 color mode")
group.add_argument("--256c", action="store_true", default=False,
        help="Change to 256 color mode")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="count", default=0,
        help="Add informations (descriptions, then additionnal info)")
group.add_argument("-q", "--quiet", action="count", default=0,
        help="Remove informations (passed tests, then additionnal info)")
parser.add_argument("prog")
parser.add_argument("path", default="../test", nargs='?')

args = parser.parse_args()
args.prog = os.path.abspath(args.prog)

cats = Root(args)
cats.accept(FileExplorer)
cats.accept(Executor)
cats.accept(Tester)
cats.accept(Resultor)
cats.accept(Printer)
