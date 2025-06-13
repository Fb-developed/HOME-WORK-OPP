## 4. 🎓 Учебная система
# Описание:  
# Создайте классы Person, Student и Teacher.  
# - Student наследует Person и имеет список предметов.
# - Teacher наследует Person и имеет список предметов, которые он преподаёт.  
# Добавьте метод assign_course(course), который добавляет предмет студенту или учителю.4


# class Person:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname


# class Student(Person):
#     def __init__(self, firstname, lastname):
#         super().__init__(firstname, lastname)
#         self.courses = []


#     def assign_course(self,course):
#         self.courses.append(course)


#     def get_list(self):
#         return self.courses



# class Teacher(Person):
#    def __init__(self, firstname, lastname):
#         super().__init__(firstname, lastname)
#         self.courses = []


#    def assign_course(self,course):
#        self.courses.append(course)


#    def get_list(self):
#         return self.courses



# st = Student("John","David")
# t = Teacher("Umed","Rajabov")
# st.assign_course("Python")
# t.assign_course("Git")
# print(st.courses)
# print(t.courses)




# Создай класс Transport:

# Атрибуты: name, speed

# Метод: show_info() — выводит имя и скорость транспорта

# Создай подкласс Car, который:

# Наследует Transport

# Добавляет атрибут fuel_type

# Переопределяет метод show_info(), чтобы он также выводил fuel_type



# class Transport:
#     def __init__(self,name,speed):
#         self.name = name
#         self.speed = speed

    
#     def info(self):
#         return self.name + " " + self.speed
    

# class Car(Transport):
#     def __init__(self, name, speed,fuel_type):
#         super().__init__(name, speed)
#         self.fuel_type = fuel_type

    
#     def info(self):
#         return self.name + " " + self.speed + " " + self.fuel_type
    




# car = Car("Bmw","210","hello")
# print(car.info())




# ✅ 2. Человек и студент
# Создай класс Person:

# Атрибуты: name, age

# Метод: introduce() — выводит Привет, меня зовут {name}

# Создай подкласс Student, который:

# Добавляет атрибут university

# Добавляет метод study(), который выводит Я учусь в {university}



# class Person:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age


#     def introduce(self):
#         return f"Привет, меня зовут {self.name}"
    
# class Student(Person):
#     def __init__(self, name, age,university):
#         super().__init__(name, age)
#         self.university = university


#     def study(self):
#         return f"Я учусь в {self.university}"


# student = Student("john",21,"Softclub")
# print(student.introduce())
# print(student.study())


# ✅ 3. Животные
# Создай класс Animal:

# Атрибут: name

# Метод: speak() — выводит Животное издает звук

# Создай подкласс Cat, который:

# Переопределяет метод speak() так, чтобы он выводил Мяу


# class Animal:

#     def __init__(self,name):
#         self.name = name

    
#     def speak(self):
#         return "Животное издает звук"
    

# class Cat(Animal):

#     def speak(self):
#         return "Мяу"


# cat = Cat("Cat")
# print(cat.speak())


# ✅ 4. Фигуры
# Создай базовый класс Shape:

# Метод: area() — возвращает 0

# Создай два подкласса:

# Circle — принимает радиус, реализует area() как π * r²

# Rectangle — принимает ширину и высоту, реализует area() как width * height


# class Shape:

#     def area(self):
#         return 0
    
# class Circle(Shape):

#     pi = 3.14

#     def __init__(self,radius):
#         super().__init__()
#         self.radius = radius

#     def area(self):
#         return self.pi * self.radius * self.radius


# class Rectangle(Shape):
    
#     def __init__(self,width,height):
#         super().__init__()
#         self.height = height
#         self.width = width


#     def area(self):
#         return self.width * self.height
    

# cir = Circle(11)
# rec = Rectangle(100,200)
# print(cir.area())
# print(rec.area())


# ✅ 5. Сотрудники
# Создай класс Employee:

# Атрибуты: name, salary

# Метод: get_salary() — возвращает зарплату

# Создай подкласс Manager, который:

# Добавляет атрибут bonus

# Переопределяет get_salary() — возвращает salary + bonus


# class Employee:

#     def __init__(self,name,salary):
#         self.name = name 
#         self. salary = salary


#     def get_salary(self):
#         return self.salary
    

# class Manager(Employee):

#     def __init__(self, name, salary,bonus):
#         super().__init__(name, salary)
#         self.bonus = bonus

    
#     def get_salary(self):
#         return self.salary + self.bonus
    

# man = Manager("John",1500,300)
# print(man.get_salary())
    


# 🟢 Уровень 1: Базовый
# 1. Класс Student
# Создай класс Student, в котором:

# Приватный атрибут __grade (оценка).

# Метод get_grade() возвращает оценку.

# Метод set_grade() устанавливает оценку, но только если она от 0 до 100.


# class Student:
#     def __init__(self):
#         self.__grade = 0


#     def get_grade(self):
#             return self.__grade
    

#     def set_grade(self,grade):         
#          if 0 <= grade <= 100:
#             self.__grade = grade
#          else:
#               return "eror sum"

              
              

# student = Student()
# print(student.get_grade())
# student.set_grade(50)
# print(student.get_grade())


# 2. Класс Circle
# Создай класс Circle с:

# Приватным атрибутом __radius.

# Свойствами radius (getter и setter).

# В сеттере проверяй, чтобы радиус был положительным числом.


# class Circle:
#     def __init__(self):
#         self.__radius = 0

#     @property
#     def radius(self):
#         return self.__radius

#     @radius.setter
#     def radius(self, value):
#         if value > 0:
#             self.__radius = value
#         else:
#             return 'eror input'

    
# cir = Circle()
# print(cir.radius)
# cir.radius = 10
# print(cir.radius)


# 🟡 Уровень 2: Средний
# 3. Класс Account
# Создай класс Account, у которого:

# Приватное поле __balance.

# Метод deposit(amount) — пополнение (если сумма > 0).

# Метод withdraw(amount) — снятие (если хватает денег).

# Метод get_balance() — возвращает баланс.


# class Account:

#     def __init__(self):
#         self.__balnce = 0

#     def deposit(self,amount):
#         self.amount = amount
#         if amount > 0:
#             self.__balnce = amount
#         else:
#             print('eror input!')


#     def withdraw(self,amount):
#         self.amount = amount
#         if self.__balnce >= amount and amount > 0:
#             self.__balnce -= amount
#         else:
#             print('eror input! or no money to balance!')

    
#     def get_balance(self):
#         return self.__balnce



# account = Account()
# print(account.get_balance())
# account.deposit(1500)
# account.withdraw(100)
# print(account.get_balance())


# 4. Класс Temperature
# Создай класс, который:

# Хранит температуру в Цельсиях (__celsius).

# Имеет свойства:

# celsius — геттер и сеттер.

# fahrenheit — только геттер (переводит в °F по формуле C * 9/5 + 32).


# class Temprature:

#     def __init__(self):
#         self.__celsius = 0

    
#     @property
#     def celsius(self):
#         return self.__celsius

#     @celsius.setter
#     def celsius(self,value):
#         self.value = value
#         if value > 0:
#             self.__celsius = value
#         else:
#             print('eror input!')
    
#     @property
#     def fahrenheit(self):
#         return self.__celsius * 9 / 5 + 32
    

# temp = Temprature()
# print(temp.celsius)
# temp.celsius = 25
# print(temp.fahrenheit)




# 🔴 Уровень 3: Продвинутый
# 5. Класс Product
# Создай класс Product, у которого:

# Приватные поля __name, __price, __discount.

# Геттеры и сеттеры для каждого.

# Метод get_final_price() — возвращает цену с учётом скидки (если есть).



# class Product:

#     def __init__(self,):
#         self.__name = None
#         self.__price = 0
#         self.__discount = 0

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def price(self):
#         return self.__price
    
#     @property
#     def discount(self):
#         return self.__discount
    
#     @name.setter
#     def name(self,value):
#         self.value = value 
#         if isinstance(value, str):
#            self.__name = value         
    
#     @price.setter
#     def price(self,value):
#         if value > 0:
#            self.__price = value
    
#     @discount.setter
#     def discount(self,value):
#         if value > 0:
#            self.__discount = value


#     def get_final_price(self):
#            return self.__price * (1 - self.__discount / 100)
    


# pro = Product()
# pro.name = 'Laptop'
# pro.price = 2000
# pro.discount = 10
# print(pro.get_final_price())