from overload import overload


class Visitor:
    """description of class"""
    depth = 0

    @staticmethod
    @overload
    def accept(obj):
        pass
