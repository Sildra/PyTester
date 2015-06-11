from visitor.Visitor import Visitor

import os
import subprocess

from data.Test import Test
from data.Root import Root
from data import Msg

join = os.path.join
popen = subprocess.Popen


class Executor(Visitor):
    @staticmethod
    def visit(obj):
        if isinstance(obj, Test):
            Executor.visit_test(obj)

    @staticmethod
    def visit_test(obj: Test):
        cwdpath = os.path.abspath(join(obj.path))
        outpath = join(cwdpath, "_cache")
        if not os.path.exists(outpath):
            os.mkdir(outpath)
        fout = open(join(outpath, "stdout"), 'w')
        ferr = open(join(outpath, "stderr"), 'w')
        fcode = open(join(outpath, "exit_code"), 'w')
        code = 0
        test_file = os.path.join(obj.path, "_test", "test")
        if os.path.isfile(test_file):
            try:
                code = popen(test_file, stdout=fout, stderr=ferr,
                             cwd=obj.path).wait()
            except PermissionError:
                Msg.error("Permission error on test " + cwdpath)
            except OSError:
                Msg.error("OS Error on test " + cwdpath)
        else:
            try:
                code = popen(Root.args().prog,
                             stdout=fout, stderr=ferr, cwd=obj.path).wait()
            except TypeError:
                Msg.error("Type Error on test " + cwdpath)
        fcode.write(str(code))
        fcode.close()
        fout.close()
        ferr.close()
