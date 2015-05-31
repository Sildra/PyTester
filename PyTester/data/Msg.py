red = ""
green = ""
yellow = ""
orange = ""
blue = ""
violet = ""
reset = ""
debug = violet + "[DEBUG] " + reset
module = violet + "[MODULE] " + reset
core = orange + "[_CORE_] " + reset
warn = yellow + "[WARNING] " + reset
cat = blue + "[CATEGORY] " + reset
error = red + "[ERROR] " + reset
info = green + "[INFO] " + reset
status_ok = green + "[OK] " + reset
status_ko = red + "[KO] " + reset


def change():
    global debug, module, core, warn, cat, error, info, status_ok, status_ko
    debug = violet + "[DEBUG] " + reset
    module = violet + "[MODULE] " + reset
    core = orange + "[_CORE_] " + reset
    warn = yellow + "[WARNING] " + reset
    cat = blue + "[CATEGORY] " + reset
    error = red + "[ERROR] " + reset
    info = green + "[INFO] " + reset
    status_ok = green + "[OK] " + reset
    status_ko = red + "[KO] " + reset


def to8c():
    global red, green, yellow, orange, blue, violet, reset
    red = "\e[31m"
    green = "\e[32m"
    yellow = "\e[33m"
    orange = "\e[33m"
    blue = "\e[34m"
    violet = "\e[35m"
    reset = "\e[0m"
    change()
    print(info + "Mode 8 colors loaded")


def to256c():
    global red, green, yellow, orange, blue, violet, reset
    red = "\e[38;5;124m"
    green = "\e[38;5;70m"
    yellow = "\e[38;5;178m"
    orange = "\e[38;5;208m"
    blue = "\e[38;5;69m"
    violet = "\e[38;5;90m"
    reset = "\e[0m"
    change()
    print(info + "Mode 256 colors loaded")
