import sys


def main():
    # use the steps in the range function
    one = set(range(2, 101, 1))
    print(f"one = {one}")
    two = set(range(4, 101, 2))
    print(f"two = {two}")
    three = set(range(6, 101, 3))
    print(f"three = {three}")
    five = set(range(10, 101, 5))
    print(f"five = {five}")
    seven = set(range(14, 101, 7))
    print(f"seven = {seven}")
    one_diff_two = one.difference(two)
    print(f"one - two = {one_diff_two}")
    #for d1 in one.difference(two):
    #    set_d1 = set(d1)
    #    print(set_d1)
    two_diff_three = one_diff_two.difference(three)
    print(f"one - two - three = {two_diff_three}")
    three_diff_five = two_diff_three.difference(five)
    print(f"one - two - three - five = {three_diff_five}")
    final_diff = three_diff_five.difference(seven)
    print(f"one - two - three - five - seven = {final_diff}")
    sort_diff = sorted(final_diff)
    print(sort_diff)
    # you can do this!
    # ...
    #s2 = {}
    # for s in range(4, 26):
    #s2_1 = set(range(4, 49))  # use step
    #s2_2 = set(range(49, 101))  # use step
    # fixme: no need for for loops in this problem; only set arithmetic
    #for s in s2_1:
    #    for k in s2_2:
    #        s2 = s2_1.union(s2_2)
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
