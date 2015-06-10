red_color = ""
green_color = ""
yellow_color = ""
orange_color = ""
blue_color = ""
violet_color = ""
reset = ""


def debug(msg, prefix=""):
    print(prefix + prefix + violet_color + "[DEBUG]" + reset + " " + msg)

def module(msg, prefix=""):
    print(prefix + violet_color + "[MODULE]" + reset + " " + msg)

def core(msg, prefix=""):
    print(prefix + orange_color + "[_CORE_]" + reset + " " + msg)

def warn(msg, prefix=""):
    print(prefix + yellow_color + "[WARN]" + reset + " " + msg)

def cat(msg, prefix=""):
    print(prefix + blue_color + "[CATEGORY]" + reset + " " + msg)

def error(msg, prefix=""):
    print(prefix + red_color + "[ERROR]" + reset + " " + msg)

def info(msg, prefix=""):
    print(prefix + green_color + "[INFO]" + reset + " " + msg)

def red(label, msg, prefix=""):
    print(prefix + red_color + label + reset + " " + msg)

def green(label, msg, prefix=""):
    print(prefix + green_color + label + reset + " " + msg)

def yellow(label, msg, prefix=""):
    print(prefix + yellow_color + label + reset + " " + msg)

def orange(label, msg, prefix=""):
    print(prefix + orange_color + label + reset + " " + msg)

def blue(label, msg, prefix=""):
    print(prefix + blue_color + label + reset + " " + msg)

def violet(label, msg, prefix=""):
    print(prefix + violet_color + label + reset + " " + msg)

def to8c():
    global red_color
    global green_color
    global yellow_color
    global orange_color
    global blue_color
    global violet_color
    global reset
    red_color = "\033[31m"
    green_color = "\033[32m"
    yellow_color = "\033[33m"
    orange_color = "\033[33m"
    blue_color = "\033[34m"
    violet_color = "\033[35m"
    reset = "\033[0m"
    info("Mode 8 colors loaded")


def to256c():
    global red_color
    global green_color
    global yellow_color
    global orange_color
    global blue_color
    global violet_color
    global reset
    red_color = "\033[38;5;124m"
    green_color = "\033[38;5;70m"
    yellow_color = "\033[38;5;178m"
    orange_color = "\033[38;5;208m"
    blue_color = "\033[38;5;69m"
    violet_color = "\033[38;5;90m"
    reset = "\033[0m"
    info("Mode 256 colors loaded")

