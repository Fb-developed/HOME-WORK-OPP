from datetime import datetime


class  User:

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


    def __str__(self):
        return self.username
    


class UserManager:

    users = []
    login_status = False
    main_user = None

    def registation(self, username, password, email):
        for user in UserManager.users:
            if user.username == username or user.email == email:
                 print("User with this email or username already exist!")
                 return
        user = User(username,password,email)
        UserManager.users.append(user)
        print("Succesfully registred!")


    def login(self,username,password):
        for user in UserManager.users:
            if user.username == username and user.password == password:
                      print("You logged in!")
                      UserManager.login_status = True
                      UserManager.main_user = username
                      return 
        print("Your password or username is incorect!")


class Product:

    def __init__(self,name,price,quan):
        self.username = UserManager.main_user
        self.name = name
        self.price = price
        self.quan = quan

    def __str__(self):
        return self.name
    

class ProductManager:

    products = []

    def create_product(self,name,price,quan):
        product = Product(name,price,quan)
        ProductManager.products.append(product)
        print("Product aded sucsessufily!")

    
    def read_product(self):
        for i, product in enumerate(ProductManager.products, 1):
            print(f"{i}. {product.name} - {product.price} - {product.quan}")


    def update_product(self,id,name,price,quan):
        product = ProductManager.products[id-1]
        product.name = name
        product.price = price
        product.quan = quan
        print("Update product sucsessufuliy!")


    def delete_product(self,id):
        ProductManager.products.pop(id-1)
        print("Task deleted!")


    def buy_product(self, id, amount):
        product = ProductManager.products[id - 1]
        if product.quan >= amount:
            product.quan -= amount
            total_price = product.price * amount
            print(f"You quan {amount}x {product.name} for ${total_price}!")
        else:
            print(f" Not quan Only {product.quan} left.")
