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
parser.add_argument("--8c", action="store_true", default=False, help="Change to 8 color mode")
parser.add_argument("--256c", action="store_true", default=False, help="Change to 256 color mode")
parser.print_help()
exit()

cats = Root(os.path.join("..", "test"), "PyTester", -1)
cats.accept(FileExplorer)
cats.accept(Executor)
cats.accept(Tester)
cats.accept(Resultor)
cats.accept(Printer)
