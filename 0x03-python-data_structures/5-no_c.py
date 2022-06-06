#!/usr/bin/python3
def no_c(my_string):
    s = " "
    for char in my_string:
        if char != "c" or char != "C":
            continue
        s += char
    return s
