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

    shopping_cart = dict()
    for product, models in catalogue.items():
        prod_response = input(f"What product do you want? {product} [y/n]")
        # print(prod_response)
        if prod_response == 'y':
            for model, price in models.items():
                model_response = input(f"Which model do you want? {model} [y/n]")
                if model_response == 'y':
                    print(f"Price of selected model: £{price}")
                    model_quant = int(input("How many do you want?"))
                    shopping_cart[(product, model)] = model_quant
    print(shopping_cart)
    invoice = {}
    for product, model in shopping_cart:
        invoice[(product, model)] = shopping_cart[(product, model)] * catalogue[product][model]
    print(invoice)
    # print(invoice.values())
    print(f"Total price: £{sum(invoice.values())}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
