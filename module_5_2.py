class House:
    houses_history = []
    
    def __new__(cls, ):
        pass
    
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other
        else:
            return False

    def __lt__(self, other):
        return self.number_of_floors < self.other

    def __le__(self, other):
        return self.number_of_floors <= self.other

    def __gt__(self, other):
        return self.number_of_floors > self.other

    def __ge__(self, other):
        return self.number_of_floors >= self.other

    def __ne__(self, other):
        return self.number_of_floors != self.other

    def __add__(self, value):
        return self.number_of_floors + value

    def __radd__(self, value):
        return self.number_of_floors + value

    def __iadd__(self, value):
        return self.number_of_floors + value

    def __del__(self):
       return f'{self.name} снесён, но он останется в истории ' 



h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
