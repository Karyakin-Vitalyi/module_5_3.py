# Домашняя работа по уроку "Перегрузка операторов"

class House:
    def __init__(self, name, number_of_floors):
        # Инициализация атрибутов объекта
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверка, существует ли указанное количество этажей
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Вывод этажей от 1 до new_floor включительно
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращает количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращает строку с названием и количеством этажей
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return False

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return False

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return False

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return False

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        raise ValueError("Value must be an integer")

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# Пример использования класса
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Пример использования метода __str__
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 20

# Пример использования метода __eq__
print(h1 == h2)  # False

h1 = h1 + 10  # __add__
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # __iadd__
print(h1)  # Ожидаемый вывод: Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # __radd__
print(h2)  # Ожидаемый вывод: Название: ЖК Акация, кол-во этажей: 30

# Пример сравнения
print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __it__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__


