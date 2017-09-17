

def piglatinify(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    if word[0:1] in vowels:
        return word + 'ay'
    
    else:
        return word[1:] + word[0:1] + 'ay'


