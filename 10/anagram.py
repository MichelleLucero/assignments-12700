"""
Given a word and a list of possible anagrams, select the correct sublist.

Given "listen" and a list of candidates like "enlists" "google" "inlets" "banana" the program should return a list containing "inlets".

"""

def anagram(w,l):
    count = 0
    for i in range(len(l)):
        curr_w = l[i]
        if len(curr_w) == len(w):
                for i in w:
                    if i in curr_w:
                        count += 1
                        ans = curr_w
                        if count == len(w):
                            return ans
w = 'listen'
l = ['enlists','google','inlets','banana']

soln = anagram(w,l)
print('Took me 3 hours to anagram ' + w + ' to ' + soln + '\n' + '#GoMichelle')

