# class Animal():

#     def make_sound(self):
#         pass


# class Dog(Animal):

#     def make_sound(self):
#         return "Woof!"
    

# class Cat(Animal):

#     def make_sound(self):
#         return "Meow!"
    

# class Cow(Animal):

#     def make_sound(self):
#         return "Moo!"
    
# animals = []
# dog = Dog()
# cat = Cat()
# cow = Cow()
# animals.append(dog)
# animals.append(cat)
# animals.append(cow)

# for i in animals:
#     print(i.make_sound())






# class Shape:

#     def area(self):
#         pass


# class Circle(Shape):

#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         pi = 3.14
#         return pi * self.radius * self.radius
    

# class Rectangle(Shape):

#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.height * self.width
    

# class Triangle(Shape):

#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def area(self):
#         return 0.5 * self.base * self.height
    

# cir = Circle(11)
# rec = Rectangle(50,50)
# tri = Triangle(6,3)
# print(cir.area())
# print(rec.area())
# print(tri.area())





# class Payment:

#     def pay(self):
#         pass


# class CreditCardPayment(Payment):
        
#     def pay(self, amount):
#         print(f"Платёж прошёл с карты: {amount}")


# class PayPalPayment(Payment):
        
#     def pay(self, amount):
#         print(f"платёж прошёл через PayPal: {amount}")


# class CryptoPayment(Payment):
        
#     def pay(self, amount):
#         print(f"прошёл в криптовалюте: {amount}")


# credit = CreditCardPayment()
# paypal = PayPalPayment()
# crypto = CryptoPayment()

# lst = [credit,paypal,crypto]

# for payment in lst:
#     payment.pay(100)





# class Translator:

#     def translate(text):
#         pass


# class EnglishTranslator(Translator):

#     def translate(self, text):
#         return "Hello"
    

# class RussianTranslator(Translator):

#     def translate(self, text):
#         return "Привет"
    

# class TajikTranslator(Translator):

#     def translate(self, text):
#         return "Салом"
    

# eng = EnglishTranslator()
# print(eng.translate("Hello"))
# tjk = TajikTranslator()
# print(tjk.translate("Hello"))
# rus = RussianTranslator()
# print(rus.translate("Hello"))





# class Device:
#     def turn_on(self):
#         pass

# class TV(Device):
#     def turn_on(self):
#         print("включает телевизор")

# class WashingMachine(Device):
#     def turn_on(self):
#         print("запускает стирку")

# class Computer(Device):
#     def turn_on(self):
#         print("включает ПК")

# obj1 = TV()
# obj2 = WashingMachine()
# obj3 = Computer()
# lst = [obj1,obj2,obj3]

# for i in lst:
#     i.turn_on()




# class Shiritori:
#     def __init__(self):
#         self.words = []
#         self.game_over = False

#     def play(self, word):
#         if self.game_over:
#             return "game over"

#         if self.words:
#             if word in self.words or word[0] != self.words[-1][-1]:
#                 self.game_over = True
#                 return "game over"
        
#         self.words.append(word)
#         return self.words

#     def restart(self):
#         self.words = []
#         self.game_over = False
#         return "game restarted"


# game = Shiritori()

# print(game.play("apple")) 
# print(game.play("ear"))   
# print(game.play("rhino")) 
# print(game.play("corn"))



