import os
import sys
import random

"""
Notes:
- Please rename variables
- Otherwise excellent attempt
"""

def main():
    x = random.choices(range(5), k=20)
    y = x.count(0)
    z = x.count(1)
    w = x.count(2)
    s = x.count(3)
    t = x.count(4)
    print(f'x = {x}')
    print(f'no. of zeroes = {y}, no. of ones = {z}, no. of twos = {w}, no. of threes = {s}, no. of fours = {t}')

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
