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


#     def is_faster_than(self, other):
#         pass

# class Car(Transport):

#     def __init__(self,fuel_type):
#         self.fuel = fuel_type
#         self.capacity = 0

#     def move(self):
#         return "Car is moving"

#     def fuel_type(self):
#         return self.fuel

#     def max_speed(self):
#         return 200
    
#     def description(self):
#         return f"This transport is car . Use{self.fuel_type()} Speed {self.max_speed} km/h"
    
#     def set_capacity(self, n):
#         self.capacity = n




# class Airplane(Transport):

#     def move(self):
#         return "Airplan is moving"

#     def fuel_type(self):
#         return "Carasin"

#     def max_speed(self):
#         return 720
    
#     def description(self):
#         return f"This transport is airplane . Use{self.fuel_type()} Speed {self.max_speed} km/h"


# class Ship(Transport):

#     def move(self):
#         return "Ship is moving"

#     def fuel_type(self):
#         return "Kumur"

#     def max_speed(self):
#         return 100
    
#     def description(self):
#         return f"This transport is ship . Use{self.fuel_type()} Speed {self.max_speed} km/h"

# class Train(Transport):

#     def move(self):
#         return "Train is moving"

#     def fuel_type(self):
#         return "Kumur"

#     def max_speed(self):
#         return 100
    
#     def description(self):
#         return f"This transport is train . Use{self.fuel_type()} Speed {self.max_speed} km/h"
    
#     def is_faster_than(self, other):
#         return other.max_speed() < self.max_speed


# class Bicycle(Transport):

#     def move(self):
#         return "Bicycle is moving"

#     def fuel_type(self):
#         return "People engine"

#     def max_speed(self):
#         return 20
        
#     def description(self):
#         return f"This transport is biycycle . Use{self.fuel_type()} Speed {self.max_speed} km/h"


# def race(transport_list: list[int]):
#     return max(list(i.max_speed() for i in transport_list))


# car = Car("electronic")
# airplane = Airplane()
# ship = Ship()
# train = Train()

# lst = [car,airplane,ship,train]

# car.set_capacity(5)
# print(car.capacity)
