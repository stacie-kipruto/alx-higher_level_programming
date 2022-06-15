#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary is {}:
        return "None"
    else:
        max = 0
        winner = ""

        for k, v in a_dictionary.items():
            if v > max:
                max = v
                winner = k
        return winner
