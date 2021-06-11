import os
import sys

"""
Notes
- What you have done is OK but I will show you a better way.

Typically, (and you will see this as you go further in bioinformatics)
real world programs are much, much larger than the problems we are 
working on in these challenges. This means that you will need to
be very efficient with how you use your memory. How you name variables is perhaps the most
important thing you do because it means that any time you look at 
a segment of code you can immediately understand what is going on. 
Furthermore, when you start writing function and classes, the naming
of functions and classes is instrumental. You will want them to be 
meaningful. Line 6 of the 'Zen of Python' 
(run 'import this' in the Python console), reads "Readability counts."

In this challenge we know we have two matrices A and B. While there
are examples where the elements of each are named a, b, c, d, e,...
this is not very helpful for two reasons:
1. you are spending variables; once you use b, c, d,... they are
typically not available again without overwriting;
2. they don't mean much.

Majority of examples use index notation. See https://en.wikipedia.org/wiki/Matrix_multiplication. 

Much better is either:
- A11 (element one), A12, A21, and so on, or
- a11, a12, ..., or
_ a_11, a_12

In this way we can always relate A*/a* to matrix A.

Of course, meaningful names depend on the context but this is 
by far one of the best skills you can ever develop: good naming.
"""


def main():
    A11 = int(input("A11 = "))
    A12 = int(input("A12 = "))
    A13 = int(input("A13 = "))
    A14 = int(input("A14 = "))
    B11 = int(input("B11 = "))
    B12 = int(input("B12 = "))
    B13 = int(input("B13 = "))
    B14 = int(input("B14 = "))
    # fixme: replace list1 (generic name)
    A1 = [[A11, A12],
             [A13, A14]]
    print(f'First Matrix = {A1}')
    # fixme: replace list2
    B1 = [[B11, B12],
             [B13, B14]]
    print(f'Second Matrix = {B1}')
    C11 = A11 * B11 + A12 * B13
    C12 = A11 * B12 + A12 * B14
    C13 = A13 * B11 + A14 * B13
    C14 = A13 * B12 + A14 * B14
    C1 = [[C11, C12],
             [C13, C14]]
    print(f'First Matrix x Second Matrix = {C1}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
