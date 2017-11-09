def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    
    for i in range(len(wordlist)):
        w = wordlist[i]
        if i == len(wordlist) - 1:
            nw = ""
        else:
            nw = wordlist[i+1]
        
        d.setdefault(w, [])
        # d[w] is the value of the key which is a []
        # the list which is a value can be appended 
        d[w].append(nw)
    return d

def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwcd(l)
    return d


d = bwcff("hamlet.txt")