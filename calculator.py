"""Simple Python module used for math computations.

    Authors: Rafael D. and [Your Name]

"""


def prompt_user(opts):

    print("Welcome to the calculator.")
    print()
    print("Select an option:\n")
    [print(f"\tOption {opt[0]}: {opt[1]}") for opt in opts]
    print()


def main():

    # Define options for the calculator.
    opts = [
        ('A', 'Addition'),
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

        user_in = input('Enter option: ')


if __name__ == '__main__':
    main()
