import os
import sys


def main():
    usr_char = input("Give 10 character words: ")
    if len(usr_char) < 10:
        print("Add more characters")
    elif len(usr_char) > 10:
        print("Please add 10 characters only.")
    usr_dict = dict()
    for k in iter(usr_char):
        print(f"key {k}")
        usr_dict[k] = usr_dict.get(k, 0) + 1

    print(f"count of all characters: {usr_dict}")

    return os.X_OK


if __name__ == '__main__':
    sys.exit(main())
