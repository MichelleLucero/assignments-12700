def strexp(s):
    
#if s = abc then retuen aababc
    
    l = len(s)
    i = 0
    while i < l:
        part = s[0:i+1]
        result = result + 1
        i = i + 1
    return result
    
    
    
strexp("abcd")


def strexp_for(s):
    
#if s = abc then retuen aababc
    
    l = len(s)
    result = ""
   for i in range(l):
        part = s[0:i+1]
        result = result + part
    return result

def strbits(s)
    l = len(s)
    result = ""
    for i in range(l)
        if i % 2 == 0:
            result = result + s[i]
    return result


    