products = {
    'beer': 3.5,
    'water': 2,
    'fanta': 3.5,
    'vodka': 50,
    'chocolate': 5
}

while True:
    for name, price in products.items():
        print(name, '\t\t', price)
    product = input('Choose a product: ')
    if product not in products:
        print('There\'s not suach a product in the shop')
    else:
        price = products[product]
        amount = int(input('How many? '))
        payment = amount * price

        print(f'Pay {payment} złoty')


