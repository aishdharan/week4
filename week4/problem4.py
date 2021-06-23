import sys


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
    usr_ask = input("What do you want to buy?")
    if usr_ask in catalogue.keys():
        #usr_ask = catalogue.values()
        print(catalogue.get(usr_ask, None))
    else:
        print("Please specify product mentioned in catalogue")
    # want to do something that'll make sure user only inputs the products :/
    #usr_quant = int(input("How many do you want to buy?"))
    #for _ in catalogue:

    return 0


if __name__ == "__main__":
    sys.exit(main())
