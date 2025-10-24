
# 01_bubble_sort.py
# author: Cesar Vivas
# last update:

#imports 
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from selection_sort import selection_sort


def main():
    
    # start menu
    print("You have entered SORTED-SORTS")
    print("By using this application you have agree to generating random list  to run different sorting algorithms ")
    print("If at time you wish not to continue, press '0', and you will be allowed to leave the program")

    # key variables and imports 
    indices = 10
    
    while True:
        print("[-] 0. Exit Site\n"
      "[-] 1. generate a list \n")
        try:
            selection = int(input("Please select an option (0-1): "))
        except ValueError:
            print("(Invalid input")

        if selection == 0:
            print("Program is existing")
            exit()
        elif selection == 1:
             # code will start with a preset list of 10
            # generate a list of 10 random numbers from -100 to 100
            list = [random.randint(-1000, 1000) for i in range(indices)]
            print(f"Generated list = {list}")

            while True:
                print("[-] 0. Exit\n"
                      "[-] 1. Resize list\n"
                      "[-] 2. Sort list \n" 

                      )

                try:
                    selection_0 = int(input("Please select an option(0-4) : "))
                except ValueError:
                    print("(Invalid input")
                    continue

                if selection_0 == 0:
                    print("Program is existing")
                    exit()

                elif selection_0 == 1:  # option 1 - resize list by adding indices
                #User can adjust the parameters for the list
                    print(f"current amount of indices is : {indices}")
                    while True:
                        try:
                            added_indexes = int(input("please indicate a value for how much indexes will be add add : "))
                            if added_indexes >= 0:
                                indices += added_indexes
                                break  #end loop if input is valid
                            assert isinstance(added_indexes,int) and added_indexes > 0 
                        except AssertionError:
                            print("Value must be an integer an postive, try again")
                            
                elif selection_0 == 2: #option 2 - apply a sorting algorithm.
                    while True:
                
                        print("[-] 1. bubble_sort\n"
                            "[-] 2. selection_sort\n"
                            "[-] 3. insertion_sort \n" 
                      )

                        try:
                            selection_2 = int(input("Please indicate an algorthim to sort the list (1-3) : "))
                        except ValueError:
                            print("(Invalid input")
                            continue
                        if selection_2 == 1: 
                            sorted_list = bubble_sort(list) 
                            print(f"old list = {list} ")
                            print(f"sorted list = {sorted_list}")
                            break 
                        elif selection_2 == 2: 
                            sorted_list = selection_sort(list) 
                            print(f"old list = {list} ")
                            print(f"sorted list = {sorted_list}")
                            break
                        elif selection_2 == 3: 
                            sorted_list = insertion_sort(list)
                            print(f"old list = {list} ")
                            print(f"sorted list = {sorted_list}")
                            break
                        else:
                            print("invalid choice")
                                



if __name__ == "__main__":
    main()
