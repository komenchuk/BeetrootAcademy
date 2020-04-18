class Flower:
    __curent_id = 0

    def __init__(self, name: str, price: float, quantity: int):
        Flower.__curent_id += 1
        self.id = Flower.__curent_id
        self.name = name
        self.price = price
        self.quantity = quantity

    """def motive(self, quantity: int):
        self.quantity = lambda x: not x % 2, quantity"""

    def add_quantity(self, quantity: int):
        self.quantity += quantity

    def remove_quantity(self, quantity: int):
        self.quantity = max(0, self.quantity - quantity)

    def __str__(self):
        return f'ID: {self.id}\tFlowers: {self.name}\tPrice: {self.price}\tQuantity: {self.quantity}'


class Store:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def add_flowers(self, flowers):
        self.flowers.extend(flowers)

    def remove_flower(self, flower_id):
        for flower in self.flowers:
            if flower.id == flower_id:
                self.flowers.remove(flower)
                break

    def print_assortment(self):
        for flower in self.flowers:
            print (flower)

    def get_total_value(self):
        sum = 0
        for flower in self.flowers:
            sum += flower.quantity * flower.price
        return sum

    """def get_motive(self):
        rip = 0
        happy = 0
        
        for flower in self.flowers:
            if flower.quantity % 2 != 0:
                rip += 1
                print('Соболезнуем..')
            else:
                happy += 1
                print('Пусть букет радует!')
            break"""


"""class Motive:
    def __init__(self, motive: str):
        self.id = Flower.__curent_id
        self.motive = motive

    def __str__(self):
        return f'ID: {self.id}\tMotive: {self.motive}'"""



f1 = Flower('Троянда', 30, 9)
f2 = Flower('Гвоздика', 15, 2)
f3 = Flower('Ромашка', 20, 21)

s = Store()

s.add_flower(f1)
s.add_flower(f2)
s.add_flower(f3)


s.print_assortment()

print(s.get_total_value())