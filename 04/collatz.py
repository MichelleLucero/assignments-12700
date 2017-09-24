def collatz(number):
    
    if number % 2 == 0:
        print(number //2)
        return number //2
        
    elif number % 2 != 0:
        print(3 * number + 1)
        return 3 * number + 1
        
user_number = input('Type an integer:      ')
while user_number != 1:
    user_number = collatz(int(user_number))    