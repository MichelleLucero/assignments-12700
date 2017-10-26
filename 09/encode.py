encoder = []

def encode(s):
    counter = 1
    first = s[0]
    rest = s[1:]
    for i in range(len(s)):
        if first in rest:
            counter += 1
            encoder.append(first)
            encoder.append(counter)
        else:
            if first != rest:
                encoder.append(first)
                
        
    return encoder

print(encode('aaaba'))
            