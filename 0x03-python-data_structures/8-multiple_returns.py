#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    first = sentence[0] if leng > 0 else None
    return leng, first
