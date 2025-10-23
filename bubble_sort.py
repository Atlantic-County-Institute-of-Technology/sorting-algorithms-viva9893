# 01_bubble_sort.py
# author: Cesar Vivas
# last update:
# import random library for list generation
import random

# generate a list of 10 random numbers from -100 to 100
values = [random.randint(-100, 100) for i in range(50)]
print(f"c{values}")


# perform the bubblesort
def bubble_sort(values):
    sorting_actions = 0
    for i in range(len(values) - 1):
        # assume the final value in each pass is sorted
        for j in range(len(values) -i - 1):

            # sorting action (SWAP) if consecutive action is less than lower index
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]

# add count to the amount of sorting actions
                sorting_actions +=1
    print(f"sorting actions = {sorting_actions}")
    return values
# called sorted list
print(f"Sorted Values = {bubble_sort(values)}")

