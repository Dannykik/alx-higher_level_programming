#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first = ' '
    if leng != 0:
        first = sentence[0]
        return leng, first
    else:
        first = None
        return first
