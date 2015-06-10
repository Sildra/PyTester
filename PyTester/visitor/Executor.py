from visitor.Visitor import Visitor

import os
import subprocess

from data.Test import Test
from data.Root import Root
from data import Msg


class Executor(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Test):
            Executor.visit_test(obj)

    @staticmethod
    def visit_test(obj: Test):
        cwdpath = os.path.abspath(os.path.join(obj.path, "_test"))
        fout = open(os.path.join(cwdpath, "stdout"), 'w')
        ferr = open(os.path.join(cwdpath, "stderr"), 'w')
        test_file = os.path.join(cwdpath, "test")
        if os.path.isfile(test_file):
            try:
                subprocess.Popen(test_file, stdout=fout, stderr=ferr,
                        cwd=obj.path).wait()
            except(PermissionError):
                Msg.error("Grant exec permission to file " + test_file)
        else:
            try:
                subprocess.Popen(Root.get_root_option("Executable", "None"),
                        stdout=fout, stderr=ferr, cwd=obj.path)
            except(TypeError):
                Msg.error("Type Error on test " + obj.name)
        fout.close()
        ferr.close()

