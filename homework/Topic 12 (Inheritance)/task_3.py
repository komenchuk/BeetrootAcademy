"""Product Store

Write a class Product that has three attributes:

    type
    name
    price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

    add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name). The discount must be specified in percentage
    sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. It also increments income if the sell_product method succeeds.
    get_income() - returns amount of many earned by ProductStore instance.
    get_all_products() - returns information about all available products in the store.
    get_product_info(product_name) - returns a tuple with product name and amount of items in the store.
"""


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


def except_decoretor(func):
    def wrapper(self, *args):
        try:
            return func(self, *args)
        except TypeError as alert:
            print(alert)

    return wrapper


class ProductStore:
    def __init__(self):
        self.store = []
        self.money = 0

    @except_decoretor
    def add(self, product, amount):
        self.store.append(
            {
                'type': product.type,
                'name': product.name,
                'price': product.price + (product.price * 0.3),
                'amount': amount
            }
        )

    def description(self, item):
        string = f"type: {item['type']}, name: {item['name']}, price: {item['price']}, amount: {item['amount']}\n"
        return string

    @except_decoretor
    def set_discount(self, identifier, percent, identifier_type='name'):
        for item in self.store:
            if item[identifier_type] == identifier:
                item['price'] = round((item['price'] - item['price'] * percent * 0.01), 2)

    @except_decoretor
    def sell_product(self, product_name, amount):
        for item in self.store:
            if product_name == item['name'] and item['amount'] >= amount:
                self.money += amount * item['price']
                item['amount'] -= amount
                break
        else:
            print(f'{product_name} - not in the store!')

    @except_decoretor
    def get_income(self):
        return self.money

    @except_decoretor
    def get_all_products(self):
        return "".join(map(self.description, self.store))

    @except_decoretor
    def get_product_info(self, product_name):
        products = list(filter(lambda x: x['name'] == product_name, self.store))[0]
        dict = (products['name'], products['amount'])
        return dict

    @except_decoretor
    def search_product(self, prod):
        product = list(filter(lambda x: x['name'] == prod, self.store))[0]
        return product


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)
assert s.get_product_info('Ramen') == ('Ramen', 290)
