import os
import sys
import random

"""
Notes (updated notes at the top):
- range(start, stop, step): ask the user for start, stop and step. That's all that's required.
It doesn't need to be random.
- The questions required you to view the arguments of the range function
then ask the user for them. You can find the documentation of range at 
https://docs.python.org/3/library/stdtypes.html#ranges
- Give your variables meaningful names; you might notice that PyCharm
adds squiggles to your variables when they are ambiguous 
(see https://drive.google.com/file/d/1QI36ckb3meTHh-oIl9Vx0cAkpbMUVDWK/view?usp=sharing)
- see the file scores.txt for scoring notes
"""


def main():

    r1 = int(input("Give start range: "))
    r2 = int(input("Give end range: "))
    r_k = int(input("Give value of k: "))
    r_rand = random.choices(range(r1, r2), k=r_k)
    rand_list = list(r_rand)
    print(rand_list)
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
