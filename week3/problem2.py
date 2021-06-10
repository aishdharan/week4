import os
import sys


def main():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    d = int(input("d = "))
    e = int(input("e = "))
    f = int(input("f = "))
    g = int(input("g = "))
    h = int(input("h = "))
    list1 = [[a, b],
             [c, d]]
    print(f'list1 = {list1}')
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
