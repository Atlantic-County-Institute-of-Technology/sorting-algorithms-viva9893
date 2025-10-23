





def main():
    # start menu
print("You have entered SORTED-SORTS")
print("By using this application you have agree to generating random list  to run different sorting algorithms ")
print("If at time you wish to not continue press '0', and you will be allow to leave the program")

print("[-] 0. Exit Site\n"
      "[-] 1. Create a list \n")




selection = int(input("Please select an option : "))








    while True:
        print("[-] 0. Exit\n"
              "[-] 1. Add apples to count 🍎 \n"
              "[-] 2. New items \n"

              )

        try:
            selection = int(input("Please select an option : "))
        except ValueError:
            print("(Invalid input")
            continue

        if selection == 0:
            print("Program is existing")
            exit()
        elif selection == 1:

            # user will be allow to to add as many apples as they want
            print(f" Current Count {apples}X apples")
            added_apples = int(input("> how many apples would you like to add to the terminal: "))
            apples += added_apples
            print(f" your new count will {apples}x apples ")

        elif selection == 2:
            while True:
                # menu / assigned apple values

                print("-______________________________-\n"

                      "| MENU                 |  X🍎 |\n"

                      "|_____________________________|\n"

                      "|1- Chop-Chop Fruit    |  2   |\n"

                      "|2- Dragon-Dragon Fruit| 14   |\n"

                      "|3- Bird-Bird Fruit    |  3   |\n"

                      "|4- Nike Fruit         | 15   |\n"

                      "|-____________________________|\n")

                devil_fruit_menu = {

                    '1': 2,

                    '2': 14,

                    '3': 3,

                    '4': 15,

                }
                # input
                item_selection = input("Please decide on a devil fruit to buy!? (1-4): ")

                if item_selection not in devil_fruit_menu:
                    print("Invalid option. Please select 1-4.")
                    # error validation  for menu option

                    continue

                try:

                    item_buying = int(input("How many are you buying: "))

                    if item_buying <= 0:
                        print(" please buy at least 1 item from shop.")

                        continue

                except ValueError:

                    print(" Invalid number. Please enter a valid amount.")

                    continue

                # total sum of check
                apples_spent = item_buying * devil_fruit_menu[item_selection]

                # in case the user does not meet the required amounts apples this if statement will prevent the user from making any purchase
                if apples >= apples_spent:

                    apples -= apples_spent

                    print(f"- {apples_spent} X🍎 spent")
                    print(f"- new apple count: {apples} X🍎")

                else:

                    print(f" Not enough apples! Current count: {apples} ")


if __name__ == "__main__":
    main()