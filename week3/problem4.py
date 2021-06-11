import os
import sys
import random


def main():
    x = random.choices(range(50, 76), k=100)
    print(f"x = {x}")
    x_sort = sorted(x)
    print(f"x after sorting = {x_sort}")
    print(x_sort[0] == min(x_sort))
    print(x_sort[99] == max(x_sort))

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
