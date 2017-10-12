
import math


def rotate_char(c,r):
    """
    Rotates character c by amount r. 
    """
    let = ord(c) + r
    
    if let > 122:
        let = let - 26
        
    elif let < 97:
       let = let + 26
        
    return chr(let)


def encode_string(s,r):
    """
    rotate a string (lower case letters only)
    """
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result

def full_encode(s):
    """
takes a string and returns a string representing all the valid rotations,
one per line (embed the \n to get a newline).
    """
    x = ''
    for i in range(26):
        x += encode_strings(s,i) + "\n"
    return x



def distance(l1,l2):
    """
    Euclidean distance between l1 and l2. If the lists are of 
    different lengths, go to the lenght of the shorter one
    """
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d
    
def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)

    return v
build_frequency_vector
def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])
        
def decode(s):
    freq = []
    for i in range(26):
        all_str = encode_string(s,i)
        all_freq = build_frequency_vector(all_str)
        dt = distance(real_stats, all_freq) #I know what this does just not how
        freq.append(dt)
        s_pos = freq.index(min(freq))  #position of the smallest value/creds to Shariar for that nice use of 'index'
        small = encode_string(s, s_pos) 
    return small
                      

f = open('pg1661.txt')
r= f.read()
r = r.lower()
real_stats = build_frequency_vector(r)
f.close()

s = 'Living that bum life'
print ("encoded sentence: " + encode_string(s,9))
print ("decoded sentence: " + decode(s))

        
        