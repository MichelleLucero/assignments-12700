  #97-a 122-z but use 123
    #chr(99)--> 'c'
    #ord('c')--> 99


def encode_letter(c,r):
    
    let = ord(c) + r
    
    if let > 122:
        let = let - 26
        
    elif let < 97:
       let = let + 26
        
    return chr(let)


 
 
def encode_strings(s,r):
    return s[r:] + s[:r]




def full_encode(s):
    x = ''
    for i in range(26):
        x += encode_strings(s,i) + "\n"
    return x

print (full_encode('I need to practice coding'))


    


    
    


    
        
    
   
