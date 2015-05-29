from data.Category import Category
from visitor.FileExplorer import FileExplorer
from visitor.Printer import Printer

cats = Category("..\\test", "PyTester", -1)
cats.visit(FileExplorer)
cats.visit(Printer)
