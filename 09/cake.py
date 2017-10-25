
def divide(A,B,u):
    divider = A/B
    cake_divider = divider * u
    people = cake_divider **-1
    return int(people)

print(divide(5,10,1))