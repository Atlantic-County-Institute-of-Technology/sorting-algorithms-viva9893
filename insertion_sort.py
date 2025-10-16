# 01_bubble_sort.py
# author: Cesar Vivas
# last update:

# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(-100, 100) for i in range(10)]
print(f"Initial Values = {values}")



# perform insertion sort

def insertion_sort(values):

    for i in range(1,len(values)):

        j = i-1
        temp = values[i]
        while j >= 0 and temp < values[j]:
            values[j+1] = values[j]
            j -= 1
        values[j+1] = temp
    return values
print(f"Sorted Values = {insertion_sort(values)}")
