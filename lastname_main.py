
# 01_bubble_sort.py
# author: Cesar Vivas
# last update:
# import random library for list generation


def main():
    # start menu
    print("You have entered SORTED-SORTS")
    print("By using this application you have agree to generating random list  to run different sorting algorithms ")
    print("If at time you wish to not continue press '0', and you will be allow to leave the program")

    print("[-] 0. Exit Site\n"
          "[-] 1. generate a list \n")


    # key variables
    indices = 10





    try:
        selection = int(input("Please select an option : "))
    except ValueError:
        print("(Invalid input")

    if selection == 0:
        print("Program is existing")
        exit()
    elif selection == 1:
        while True:

            import random
            # generate a list of 10 random numbers from -100 to 100
            values = [random.randint(-1000, 1000) for i in range(indices)]
            print(f"list = {values}")

            while True:
                print("[-] 0. Exit\n"
                      "[-] 1. Resize list 🍎 \n"
                      "[-] 2. Sort list \n"

                      )

                try:
                    selection_0 = int(input("Please select an option(0-2) : "))
                except ValueError:
                    print("(Invalid input")
                    continue

                if selection_0 == 0:
                    print("Program is existing")
                    exit()

                elif selection_0 == 1:
                #Unser can adjust the perameters for the list
                    print(f"current amount of indices is : {indices}")
                    while True:
                        try:
                            added_indexes = int(input("please indicate a value for how much indexes will be add add : "))
                            if added_indexes >= 0:
                                indices += added_indexes
                                break  #end loop if input is vallued
                            assert added_indexes > 0
                        except AssertionError:
                            print("Number is invalid!")
                elif selection_0 == 2:





if __name__ == "__main__":
    main()