for i in range(0,5):
    print(i)
    
shoppingList = ["Milk", "Eggs", "Oranges"]
for i in shoppingList:
    print(i)
    
for i in range(0,101,2): #range take in 3 values the starting value,the ending value +1 , and incrementator
    print(i)
    
    

def piglatinify(word):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]

   
   
   if word[0:1] != vowels:
        return word[1:] + word[0:1] + 'ay'
    else:      
        return word + 'ay'

