from datetime import datetime
import random, string, time


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.email = email

        if self.__validate_password(password):
            self.__password = password
        else:
            self.__password = User.create_random_password()
            print("Your generated password is:", self.__password)

        self.__create_email_for_user()

    def __validate_password(self, password):
        digit = False
        upper = False
        symbol = False
    
        for c in password:
            if c.isdigit():
                digit = True
            elif c.isupper():
                upper = True
            elif c in string.punctuation:
                symbol = True
    
        return len(password) > 7 and digit and upper and symbol


    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def __create_email_for_user(self):
        with open(f"{self.email}.txt", 'w'):
            pass

    @staticmethod
    def create_random_password():
        digit = random.choice(string.digits)
        up_letter = random.choice(string.ascii_uppercase)
        symbol = random.choice(string.punctuation)
        printable = string.digits + string.ascii_letters + string.punctuation
        other = random.choices(printable, k=6)
        password_list = [digit, up_letter, symbol] + other
        random.shuffle(password_list)
        return ''.join(password_list)


class UserManager:
    users = []
    login_status = False
    main_user = None

    def registration(self, username, password, email):
        for user in UserManager.users:
            if user.username == username or user.email == email:
                print("User with this email or username already exists!")
                return
        user = User(username, password, email)
        UserManager.users.append(user)
        print("Successfully registered!")

    def login(self, username, password):
        for user in UserManager.users:
            if user.username == username and user.password == password:
                print("You logged in!")
                UserManager.login_status = True
                UserManager.main_user = user 
                return
        print("Your password or username is incorrect!")

    def update_password(self, new_password, old_password=None, email=None):
        if old_password:
            if UserManager.main_user and UserManager.main_user.password == old_password:
                UserManager.main_user.password = new_password
                print("Password updated!")
            else:
                print("Old password is incorrect.")
        elif email: 
            for user in UserManager.users:
                if user.email == email:
                    user.password = new_password
                    print("Password reset successful!")

    def __create_random_code(self):
        return random.choice(string.ascii_uppercase) + ''.join(random.choices(string.digits, k=6))

    def forgot_password(self, email):
        code = self.__create_random_code()
        with open(f"{email}.txt", 'w') as file:
            file.write(code)
        print("We sent a code to your email!")
        time.sleep(2)
        code_input = input("Enter your email code: ")
        if code == code_input:
            new_password = input("Enter new password: ")
            self.update_password(new_password=new_password, email=email)
        else:
            print("Invalid code!")


class Product:
    def __init__(self, name, price, quan):
        self.username = UserManager.main_user.username
        self.name = name
        self.price = price
        self.quan = quan

    def __str__(self):
        return self.name


class ProductManager:
    products = []

    def create_product(self, name, price, quan):
        product = Product(name, price, quan)
        ProductManager.products.append(product)
        print("Product added successfully!")

    def read_product(self):
        for i, product in enumerate(ProductManager.products, 1):
            print(f"{i}. {product.name} - {product.price} - {product.quan}")

    def update_product(self, id, name, price, quan):
        product = ProductManager.products[id - 1]
        product.name = name
        product.price = price
        product.quan = quan
        print("Product updated successfully!")

    def delete_product(self, id):
        ProductManager.products.pop(id - 1)
        print("Product deleted!")

    def buy_product(self, id, amount):
        product = ProductManager.products[id - 1]
        if product.quan >= amount:
            product.quan -= amount
            total_price = product.price * amount
            print(f"You bought {amount}x {product.name} for ${total_price}!")
        else:
            print(f"Only {product.quan} left.")
