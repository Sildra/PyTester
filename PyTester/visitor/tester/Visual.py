import os

from data import Msg


class Visual:
    @staticmethod
    def start(obj):
        Msg.violet("[VISUAL]", obj.name)
        for files in os.listdir(os.path.join(obj.path, "_test")):
            if os.path.isfile(os.path.join(obj.path, "_test", files)):
                Msg.yellow(files, "", "  " * (obj.depth + 1))
                for line in open(os.path.join(obj.path, "_test", files)):
                    print(os.linesep + "  " * (obj.depth + 2) + line)
