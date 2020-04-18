class FLowers:
    all_flowers = 0

    def __init__(self, name: str, price: float, color: str, volume: str):
        self.name = name
        self.price = price
        self.color = color
        self.volume = volume
        self.flowers = []

    def __repr__(self):
        return f'Flowers ('
        {self.price}, {self.color}, {self.volume}
        ').'

    def __str__(self):
        return f'Flowers {self.name} are worth it {self.price}, they are {self.color} in {self.volume} volume.'


class Birthday(FLowers):

    def __init__(self, name, price, color, volume, quantity):
        super().__init__(name, price, color, volume)
        self.quantity = quantity
        self.birthday_flowers = []

    def new_bouquet(self, name, price, color, volume, quantity):
        self.birthday_flowers.append(FLowers(name, price, color, volume, quantity))

    def __repr__(self):
        return f'Birthday bouquet('
        {self.name}
        ').'

    def __str__(self):
        list_of_flowers = '\n'.join(map(lambda x: f'{x.name}, {x.price}, {x.color}, {x.volume}, {x.quantity}'))
        return list_of_flowers


class Kosyak(FLowers):

    def __init__(self, name, price, color, volume, quantity):
        super().__init__(name, price, color, volume)
        self.quantity = quantity
        self.kosyak_flowers = []

    def new_bouquet(self, name, price, color, volume, quantity):
        self.kosyak_flowers.append(FLowers(name, price, color, volume, quantity))

    def __repr__(self):
        return f'Kosyak bouquet('
        {self.name}
        ').'

    def __str__(self):
        list_of_flowers = '\n'.join(map(lambda x: f'{x.name}, {x.price}, {x.color}, {x.volume}, {x.quantity}'))
        return list_of_flowers


class Simple(FLowers):

    def __init__(self, name, price, color, volume, quantity):
        super().__init__(name, price, color, volume)
        self.quantity = quantity
        self.simple_flowers = []

    def new_bouquet(self, name, price, color, volume, quantity):
        self.simple_flowers.append(FLowers(name, price, color, volume, quantity))

    def __repr__(self):
        return f'Simple bouquet('
        {self.name}
        ').'

    def __str__(self):
        list_of_flowers = '\n'.join(map(lambda x: f'{x.name}, {x.price}, {x.color}, {x.volume}, {x.quantity}'))
        return list_of_flowers


class Funeral(FLowers):

    def __init__(self, name, price, color, volume, quantity):
        super().__init__(name, price, color, volume)
        self.quantity = quantity
        self.funeral_flowers = []

    def new_bouquet(self, name, price, color, volume, quantity):
        self.funeral_flowers.append(FLowers(name, price, color, volume, quantity))

    def __repr__(self):
        return f'Funeral bouquet('
        {self.name}
        ').'

    def __str__(self):
        list_of_flowers = '\n'.join(map(lambda x: f'{x.name}, {x.price}, {x.color}, {x.volume}, {x.quantity}'))
        return list_of_flowers
