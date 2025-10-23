# 02_insertion_sort.py
# author: Cesar Vivas
# last update:
# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(-100, 100) for i in range(10)]
print(f"Initial Values = {values}")



# perform insertion sort

def insertion_sort(values):
    sorting_actions = 0
    for i in range(1,len(values)):

        j = i-1
        # take a temp value from index i
        temp = values[i]



        while j >= 0 and temp < values[j]:
            values[j+1] = values[j]
            # assume j index wil sift to the left
            j -= 1
        # reassign temp value to be the index infront of j
        values[j+1] = temp
        # add count to the amount of sorting actions we can assume code will execute any time temp is not equal to i
        if temp != i:
            sorting_actions += 1
    print(f"sorting actions = {sorting_actions}")
    return values
print(f"Sorted Values = {insertion_sort(values)}")
