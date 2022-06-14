#!/usr/bin/python3
def no_c(my_string):
    s = ""
    for char in my_string:
        if char != "c" and char != "C" :
         s += char

    return s
