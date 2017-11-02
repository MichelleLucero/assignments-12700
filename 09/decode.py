#Zamansky's rle
def rle(s):
    encoded = []
    while len(s)>1:
        runlen = 1
        runchar = s[0]
        while runlen < len(s) and s[runlen]==runchar:
            runlen = runlen + 1
        if runlen>1:
            encoded.append(runlen)
        encoded.append(runchar)
        s=s[runlen:]
    return encoded


s = "aavbbbbbccdddddd"
print(s)
print(rle(s))


def rle_decode(l):
    str = ""
    tim = 0
    for i, o in enumerate(l):
        if (type(i) == int):
            str = l[i] * i[i+1]
                                         
        else:
            str = l[i]
    return str
        
print(rle_decode(rle(s)))     
        
        