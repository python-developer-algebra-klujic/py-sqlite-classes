# Svaki kolac ima: naziv, cijenu, tezinu (u gramima)

class Cake:
    # START
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight
    # END
    def __str__(self):
        return f'{self.name} {self.price} EUR {self.weight} g.'


class CakesRepo:
    def get_cakes(self):
        return [
            Cake('Dorina s keksima', 2.49, 80),
            Cake('Mikado rizna cokolada', 4.79, 150),
            Cake('Lindt w chilli', 3.59, 100),
            Cake('Ritter Dark', 2.99, 100),
            Cake('Linolada', 5.99, 100),
        ]
