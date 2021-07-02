import itertools
import sys
import random


def main():
    l = random.choices(range(0, 101), k=100)
    print(l)
    print(len(l))
    new_l = list()
    # print(new_l)
    j = 0
    # cumulative sum
    for i in l:
        j += i
        new_l.append(j)
    print(new_l)
    print(len(new_l))
    # Adjoint pair sum
    new_l1 = [(l[k] + l[k + 1]) for k in range(0, len(l) - 1)]
    print(new_l1)





    # print(l1[1::1])

    # j1 = 0
    # l1_dict = dict(iter())
    # print(l1_dict)
    # j1 = 0
    # for k, v in l1_dict.items():
    #    j1 = j1 + k + v
    #    new_l1.append(j1)
    # print(j1)
    # for v in l1:
    # print(v)
    # j2 = j1 + v
    # print(j2)
    # print(k)
    # print(v)
    # j = j + k + v
    # new_l2.append(j2)
    # print(new_l1)
    # print(k[0])

    # l1.index()
    # new_l = l1
    # new_l[0] = l1.index(0)
    # new_l[1] = l1.index
    # for _
    # for new_l in l1:
    #    new_l = l1 + 1
    #    print(new_l)

    # print(l1)

    return 0


if __name__ == "__main__":
    sys.exit(main())
