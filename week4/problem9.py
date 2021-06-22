import sys


def main():
    # use the steps in the range function
    one = set(range(2, 101, 1))
    print(f"one = {one}")
    two = set(range(4, 101, 2))
    print(f"two = {two}")
    # you can do this!
    # ...
    s2 = {}
    # for s in range(4, 26):
    s2_1 = set(range(4, 49))
    s2_2 = set(range(49, 101))
    # fixme: no need for for loops in this problem; only set arithmetic
    for s in s2_1:
        for k in s2_2:
            s2 = s2_1.union(s2_2)
            #print(s2)


    # for k in range(26, 101):
    # print(s2_2)
    # s2 = s2_1.union(s2_2)
    # print("set two = ", s2)
    # print(len(s2))

    # s2 = set(range(s, k))
    # print("set two = ", s2)

    return 0


if __name__ == "__main__":
    sys.exit(main())
