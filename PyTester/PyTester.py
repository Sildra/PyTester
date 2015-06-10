#!/usr/bin/python3

import os

from data.Category import Category
from data.Root import Root
from visitor.tester.Tester import Tester
from visitor.FileExplorer import FileExplorer
from visitor.Printer import Printer
from visitor.Executor import Executor

cats = Root(os.path.join("..", "test"), "PyTester", -1)
cats.accept(FileExplorer)
cats.accept(Tester)
cats.accept(Printer)
