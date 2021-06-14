import os
import sys


def main():
    ur_char = input("Give 10 character words: ")
    if len(ur_char) < 10:
        print("Add more characters")
    elif len(ur_char) > 10:
        print("Please add 10 characters only.")
    ur_list = list(ur_char)
    print(ur_list)
    for k in iter(ur_list):
        print(f"key {k}")
    # I'm not getting how to count the characters the user inputs
    # Should I let the program count the no. of characters even if its < or > 10?
    return os.X_OK


if __name__ == '__main__':
    sys.exit(main())
