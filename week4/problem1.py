import os
import sys

import random


def main():
    bases = ['A', 'T', 'G', 'C']
    seq = random.choices(bases, k=100)
    print("Given sequence =", seq)
    k = int(input("Give k_mer: "))
    for value in range(len(seq) - k + 1):
        val_k = seq[value: value + k]
        print(val_k)

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
