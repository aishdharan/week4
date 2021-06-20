import sys


def main():
    s1 = set(range(2, 101))
    print("set one = ", s1)
    s2 = {}
    # for s in range(4, 26):
    s2_1 = set(range(4, 49))
    s2_2 = set(range(49, 101))
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
