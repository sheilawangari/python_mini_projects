# Binary search takes a list of ordered data and takes a target
# It splits that data into halves until it reaches its target 
# We'll create a function that takes a list and target parameter(it will take 2 parameters list and target)
# Multiples variables : start, middle, end, steps( the amount of time it has taken to get the target )
# Use recursion or while loop 
# Increase the steps each time a split is done 
# Conditions to track target positions in the list 


def binary_search(list, element):     # the element is the target to be reached
    middle = 0
    start = 0
    end = len(list)
    steps = 0 

    while(start <= end):                                     # this will loop until condition is not true
        print("Step", steps, ":" , str(list[start:end+1])) 

        steps= steps + 1                                     # updating the steps 
        middle = (start + end) // 2    

        if element == list[middle]:
            return middle 

        if element < list[middle]:
            end = middle - 1                                   # the end here is END OF NEW LIST. -1 is used because all indexex start from 0

        else:
            start = middle + 1 
    return - 1 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 2 

binary_search(my_list, target)