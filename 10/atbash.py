
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
        