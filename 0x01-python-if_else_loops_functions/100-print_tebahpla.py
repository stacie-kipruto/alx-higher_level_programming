#!/usr/bin/python3
for i in reversed(range(65, 91)):
    print("{:c}".format(i + 32 if i % 2 == 0 else i), end="")
