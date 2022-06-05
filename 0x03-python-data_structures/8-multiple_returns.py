#!/usr/bin/python3
def multiple_returns(sentence):
    le = len(sentence)
    if le == 0:
        return (le, None,)
    else:
        return (le, sentence[0],)
