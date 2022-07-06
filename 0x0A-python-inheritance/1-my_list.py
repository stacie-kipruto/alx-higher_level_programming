#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """
    extends the list class
    """
    def print_sorted(self):
        print(sorted(self))
