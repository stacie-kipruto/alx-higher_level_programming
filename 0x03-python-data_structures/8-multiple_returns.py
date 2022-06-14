#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    return (str_len, sentence[0] if str_len > 0 else None)
