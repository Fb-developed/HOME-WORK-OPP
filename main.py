# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#         self.pi = 3.14159

#     def getarea(self):
#         return self.pi * (self.radius ** 2)
    
#     def getperimetr(self):
#         return 2 * self.pi * self.radius

# circy = Circle(11)
# print(circy.getarea())
# print(circy.getperimetr())






# class Onethreenines:
#     def __init__(self,number):
#         self.nines = number // 9
#         res = number % 9
#         self.three = res // 3
#         self.ones = res % 3
# n1 = Onethreenines(5)
# print(n1.ones)
# print(n1.three)
# print(n1.nines)






# class Player:
#     def __init__(self,name,age,height,weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight

#     def get_age(self):
#         return f"{self.name} age {self.age}"
    
#     def get_height(self):
#         return f"{self.name} height {self.height}"
    
#     def get_weight(self):
#         return f"{self.name} weight {self.weight}"
    

# p1 = Player("Umed Rajabov",26, 180, 80)
# print(p1.get_age())
# print(p1.get_height())
# print(p1.get_weight())





# class Employee:
#     def __init__(self,first,last):
#         self.first = first
#         self.last = last
#         self.fullname = first + " " + last
#         self.email = (first + "." + last + "@company.com")


# emp1 = Employee("Umed", 'Rajabov')
# emp2 = Employee("Ali", 'Zokirov')
# emp3 = Employee("Alisher", 'Safarov')
# print(emp1.fullname)
# print(emp2.email)
# print(emp3.first)




# class User:
#     user_cnt = 0

#     def __init__(self,username):
#         self.username = username
#         User.user_cnt += 1

# user1 = User("john_doe")
# print(User.user_cnt)
# user2 = User("john_doe")
# print(User.user_cnt)
# user3 = User("john_doe")
# print(User.user_cnt)
# print(user1.username)





# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
    
#     def get_title(self):
#         return f"Title: {self.title}"
    
#     def get_author(self):
#         return f"Author: {self.author}"
    
# n = Book('Pride and Prejudie','Jane Austen')
# h = Book('Pride and Prejudie','Umed Rjabov')
# print(n.title)
# print(h.author)
# print(n.get_title())
# print(h.get_author())