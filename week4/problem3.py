import random
import string
import sys

"""
Notes:
- Well done! I've checked the values carefully and your code
seems to be doing the right thing.
"""


def main():
    v1 = random.choices(range(101), k=100)
    lower_alpha = string.ascii_lowercase
    random_letter = random.choices(lower_alpha, k=100)
    v2 = random.choices(range(101), k=100)
    lower_alpha2 = string.ascii_lowercase
    random_letter2 = random.choices(lower_alpha2, k=100)
    d1 = dict(zip(random_letter, v1))
    d2 = dict(zip(random_letter2, v2))
    print("d1 = ", d1)
    print("d2 = ", d2)
    d3 = dict(d1)
    d3.update(d2)
    for i, j in d1.items():
        for x, y in d2.items():
            if i == x:
                d3[i] = (j + y)
    print(f"d1 + d2 = {d3}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
