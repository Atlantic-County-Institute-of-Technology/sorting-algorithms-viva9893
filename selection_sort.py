# 01_bubble_sort.py
# author: Cesar Vivas
# last update:

# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(-100, 100) for i in range(10)]
print(f"Initial Values = {values}")


# perform the bubblesort

def selection_sort(values):
    for i in range(len(values)):
        #
        min_index = i

        for j in range(i+1,len(values)):

            if values[min_index] > values[j]:
                min_index = j
            #sort

        values[i], values[min_index] = values[min_index], values[i]

    return values
print(f"Sorted Values = { selection_sort(values)}")


