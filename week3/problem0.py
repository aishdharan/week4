import os
import sys

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
    # simpler is simply the names of the arguments as the occur in range()
    start = int(input("Give start range: "))
    stop = int(input("Give end range: "))
    step = int(input("Give step value: "))
    r_list = list(range(start, stop, step))
    print(r_list)
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
