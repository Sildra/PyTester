from data import Color


def debug(msg, prefix=""):
    print(prefix + Color.debug() + " " + msg)


def module(msg, prefix=""):
    print(prefix + Color.module() + " " + msg)


def core(msg, prefix=""):
    print(prefix + Color.core() + " " + msg)


def warn(msg, prefix=""):
    print(prefix + Color.warn() + " " + msg)


def cat(msg, prefix=""):
    print(prefix + Color.cat() + " " + msg)


def error(msg, prefix=""):
    print(prefix + Color.error() + " " + msg)


def info(msg, prefix=""):
    print(prefix + Color.info() + " " + msg)


def red(label, msg, prefix=""):
    print(prefix + Color.red(label) + " " + msg)


def green(label, msg, prefix=""):
    print(prefix + Color.green(label) + " " + msg)


def yellow(label, msg, prefix=""):
    print(prefix + Color.yellow(label) + " " + msg)


def orange(label, msg, prefix=""):
    print(prefix + Color.orange(label) + " " + msg)


def blue(label, msg, prefix=""):
    print(prefix + Color.blue(label) + " " + msg)


def violet(label, msg, prefix=""):
    print(prefix + Color.violet(label) + " " + msg)
