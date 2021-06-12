import os
import sys

"""
Notes:
- This is excellent! However, I would like you to use only range().
Revisit the notes with regard to slicing
"""


def main():
    x = list(range(12, 2, -1))
    # don't use slices for this
    # print(x[::-1])
    # I'm confident you can figure it out
    print(f"x reversed = {x}")

    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
