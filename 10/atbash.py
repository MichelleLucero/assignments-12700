"""
The Atbash cipher is a simple substitution cipher that
relies on transposing all the lettersin the alphabet such
that the resulting alphabet is backwards. The first letter is
replaced with the last letter, the second with the second-last,
and so on.
"""


w = 'almnobc'

def atbash(w):
    rw =''
    w.lower
    for i in w:
        o = ord(i)
        if 97 <= o <= 122:
            bco = o - 97
            co = 122 - bco
            r = chr(co)
            rw = rw + r
    return rw


print(atbash(w))
        