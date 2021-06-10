import os
import sys
import random


def main():
    r = int(input("Give a range: "))
    l = int(input("Give value of k: "))
    x = random.choices(range(r), k=l)
    x_list = list(x)
    print(x_list)
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
