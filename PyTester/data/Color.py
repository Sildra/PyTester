""" Module used to colorize strings """

red_color = ""
green_color = ""
yellow_color = ""
orange_color = ""
blue_color = ""
violet_color = ""
reset = ""


def debug():
    return violet_color + "[DEBUG]" + reset


def module():
    return violet_color + "[MODULE]" + reset


def core():
    return orange_color + "[_CORE_]" + reset


def warn():
    return yellow_color + "[WARN]" + reset


def cat():
    return blue_color + "[CATEGORY]" + reset


def error():
    return red_color + "[ERROR]" + reset


def info():
    return green_color + "[INFO]" + reset


def red(msg):
    return red_color + msg + reset


def green(msg):
    return green_color + msg + reset


def yellow(msg):
    return yellow_color + msg + reset


def orange(msg):
    return orange_color + msg + reset


def blue(msg):
    return blue_color + msg + reset


def violet(msg):
    return violet_color + msg + reset


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
    info()


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
    info()
