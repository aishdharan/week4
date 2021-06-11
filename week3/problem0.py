import os
import sys
import random

"""
Notes:
- The questions required you to view the arguments of the range function
then ask the user for them. You can find the documentation of range at 
https://docs.python.org/3/library/stdtypes.html#ranges
- Give your variables meaningful names; you might notice that PyCharm
adds squiggles to your variables when they are ambiguous 
(see https://drive.google.com/file/d/1QI36ckb3meTHh-oIl9Vx0cAkpbMUVDWK/view?usp=sharing)
- see the file scores.txt for scoring notes
"""


def main():
    r = int(input("Give a range: "))
    r_k = int(input("Give value of k: "))
    r_rand = random.choices(range(r), k=r_k)
    r_list = list(r_rand)
    print(r_list)
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
