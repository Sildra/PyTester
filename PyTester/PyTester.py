#!/usr/bin/python3

import os
import argparse

from data import Msg
from data.Root import Root
from visitor.tester.Tester import Tester
from visitor.FileExplorer import FileExplorer
from visitor.Printer import Printer
from visitor.Executor import Executor
from visitor.Resultor import Resultor


def parse_cmd():
    parser = argparse.ArgumentParser()
    # Project options
    parser.add_argument("prog")
    parser.add_argument("path", default="../test", nargs='?')

    # Test options
    parser.add_argument("--ref", action="store_true", default=False,
                        help="Uses current run as reference")
    # Color options
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--8c", action="store_true", default=False,
                       help="Change to 8 color mode")
    group.add_argument("--256c", action="store_true", default=False,
                       help="Change to 256 color mode")
    # Verbose options
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="count", default=0,
                       help="Add information (descriptions, then additional info)")
    group.add_argument("-q", "--quiet", action="count", default=0,
                       help="Remove information (passed tests, then additional info)")

    # Output options

    args = parser.parse_args()
    if not os.path.exists(args.prog):
        Msg.error("Executable " + args.prog + " not found")
        exit(1)
    args.prog = os.path.abspath(args.prog)
    os.environ["EXECUTABLE"] = args.prog
    os.environ["RESULT"] = "_test" if args.ref else "_result"
    return args


def execute(args):
    cats = Root(args)
    cats.accept(FileExplorer)
    cats.accept(Executor)
    cats.accept(Tester)
    cats.accept(Resultor)
    cats.accept(Printer)


execute(parse_cmd())
