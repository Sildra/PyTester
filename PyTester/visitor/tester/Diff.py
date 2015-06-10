import os
import difflib
import sys
import filecmp

join = os.path.join


class Diff:
    @staticmethod
    def start(obj):
        inpath = join(obj.path, "_test")
        outpath = join(obj.path, "_cache")
        obj.tested = 1
        obj.passed = 1
        dcompare = filecmp.dircmp(inpath, outpath, ignore=["input"])
        for file in dcompare.left_only:
            obj.passed = 0
            obj.add_empty(file)
        for file in dcompare.diff_files:
            infile = join(inpath, file)
            outfile = join(outpath, file)
            inlines = open(infile, 'U').readlines()
            outlines = open(outfile, 'U').readlines()
            diff = difflib.unified_diff(inlines, outlines)
            obj.passed = 0
            obj.add_diff(file, diff)
