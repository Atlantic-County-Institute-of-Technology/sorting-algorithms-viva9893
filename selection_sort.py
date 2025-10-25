# 01_selection_sort.py
# author: Cesar Vivas
# last update:10.24.25



# perform the selection sort

def selection_sort(values):
    sorting_actions = 0

    for i in range(len(values)):

        min_index = i
        # assume j begins at index 1 directly infrom index i
        for j in range(i+1,len(values)):

            if values[min_index] > values[j]:
                # if j has value less than i then it will become the new min index
                min_index = j
                # asumme a sorting actions will always excute when j becomes new min
                sorting_actions += 1

        # sorting action (SWAP) if  min_index  does not come before the second index
        values[i], values[min_index] = values[min_index], values[i]
        print(f"sorting actions = {sorting_actions}")
    return values



