# INITIAL_BONUS = 100
# INTERMEDIATE_BALANCE = 5000
# ADVANCED_BALANCE = 15000
#
# class Client:
#     bank_name = "Sberbank"
#     country = "Russia"
#
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance + INITIAL_BONUS
#
#         if self.balance < INTERMEDIATE_BALANCE:
#             self.level = "Basic"
#         elif self.balance < ADVANCED_BALANCE:
#             self.level = "Intermediate"
#         else:
#             self.level = "Advanced"
#
# John_Doe = Client("John Doe", 500)
# Jane_Defoe = Client("Jane Defoe", 150000)
#
# print(Jane_Defoe.country)
# Client.country = "Russian Federation"
# print(Jane_Defoe.country)
# John_Doe.country = 'Brit'
# print(John_Doe.country)
# import datetime
# from school21 import Calculator
#
#
# def test_init():
# 	c = Calculator()
# 	assert bool(c.history(1)) == False, "history не пуста"
# 	assert bool(c.last) == False, "last не пустое"
#
# def test_sum():
# 	c = Calculator()
# 	assert c.sum(1, 2) == 3, "сумма считается неверно"
# 	assert c.last == "sum(1, 2) == 3", "при сложении не записался last"
# 	assert c.history(1) == "sum(1, 2) == 3", "неправильная запись в history"
#
# def test_sub():
# 	c = Calculator()
# 	assert c.sub(1, 2) == -1, "разность считается неверно"
# 	assert c.last == "sub(1, 2) == -1", "при вычитании не записался last"
# 	assert c.history(1) == "sub(1, 2) == -1", "неправильная запись в history"
#
# def test_mul():
# 	c = Calculator()
# 	assert c.mul(3, 2) == 6, "произведение считается неверно"
# 	assert c.last == "mul(3, 2) == 6", "при произведении не записался last"
# 	assert c.history(1) == "mul(3, 2) == 6", "неправильная запись в history"
#
# def test_div():
# 	c = Calculator()
# 	assert c.div(3, 2) == 1.5, "деление считается неверно"
# 	assert c.last == "div(3, 2) == 1.5", "при делении не записался last"
# 	assert c.history(1) == "div(3, 2) == 1.5", "неправильная запись в history"
#
# def test_mod():
# 	c = Calculator()
# 	assert c.div(3, 2, True) == 1, "деление с остатком считается неверно"
# 	assert c.last == "div(3, 2) == 1", "при делении с остатком не записался last"
# 	assert c.history(1) == "div(3, 2) == 1", "неправильная запись в history"
#
# def test_history():
# 	c = Calculator()
# 	c1 = Calculator()
# 	c.sum(1, 2)
# 	assert c.last == "sum(1, 2) == 3", "при сложении не записался last"
# 	c1.sum(5, 5)
# 	assert c.history(1) == "sum(1, 2) == 3", f"неправильная запись в history: {c.history(1)}"
# 	c.sum(3, 4)
# 	assert c.last == "sum(3, 4) == 7", "при сложении не записался last"
# 	c1.sub(6, 3)
# 	assert c.history(2) == "sum(1, 2) == 3", f"неправильная запись в history(2): {c.history(2)}"
# 	assert c.history(1) == "sum(3, 4) == 7", f"неправильная запись в history(1): {c.history(1)}"
# 	c.sub(5, 5)
# 	assert c.last == "sub(5, 5) == 0", "не записался last"
# 	c1.mul(543, 55)
# 	assert c.history(3) == "sum(1, 2) == 3", f"неправильная запись в history(3): {c.history(3)}"
# 	assert c.history(2) == "sum(3, 4) == 7", f"неправильная запись в history(2): {c.history(2)}"
# 	assert c.history(1) == "sub(5, 5) == 0", f"неправильная запись в history(1): {c.history(1)}"
# 	c.mul(-1, 6)
# 	assert c.last == "mul(-1, 6) == -6", "не записался last"
# 	c1.div(54, 3)
# 	assert c.history(4) == "sum(1, 2) == 3", f"неправильная запись в history(4): {c.history(4)}"
# 	assert c.history(3) == "sum(3, 4) == 7", f"неправильная запись в history(3): {c.history(3)}"
# 	assert c.history(2) == "sub(5, 5) == 0", f"неправильная запись в history(2): {c.history(2)}"
# 	assert c.history(1) == "mul(-1, 6) == -6", f"неправильная запись в history(1): {c.history(1)}"
#
# def test_last():
# 	c1 = Calculator()
# 	c2 = Calculator()
# 	c1.sum(1, 2)
# 	assert c1.last == "sum(1, 2) == 3", "при сложении не записался last"
# 	assert c2.last == "sum(1, 2) == 3", "при сложении не записался last"
# 	assert c1.last is c2.last, "last не ссылается на один и тот же объект"
# 	c2.mul(35, 100)
# 	assert c1.last == "mul(35, 100) == 3500", "при вычитании не записался last"
# 	assert c2.last == "mul(35, 100) == 3500", "при вычитании не записался last"
# 	assert c1.last is c2.last, "last не ссылается на один и тот же объект"
# 	assert c1.history(1) != c2.history(1), "history разных калькуляторов совпадают"
# 	c1.clear()
# 	assert c1.last is None, "clear не задает значение None в last"
# 	assert c2.last is None, "clear не задает значение None в last"
# 	assert c1.last is c2.last, "last не ссылается на один и тот же объект"
#
#
# test_init()
# test_sum()
# test_sub()
# test_mul()
# test_div()
# test_mod()
# test_history()
# test_last()

# from datetime import *
#
# a = datetime(2022, 12, 15, 14)
# b = datetime(2022, 12, 15, 16)
# diff = b - a
# diff = diff.total_seconds()/60
# print(diff)
# print(type(diff))

# class Meal:
#     def __init__(self, title, price):
#         self.title = title
#         self.price = price
#
#     def __str__(self):
#         return ': '.join([self.title, str(self.price)])
#
#     def __repr__(self):
#         """Функция, которая используется для текстового представления объекта в случаях, когда это происходит не
#         через функцию str(obj)"""
#         return str(self)
#
#     def __add__(self, other):
#         """Функция, которая описывает прибавление к нашему объекту объекта other"""
#         # если у нас оба объекта данного класса, сложим их атрибуты
#         if isinstance(other, Meal):
#             new_title = ', '.join([self.title, other.title])
#             new_price = self.price + other.price
#         else:
#             # а если второй объект не этого класса, то попробуем его привести к типу float
#             new_title = self.title + " и что-то еще"
#             new_price = self.price + float(other)
#         return Meal(new_title, new_price)
#
#
# Meal.__radd__ = Meal.__add__
#
#
# def our_call_method(self):
#     self.title = "Ты всё съел!"
#     self.price = -self.price
#     print(self)
#
# Meal.__call__ = our_call_method
#
# m = Meal("Борщ", 150)
# print(m)
# m()

# def create_car(color, consumption, tank_volume, mileage=0):
#     return {
#         "color": color,
#         "consumption": consumption,
#         "tank_volume": tank_volume,
#         "reserve": tank_volume,
#         "mileage": mileage,
#         "engine_on": False
#     }
#
#
# def start_engine(car):
#     if not car["engine_on"] and car["reserve"] > 0:
#         car["engine_on"] = True
#         return "Двигатель запущен."
#     return "Двигатель уже был запущен."
#
#
# def stop_engine(car):
#     if car["engine_on"]:
#         car["engine_on"] = False
#         return "Двигатель остановлен."
#     return "Двигатель уже был остановлен."
#
#
# def drive(car, distance):
#     if not car["engine_on"]:
#         return "Двигатель не запущен."
#     if car["reserve"] / car["consumption"] * 100 < distance:
#         return "Малый запас топлива."
#     car["mileage"] += distance
#     car["reserve"] -= distance / 100 * car["consumption"]
#     return f"Проехали {distance} км. Остаток топлива: {car['reserve']} л."
#
#
# def refuel(car):
#     car["reserve"] = car["tank_volume"]
#
#
# def get_mileage(car):
#     return f"Пробег {car['mileage']} км."
#
#
# def get_reserve(car):
#     return f"Запас топлива {car['reserve']} л."
#
#
# car_1 = create_car(color="black", consumption=10, tank_volume=55)
#
# print(start_engine(car_1))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 100))
# print(drive(car_1, 300))
# print(get_mileage(car_1))
# print(get_reserve(car_1))
# print(stop_engine(car_1))
# print(drive(car_1, 100))

# class Car:
#
#     def __init__(self, color, consumption, tank_volume, mileage=0):
#         self.color = color
#         self.consumption = consumption
#         self.tank_volume = tank_volume
#         self.reserve = tank_volume
#         self.mileage = mileage
#         self.engine_on = False
#
#     def start_engine(self):
#         if not self.engine_on and self.reserve > 0:
#             self.engine_on = True
#             return "Двигатель запущен."
#         return "Двигатель уже был запущен."
#
#     def stop_engine(self):
#         if self.engine_on:
#             self.engine_on = False
#             return "Двигатель остановлен."
#         return "Двигатель уже был остановлен."
#
#     def drive(self, distance):
#         if not self.engine_on:
#             return "Двигатель не запущен."
#         if self.reserve / self.consumption * 100 < distance:
#             return "Малый запас топлива."
#         self.mileage += distance
#         self.reserve -= distance / 100 * self.consumption
#         return f"Проехали {distance} км. Остаток топлива: {self.reserve} л."
#
#     def refuel(self):
#         self.reserve = self.tank_volume
#
#     def get_mileage(self):
#         return self.mileage
#
#     def get_reserve(self):
#         return self.reserve
#
#
# car_1 = Car(color="black", consumption=10, tank_volume=55)
# car_1.mileage = 1000
# print(f"Пробег {car_1.get_mileage()} км.")
# print(f"Запас топлива {car_1.get_reserve()} л.")

# print(car_1.start_engine())
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(100))
# print(car_1.drive(300))
# print(f"Пробег {car_1.get_mileage()} км.")
# print(f"Запас топлива {car_1.get_reserve()} л.")
# print(car_1.stop_engine())
# print(car_1.drive(100))


# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, a, b):
#         self.x += a
#         self.y += b
#
#     def length(self, other):
#         z = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
#         z = round(z, 2)
#         return z
#
# first_point = Point(2, -7)
# second_point = Point(7, 9)
# print(first_point.length(second_point))
# print(second_point.length(first_point))

# class RedButton():
#     press_count = 0
#
#     def click(self):
#         self.press_count += 1
#         print('Тревога!')
#
#     def count(self):
#         return self.press_count
#
# first_button = RedButton()
# second_button = RedButton()
# for time in range(5):
#     if time % 2 == 0:
#         second_button.click()
#     else:
#         first_button.click()
# print(first_button.count(), second_button.count())


# class Programmer():
#     def __init__(self, name, position, hours=0):
#         self.name = name
#         self.position = position
#         self.hours = hours
#         self.acc_salary = 0
#
#     def work(self, time):
#         d = {
#             'Junior': 10,
#             'Middle': 15,
#             'Senior': 20,
#             1: 21
#         }
#         self.hours += time
#         self.acc_salary += time * d[self.position]
#
#     def rise(self):
#         if self.position == 'Junior':
#             self.position = 'Middle'
#         elif self.position == 'Middle':
#             self.position = 'Senior'
#         elif self.position == 'Senior':
#             self.position = 1
#         else:
#             self.position += 1
#
#     def info(self):
#         return f'{self.name} {self.hours}ч. {self.acc_salary}тгр.'
#
#
# programmer = Programmer('Васильев Иван', 'Junior')
# programmer.work(750)
# print(programmer.info())
# programmer.rise()
# programmer.work(500)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())
# programmer.rise()
# programmer.work(250)
# print(programmer.info())


# class Rectangle:
#     def __init__(self, xy, ab):
#         self.x, self.y = xy
#         self.a, self.b = ab
#
#     def perimeter(self):
#         p = 2 * abs(self.a - self.x) + 2 * abs(self.b - self.y)
#         return round(p, 2)
#
#     def area(self):
#         sq = abs(self.a - self.x) * abs(self.b - self.y)
#         return round(sq, 2)
#
#     def get_pos(self):
#         if self.a > self.x:
#             p1 = self.x
#         else:
#             p1 = self.a
#         if self.b < self.y:
#             p2 = self.y
#         else:
#             p2 = self.b
#         return round(p1, 2), round(p2, 2)
#
#     def get_size(self):
#         return round(abs(self.a - self.x), 2), round(abs(self.b - self.y), 2)
#
#     def move(self, dx, dy):
#         self.a += dx
#         self.x += dx
#         self.b += dy
#         self.y += dy
#
#     def resize(self, width, height):
#         if self.a > self.x:
#             self.a = self.x + width
#         else:
#             self.x = self.a + width
#         if self.b < self.y:
#             self.b = self.y - height
#         else:
#             self.y = self.b - height
#
#     def turn(self):
#         px, py = self.get_pos()
#         lx, ly = self.get_size()
#         cx = px + lx / 2
#         cy = py - ly / 2
#         self.x = cx - ly / 2
#         self.y = cy + lx / 2
#         self.a = cx + ly / 2
#         self.b = cy - lx / 2
#
#     def scale(self, factor):
#         px, py = self.get_pos()
#         lx, ly = self.get_size()
#         cx = px + lx / 2
#         cy = py - ly / 2
#         self.x = cx - (lx / 2) * factor
#         self.y = cy + (ly / 2) * factor
#         self.a = cx + (lx / 2) * factor
#         self.b = cy - (ly / 2) * factor
#
# rect = Rectangle((3, 3), (9, 7))
# print(rect.get_pos(), rect.get_size())
# print(rect.turn())
#
# rect = Rectangle((-3.14, 2.71), (3.14, -2.71))
# print(rect.get_pos(), rect.get_size())
# rect.scale(2.0)
# print(rect.get_pos(), rect.get_size())

# class Checkers:
#     def __init__(self):
#         # self.d = {}
#         # for q in '87654321':
#         #     for p in 'ABCDEFGH':
#         #         if q in ('68') and p in 'BDFH':
#         #             self.d[p + q] = self.d.setdefault(p + q, 'B')
#         #         elif q in ('7') and p in 'ACEG':
#         #             self.d[p + q] = self.d.setdefault(p + q, 'B')
#         #         elif q in ('13') and p in 'ACEG':
#         #             self.d[p + q] = self.d.setdefault(p + q, 'W')
#         #         elif q in ('2') and p in 'BDFH':
#         #             self.d[p + q] = self.d.setdefault(p + q, 'W')
#         #         else:
#         #             self.d[p + q] = self.d.setdefault(p + q, '*')
#         self.d = [[p + q for p in 'ABCDEFGH'] for q in '87654321']
#
#     def get_cell(self, p):
#         return self.d[p]
#
#     def move(self, f, t):
#         print(self.d[f], self.d[t])
#         self.d[t] = self.d[f]
#         self.d[f] = '*'
#
#
# class Cell:
#     def __init__(self):
#         pass
#
#     def status(self):
#         pass
#
# # checkers = Checkers()
# # for row in '87654321':
# #     for col in 'ABCDEFGH':
# #         print(checkers.get_cell(col + row), end='')
# #     print()
#
#
# # d = {}
# # for q in '12345678':
# #     for p in 'ABCDEFGH':
# #         if q in ('13') and p in 'BDFH':
# #             d[p + q] = d.setdefault(p + q, 'B')
# #         elif q in ('2') and p in 'ACEG':
# #             d[p + q] = d.setdefault(p + q, 'B')
# #         elif q in ('68') and p in 'ACEG':
# #             d[p + q] = d.setdefault(p + q, 'W')
# #         elif q in ('7') and p in 'BDFH':
# #             d[p + q] = d.setdefault(p + q, 'W')
# #         else:
# #             d[p + q] = d.setdefault(p + q, '*')
# #
# # for q in '12345678':
# #     for p in 'ABCDEFGH':
# #         print(d[p + q], end='')
# #     print()
#
# # for q in '87654321':
# #     for p in 'ABCDEFGH':
# #         if q in ('68') and p in 'BDFH':
# #             self.d[p + q] = self.d.setdefault(p + q, 'B')
# #         elif q in ('7') and p in 'ACEG':
# #             self.d[p + q] = self.d.setdefault(p + q, 'B')
# #         elif q in ('13') and p in 'ACEG':
# #             self.d[p + q] = self.d.setdefault(p + q, 'W')
# #         elif q in ('2') and p in 'BDFH':
# #             self.d[p + q] = self.d.setdefault(p + q, 'W')
# #         else:
# #             self.d[p + q] = self.d.setdefault(p + q, '*')

# class Queue:
#     def __init__(self):
#         self.q = []
#
#     def push(self, item):
#         self.q.append(item)
#
#     def pop(self):
#         return self.q.pop(0)
#
#     def is_empty(self):
#         return len(self.q) == 0
#
# queue = Queue()
# for item in ("Hello,", "world!"):
#     queue.push(item)
# while not queue.is_empty():
#     print(queue.pop())

# class Stack:
#     def __init__(self):
#         self.q = []
#
#     def push(self, item):
#         self.q.append(item)
#
#     def pop(self):
#         return self.q.pop(-1)
#
#     def is_empty(self):
#         return len(self.q) == 0
#
# stack = Stack()
# for item in ("Hello,", "world!"):
#     stack.push(item)
# while not stack.is_empty():
#     print(stack.pop())

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, a, b):
#         self.x += a
#         self.y += b
#
#     def length(self, other):
#         z = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
#         z = round(z, 2)
#         return z
#
#
# class PatchedPoint(Point):
#     def __init__(self, x=0, y=0):
#         super().__init__(x=x, y=y)
#         if isinstance(x, tuple):
#             self.x, self.y = x
#         else:
#             self.x = x
#             self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#     def __repr__(self):
#         return f'PatchedPoint({self.x}, {self.y})'
#
#     def __add__(self, other):
#         x, y = other
#         x = self.x + x
#         y = self.y + y
#         return PatchedPoint(x, y)
#
#     def __iadd__(self, other):
#         a, b = other
#         self.x = self.x + a
#         self.y = self.y + b
#         return self
#
# first_point = second_point = PatchedPoint((2, -7))
# first_point += (7, 3)
# print(first_point, second_point, first_point is second_point)

class Fraction:
    def __init__(self, n, d=None):
        if d is None:
            n, d = n.split('/')
        n, d = int(n), int(d)
        gcd = self._gcd(n, d)
        self.num = n // gcd
        self.denom = d // gcd

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def __repr__(self):
        return f'Fraction(\'{self.__str__()}\')'

    def __str__(self):
        if self.num == 0:
            return '0'
        elif self.denom == self.num:
            return '1'
        return f'{self.num}/{self.denom}'

    def numerator(self, new_num=None):
        if new_num is not None:
            gcd = self._gcd(new_num, self.denom)
            self.num = new_num // gcd
            self.denom = self.denom // gcd
        else:
            return self.num

    def denominator(self, new_denom=None):
        if new_denom is not None:
            gcd = self._gcd(self.num, new_denom)
            self.num = self.num // gcd
            self.denom = new_denom // gcd
        else:
            return self.denom

    def __neg__(self):
        return Fraction(-self.num, self.denom)

    def __add__(self, other):
        num = self.num * other.denom + other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __iadd__(self, other):
        self.num = self.num * other.denom + other.num * self.denom
        self.denom = self.denom * other.denom
        return self

    def __sub__(self, other):
        num = self.num * other.denom - other.num * self.denom
        denom = self.denom * other.denom
        return Fraction(num, denom)

    def __isub__(self, other):
        self.num = self.num * other.denom - other.num * self.denom
        self.denom = self.denom * other.denom
        return self


a = Fraction(1, 3)
c = b = Fraction(1, 2)
b -= a
print(a, b, c, b is c)
















