import os
import sys
import random

"""
Notes
- The same feedback applies on variable names (see problem0.py).
- While it is good that you have implemented an if statement it would 
have been perfectly OK to simply use a boolean as below. Please keep
in mind that I only expect students to apply what they have learned
so far so please do not feel any pressure to use unfamiliar libraries
and constructs. Programming thinking always involves using available
resources and the quality of your code tanks the moment you use
constructs that you are unfamiliar with. The focus should be on 
the thinking process.
"""


def main():
    r = int(input("Give a number: "))
    x = random.choices(range(10), k=10)
    print(x)
    print(f"You win? {r in x}")  # this is sufficient
    # if r in x:
    #     print("You win!")
    # else:
    #     print("You lose :(")
    return os.X_OK


if __name__ == "__main__":
    sys.exit(main())
