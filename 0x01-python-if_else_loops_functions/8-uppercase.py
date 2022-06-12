#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if i.islower():
            string += chr(ord(i) - 32)
        else:
            string += i
    print("{}".format(string))
