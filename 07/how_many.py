import operator
number = 3
num_list = [7,9,-10,1,2,3,4,5,3,10,-20]

def freq(n,l):
    counter = 0
    for i in range(len(l)):
        if(l[i] == n):
            counter += 1
    return counter

def min(l):
    min_counter = 0
    for i in l:
        if(i < min_counter):
            min_counter = i
    return min_counter

def mode(l):
    nums = {}
    for i in l:
        nums[i] = freq(i, l)
        mode = max(nums.keys(), key=(lambda k: nums[k]))
    return mode
    
print(str(num_list)) 
print("the frequency of 3 is "+ str(freq(3,num_list)))
print("the min number is " + str(min(num_list)))
print("the mode is "+ str(mode(num_list)))

