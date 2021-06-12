import os
import sys

"""
Notes:
- This is A11n excellent illustration of 'running out of variables'
- Please see inline note 1 below
"""


def main():
    A11 = int(input("A11 = "))
    A12 = int(input("A12 = "))
    A13 = int(input("A13 = "))
    A14 = int(input("A14 = "))
    A15 = int(input("A15 = "))
    A16 = int(input("A16 = "))
    A17 = int(input("A17 = "))
    A18 = int(input("A18 = "))
    A19 = int(input("A19 = "))
    B11 = int(input("B11 = "))
    B12 = int(input("B12 = "))
    B13 = int(input("B13 = "))
    B14 = int(input("B14 = "))
    B15 = int(input("B15 = "))
    B16 = int(input("B16 = "))
    B17 = int(input("B17 = "))
    B18 = int(input("B18 = "))
    B19 = int(input("B19 = "))

    A1 = [[A11, A12, A13],
          [A14, A15, A16],
          [A17, A18, A19]]
    print(f'First Matrix = {A1}')
    B1 = [[B11, B12, B13],
          [B14, B15, B16],
          [B17, B18, B19]]
    print(f'Second Matrix = {B1}')
    """
    inline note 1:
    - I don't doubt the calculation below is correct but by being
    very hard to read it becomes prone to bugs.
    """
    C11 = A11 * B11 + A12 * B14 + A13 * B17
    C12 = A11 * B12 + A12 * B15 + A13 * B18
    C13 = A11 * B13 + A12 * B16 + A13 * B19
    C14 = A14 * B11 + A15 * B14 + A16 * B17
    C15 = A14 * B12 + A15 * B15 + A16 * B18
    C16 = A14 * B13 + A15 * B16 + A16 * B19
    C17 = A17 * B11 + A18 * B14 + A19 * B17
    C18 = A17 * B12 + A18 * B15 + A19 * B18
    C19 = A17 * B13 + A18 * B16 + A19 * B19
    C1 = [[C11, C12, C13],
          [C14, C15, C16],
          [C17, C18, C19]]
    # fixme: the user doesn't need to know the
    #  names of your variables; all they want is the name of matrices
    print(f'First Matrix x Second Matrix = {C1}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
