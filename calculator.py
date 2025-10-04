"""Simple Python module used for math computations.

    Authors: Rafael D. and [Your Name]

"""
import math


def prompt_user(opts):

    print("Welcome to the calculator.")
    print()
    print("Select an option:\n")
    [print(f"\tOption {opt[0]}: {opt[1]}") for opt in opts]
    print()


def add_numbers():
    print(f"\nADDITION OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a + b): {a + b}")


def sub_numbers():
    print(f"\nSUBTRACTION OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a - b): {a - b}")


def mlt_numbers():
    print(f"\nMULTIPLICATION OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a * b): {a * b}")


def div_numbers():
    print(f"\nDIVISION OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a / b): {a * b}")


def exp_numbers():
    print(f"\nEXPONENT OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a ^ b): {a * b}")


def avg_numbers():
    print("\nAVERAGE OPERATION:\n")
    raw_nums = input('Enter in a list of space-separated numbers "a b c ... n": ').split()
    nums = [int(raw_num) for raw_num in raw_nums]

    # Sum, then divide by number of user entries.
    total = 0.0
    for num in nums:
        total += num

    print(f"RESULT (avg): {total / len(nums)}")


def hyp_numbers():
    print("\nHYPOTENUSE OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (hypotenuse): {math.sqrt((a ** 2) + (b ** 2))}")


def main():

    # Define options for the calculator.
    opts = [
        ('A', 'Addition', add_numbers),
        ('B', 'Subtraction'),
        ('C', 'Multiplication'),
        ('D', 'Division'),
        ('E', 'Exponentiation'),
        ('F', 'Average'),
        ('G', 'Hypotenuse')
    ]

    prompt_user(opts)
    user_in = input('Enter option: ').upper()
    while (user_in != 'Q'):

        if (user_in == 'A'):
            opts[0][2]()
        elif (user_in == 'B'):
            sub_numbers()
        elif (user_in == 'C'):
            mlt_numbers()
        elif (user_in == 'D'):
            div_numbers()
        elif (user_in == 'E'):
            exp_numbers()
        elif (user_in == 'F'):
            avg_numbers()
        elif (user_in == 'G'):
            hyp_numbers()
        else:
            print(f"\nInvalid option {user_in}, please select a valid option.")

        # Keep asking for user input.
        prompt_user(opts)
        user_in = input('Enter option: ')


if __name__ == '__main__':
    main()
