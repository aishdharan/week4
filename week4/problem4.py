import sys

"""
Notes:
- In my experience, I sense you are currently at an important juncture in your
learning: you are reaching the limits of your mental memory. This is evident 
because your code is hard to follow meaning that you are trying to juggle
everything in your head, and that is very hard. In fact, it is also
very stressful and can interfere with your joy of learning. I propose following
two steps below (write these down and try them out for every problem):

1. substitute the original problem with a far, far simpler one
instead of making a big dictionary start with the most most basic
d1 = {'a': 1} and d2 = {'a': 1}

2. solve the problem in (1) *on paper* first; do not write any code until
you have a good grasp of the moving parts; the key question you should 
ask is "how do I gradually transform the inputs into the desired outputs?";
then make it slightly more difficult then repeat until you have 
something like the real one e.g. 
d1 = {'a': 1, 'b': 2} and d2 = {'b': 5, 'z': 10}

This is the skill of abstraction, the ability to simplify an actual 
problem into the essential steps required to solve it. 
It is at the heart of programming. For some people it comes far 
easier than for others but I think of it like learning to ride a bicycle: 
no one can tell you exactly how but once you know how you just know.
"""


def main():
    catalogue = {
        'iphone': {
            'X': 800,
            'XR': 900,
            '11': 1000,
            '12': 1200,
        },
        'ipad': {
            'mini': 400,
            'air': 500,
            'pro': 800,
        },
        'mac': {
            'macbook air': 999,
            'macbook': 1299,
            'macbook pro': 1799,
        }
    }

    print("Apple Catalogue", catalogue)

    # if usr_ask_prod in catalogue.keys():
    # usr_ask = catalogue.values()
    #   print(catalogue.get(usr_ask_prod, None))
    # else:
    #   print("Please specify product mentioned in catalogue")

    for usr_ask_prod, prod_category in catalogue.items():
        usr_ask_prod = input("What product do you want to buy?")
        print("Product", usr_ask_prod)
        # for value in prod_category:
        # print(value + ':', prod_category[value])
        # print(prod_category[key])
        # print(key + ':', prod_category[key])
    # print(prod_category)
    # for usr_ask_prod in prod_category:
    #   print(usr_ask_prod + ':', prod_category[usr_ask_prod])

    # for value in prod_category:
    #   select_cat = input("Select product category: ")
    #  if select_cat == key:
    #     print(key + ':', prod_category[value])
    # else:
    #   print("Please choose from the product category. ")

    # print(prod_category[value])
    # for select_cat in prod_category:
    # select_cat = input("Select product category: ")
    # print(select_cat + ':', prod_category[value])
    # for select_cat in value:
    # select_cat = input("Select product category: ")
    # print(select_cat + ':', prod_category[value])
    # print(value)

    # usr_quant = int(input("How many do you want to buy?"))

    # want to do something that'll make sure user only inputs the products :/
    # usr_quant = int(input("How many do you want to buy?"))
    # for _ in catalogue:

    return 0


if __name__ == "__main__":
    sys.exit(main())
