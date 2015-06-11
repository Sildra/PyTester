from data.Category import Category


class Root(Category):
    """description of class"""
    instance = None

    def __init__(self, args, name="Root", depth=-1):
        super().__init__(args.path, name, depth)
        global instance
        instance = self
        self.args = args

    def accept(self, visitor):
        visitor.visit(self)
        if len(self.categories) > 0:
            for node in self.categories.values():
                node.accept(visitor)
                visitor.leave(self, node)

    @staticmethod
    def get_root_option(a, b):
        instance.get_option(a, b)

    @staticmethod
    def args():
        return instance.args
