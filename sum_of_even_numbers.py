# !/user/bin/env python3

# Created by Trent Hodgins
# Created on 10/27/2021
# This is the sum_of_numbers Mark program
# The program asks the user what their mark is
# The program then figures out and displays the sum_of_numbers of all the marks


def sum_of_numbers_numb(list_of_numbers):
    # This program uses a list to find the sum_of_numbers mark

    total = 0
    number_in_list = list_of_numbers[0]
    for element in list_of_numbers:
        if element % 2 == 0:
            total = element + number_in_list

    return total


def main():
    # Theis function gets the marks1

    list_of_numbers = []
    temp_w = None

    # input
    amount = input("How many numbers would you like to add: ")
    print("")

    try:
        amount_of_numbers = int(amount)
        for loop_counter in range(0, amount_of_numbers):
            temp_str = input("Number to add: ")
            temp_w = int(temp_str)
            list_of_numbers.append(temp_w)

        calculate = sum_of_numbers_numb(list_of_numbers)
        print("")
        print("The sum of the even numbers is {0}".format(calculate))

    except Exception:
        print("")
        print("Invalid input.")
        print("")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
