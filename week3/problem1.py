import os
import sys
import random


def main():
    r = int(input("Give a number: "))
    x = random.choices(range(10), k=10)
    print(x)
    if r in x:
        print("You win!")
    else:
        print("You lose :(")
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
