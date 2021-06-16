import os
import sys

"""
Notes:
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
    # fixme: consider using a try/except block here
    try:
        assert len(usr_char) == 10
    except AssertionError:
        print("Give 10 characters only")
    print(f"No. of characters given: {len(usr_char)}")
    usr_dict = dict()
    # fixme: you can run a for loop over a string without the need to pass it to iter()
    for k in usr_char:
        # print(f"key {k}")
        usr_dict[k] = usr_dict.get(k, 0) + 1

    print(f"count of all characters: {usr_dict}")

    return os.X_OK


if __name__ == '__main__':
    sys.exit(main())
