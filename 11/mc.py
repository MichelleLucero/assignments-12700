import random

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


def tri_combo_dict(w):
    d = {}
    for i in range(len(w)-2):
        w1 = w[i]
        w2 = w[i+1]
        w3 = w[i+2]
        d.setdefault((w1,w2),w3)
        d[w1,w2].append(w3)
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
    d = tri_combo_dict(w)
    return d

def tri_generate_text(d,start_word,length=50):
    wordlist = []
    next = start_word
    for i in range(length):
        if next not in d:
            break
        wordlist.append(next)
        next = random.choice(d[next])
    return " ".join(wordlist)


hamlet = bwcff("hamlet.txt")
psalms = bwcff("psalms.txt")
sonnets = bwcff("sonnets.txt")
print(tri_combo_dict(hamlet))
