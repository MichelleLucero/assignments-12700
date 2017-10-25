"""
def score(w):
    letters = list(w)
    points = 0
    for i in letters:
        if i in 'a,e,i,o,u,l,n,r,s,t':
            points += 1  
        if i in 'd,g':
            points += 2
        if i in 'b,c,m,p':
            points += 3
        if i in 'f,h,v,m,y':
            points += 4
        if i in 'k':
            points += 5
        if i in 'j,x':
            points += 8
        if i in 'q,z':
            points += 10
    return points
print(score('hello'))
"""


points = {'a':1,'e':1,'i':1,'o':1,'u':1,'l':1,'n':1,'r':1,'s':1,'t':1,
          'd':2,'g':2,'b':3,'c':3,'m':3,'p':3,'f':4,'h':4,'v':4,'w':4,
          'y':4,'k':5,'j':8,'x':8,'q':10,'z':10}


def score(w):
    w = w.lower()
    score = 0
    for i in w:
        if i in points:
            score += points[i]
    return score

print(score('hello'))






    
    
        
    
    
    