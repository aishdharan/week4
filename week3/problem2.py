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
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    e = int(input("e = "))
    f = int(input("f = "))
    g = int(input("g = "))
    h = int(input("h = "))
    # fixme: replace list1 (generic name)
    list1 = [[a, b],
             [c, d]]
    print(f'list1 = {list1}')
    # fixme: replace list2
    list2 = [[e, f],
             [g, h]]
    print(f'list2 = {list2}')
    w = a * e + b * g
    x = a * f + b * h
    y = c * e + d * g
    z = c * f + d * h
    list3 = [[w, x],
             [y, z]]
    print(f'list1 x list2 = {list3}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
