# s = starting point of house
s = 7
# t = ending point of house
t = 11
# a = point of apple tree
a = 5
# b = point of orange tree
b = 15
# m = # of apples
m = 3
# n = # of oranges
n = 2


a_dist = [-2,2,1]
o_dist = [5,-6]


def apples_fall(a,s,t,a_dist):
    apples = 0
    for i in range(len(a_dist)):
        if s <= a + a_dist[i] <= t:
            apples += 1
    return apples


def oranges_fall(b,s,t,o_dist):
    oranges = 0
    for i in range(len(o_dist)):
         if s <= b + o_dist[i] <= t:
             oranges += 1
    return oranges

print("Sam has " + str(apples_fall(a,s,t,a_dist)) + " apples/apple on his house.")
print("Sam has " + str(oranges_fall(b,s,t,o_dist)) + " oranges/orange on his house.")
    
    

