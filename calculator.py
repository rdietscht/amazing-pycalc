"""Simple Python module used for math computations.

    Authors: Rafael D. and [Yo Name Fool]

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
    print(f"RESULT (a * b): a * b")


def div_numbers():
    print(f"\nDIVISION OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a / b): {a * b}")


def exp_numbers():
    print(f"\nEXPONENT OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]
    print(f"RESULT (a ^ b): {a ** b}")


def avg_numbers():
    print("\nAVERAGE OPERATION:\n")
    raw_nums = input('Enter in a list of space-separated numbers "a b c ... n": ').split()
    nums = [int(raw_num) for raw_num in raw_nums]

    # Sum, then divide by number of user entries.
    total = 0.0
    i = 0
    while (i <= len(nums)):
        total += nums[i]
        i += 1

    print(f"RESULT (avg): {total / len(nums)}")


def hyp_numbers():
    print("\nHYPOTENUSE OPERATION:\n")
    a, b = input('Enter in two, space-separated numbers "a b": ').split()
    a, b = [int(a), int(b)]

    # Compute the exponent of both a AND b.
    a_sqrd = 0.0
    b_sqrd = 0.0
    for i in range(a):
        a_sqrd += a
    for i in range(b):
        b_sqrd += b

    print(f"RESULT (hypotenuse): {math.sqrt(a_sqrd + b_sqrd)}")


def main():

    # Define options for the calculator.
    opts = [
        ('A', 'Addition', add_numbers),
        ('B', 'Subtraction', sub_numbers),
        ('C', 'Multiplication', mlt_numbers),
        ('D', 'Division', div_numbers),
        ('E', 'Exponentiation', exp_numbers),
        ('F', 'Average', avg_numbers),
        ('G', 'Hypotenuse', hyp_numbers)
    ]

    prompt_user(opts)
    user_in = input('Enter option: ').upper()
    while (user_in != 'Q'):

        # Use the defined options for our calculator to compute user inputs.
        if (user_in == opts[0][0]):
            opts[0][2]()
        elif (user_in == opts[1][0]):
            opts[1][2]()
        elif (user_in == opts[2][0]):
            opts[2][2]()
        elif (user_in == opts[3][0]):
            opts[3][2]()
        elif (user_in == opts[4][0]):
            opts[4][2]()
        elif (user_in == opts[5][0]):
            opts[5][2]()
        elif (user_in == opts[6][0]):
            opts[6][2]()
        else:
            print(f"\nInvalid option {user_in}, please select a valid option.")

        # Keep asking for user input.
        prompt_user(opts)
        user_in = input('Enter option: ').upper()


if __name__ == '__main__':
    main()
