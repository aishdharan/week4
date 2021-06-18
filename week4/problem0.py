import os
import sys

"""
Notes:
- Some of the constraints in the challenges are only artificial to stretch you. 
Remember your goal is to be able to write code exactly to your desired outcome
and this usually entails having a constraint. In my experience, it is very
helpful to separate the requirements from the task of programming since as you
get sucked into solving the problem your focus gets redirected to minutiae.
- Excellent solution! I would not have thought of that but your way is 
perhaps the best I have seen ever. I would have done:

usr_dict = dict()
for k in usr_char:
    if k not in usr_dict:
        usr_dict[k] = 1
    else:
        usr_dict[k] += 1
"""


def main():
    usr_char = input("Give word of 10 characters: ")
    try:
        assert len(usr_char) == 10
    except AssertionError:
        # see https://github.com/sci2pro/pl1c-solutions
        # we write to sys.stderr for errors/warnings
        print("Give 10 characters only", file=sys.stderr)
        # terminate; user did not follow instructions
        return os.EX_USAGE
    # no need really since we know they should be 10
    print(f"No. of characters given: {len(usr_char)}")
    usr_dict = dict()
    for k in usr_char:
        # print(f"key {k}")
        usr_dict[k] = usr_dict.get(k, 0) + 1
    print(f"count of all characters: {usr_dict}")
    # if you're running this on Windows and os.EX_OK gives you an error
    # replace with 0
    # return os.X_OK
    return 0  # OK


if __name__ == '__main__':
    sys.exit(main())
