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

    # catalogue = {'iphone': {'X': 800}}
    # print(catalogue)
    for product, models in catalogue.items():
        print(product)
        print('-' * 25)
        for model, price in models.items():
            print(f"{model}: £{price}")
        print('=' * 25)

    # for product, models in catalogue.items():
    #    for model, price in models.items():
    #        usr_model = input("What model do you want?")
    #      try:
    #          assert usr_model == models.a
    #          print(models.get(usr_model, None))
    #      except AssertionError:
    #          print("Select model from given catalogue only", file=sys.stderr)
    # print(catalogue.keys())
    usr_prod = str(input("Select a product: "))
    if usr_prod in catalogue.keys():
        print("Product categories:", catalogue[usr_prod])
    else:
        print("Select product from given catalogue only")
    usr_model = input("Select a model: ")
    usr_quant = int(input("Select a quantity: "))

    if usr_model in catalogue.get(usr_prod, None):
        print("Final Invoice")
        print("Model name:", usr_model)
        print(f"Price of selected model: £{catalogue[usr_prod][usr_model]}")
        print("Quantity:", usr_quant)
        print(f"Total price = £{usr_quant * catalogue[usr_prod][usr_model]}")
    else:
        print("Select model from selected product category only")

    # try:
    #   assert usr_prod == catalogue.keys()

    # except AssertionError:
    #   print("Select product from given catalogue only", file=sys.stderr)
    #  return os.X_OK

    # return os.X_OK

    # if usr_model == model:
    #   print(usr_model)
    # else:
    #   print("Select model from given catalogue only")
    # try:
    #   assert usr_prod == product in catalogue.items()
    # print(model)
    # except AssertionError:
    #  print("Give product from given catalogue only", file=sys.stderr)
    #   return os.X_OK

    return 0


if __name__ == "__main__":
    sys.exit(main())
