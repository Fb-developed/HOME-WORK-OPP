from abc import ABC, abstractmethod


# 1. Create an abstract class PaymentMethod with:
# An abstract method pay(amount)

# An abstract method validate_payment()

# 2. Create a class CreditCard that:
# Implements pay() by printing: Paid {amount} using Credit Card

# Implements validate_payment() by printing: Validating Credit Card

# 3. Create a class PayPal that:
# Implements pay() by printing: Paid {amount} using PayPal

# Implements validate_payment() by printing: Validating PayPal account

# 4. Create instances of both classes and call their methods.


# class PaymentMethod(ABC):


#     @abstractmethod
#     def pay(self,amount):
#         pass



#     @abstractmethod
#     def validate_payment(self):
#         pass



# class CreditCard(PaymentMethod):

#     def pay(self,amount):
#         return f"Paid {amount} using Credit Card"
    

#     def validate_payment(self):
#         return 'Validating Credit Card'
    

# class PayPal(PaymentMethod):

#     def pay(self,amount):
#         return f'Paid {amount} using PayPal'
    
    
#     def validate_payment(self):
#         return 'Validating PayPal account'
    
# credit = CreditCard()
# pal = PayPal()

# print(credit.validate_payment())
# print(credit.pay(100))
# print(pal.validate_payment())
# print(pal.pay(50))







# class Transport(ABC):

#     @abstractmethod
#     def move(self):
#         pass

#     @abstractmethod
#     def fuel_type(self):
#         pass

#     @abstractmethod
#     def max_speed(self):
#         pass

#     @abstractmethod
#     def description(self):
#         pass

#     @abstractmethod
#     def capacity(self):
#         pass

#     def is_faster_than(self, other):
#         if self.max_speed() > other.max_speed():
#             return f"{self.__class__.__name__} быстрее чем {other.__class__.__name__}"
#         elif self.max_speed() < other.max_speed():
#             return f"{self.__class__.__name__} медленнее чем {other.__class__.__name__}"
#         else:
#             return f"{self.__class__.__name__} и {other.__class__.__name__} одинаковы по скорости"


# class Car(Transport):
#     def __init__(self, fuel="бензин"):
#         self._fuel = fuel

#     def move(self):
#         return "Машина едет по дороге"

#     def fuel_type(self):
#         return self._fuel

#     def max_speed(self):
#         return 200 if self._fuel == "бензин" else 180

#     def description(self):
#         return f"Транспорт: Машина топливо: {self.fuel_type()}, макс. скорость: {self.max_speed()} км/ч"

#     def capacity(self):
#         return 5


# class Airplane(Transport):
#     def move(self):
#         return "Самолёт летит в небе"

#     def fuel_type(self):
#         return "керосин"

#     def max_speed(self):
#         return 900

#     def description(self):
#         return f"Транспорт: Самолёт топливо: {self.fuel_type()} макс. скорость: {self.max_speed()} км/ч"

#     def capacity(self):
#         return 180


# class Ship(Transport):
#     def move(self):
#         return "Корабль плывёт по воде"

#     def fuel_type(self):
#         return "дизель"

#     def max_speed(self):
#         return 60

#     def description(self):
#         return f"Транспорт: Корабль топливо: {self.fuel_type()} макс. скорость: {self.max_speed()} км/ч"

#     def capacity(self):
#         return 1000


# class Train(Transport):
#     def move(self):
#         return "Поезд движется по рельсам"

#     def fuel_type(self):
#         return "электричество"

#     def max_speed(self):
#         return 250

#     def description(self):
#         return f"Транспорт: Поезд, топливо: {self.fuel_type()}, макс. скорость: {self.max_speed()} км/ч"

#     def capacity(self):
#         return 600


# class Bicycle(Transport):
#     def move(self):
#         return "Велосипед едет с помощью педалей"

#     def fuel_type(self):
#         return "человеческая сила"

#     def max_speed(self):
#         return 30

#     def description(self):
#         return f"Транспорт: Велосипед, топливо: {self.fuel_type()}, макс. скорость: {self.max_speed()} км/ч"

#     def capacity(self):
#         return 1


# def race(transports):
#     fastest = max(transports, key=lambda t: t.max_speed())
#     print(f" Самый быстрый транспорт — {fastest.__class__.__name__} со скоростью {fastest.max_speed()} км/ч!")



# car = Car("electro")
# airplane = Airplane()
# ship = Ship()
# train = Train()
# bike = Bicycle()

# all_transports = [car, airplane, ship, train, bike]

# for t in all_transports:
#     print(t.description())
#     print("vmestimost:", t.capacity())
#     print("kak dvisatsa:", t.move())
#     print("*" * 50)

# print(car.is_faster_than(train))
# print(ship.is_faster_than(bike))

# race(all_transports)
