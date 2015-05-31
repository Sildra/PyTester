import os


class Element:
    def __init__(self, path, name, depth=0, parent=None):
        self.name = name
        self.path = path
        self.depth = depth
        self.parent = parent
        self.options = {}
        options = os.path.join(path, "_options")
        if os.path.isfile(options):
            for line in open(options):
                args = line.replace(" ", "").split("=")
                if len(args) == 2:
                    self.options[args[0]] = args[1]

    def get_option(self, name, default=''):
        if name in self.options:
            return self.options[name]
        elif self.parent is not None:
            return self.parent.get_option(name, default)
        else:
            return default

    def accept(self, obj):
        pass
