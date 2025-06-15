from main import UserManager, ProductManager

user_manager = UserManager()
product_manager = ProductManager()

while True:
    if not user_manager.login_status:
        print("""
1. Registration
2. Login
3. Forgot password
""")
        choice = input("Choose one: ")
        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            email = input("Enter your email: ")
            user_manager.registration(username, password, email)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user_manager.login(username, password)
        elif choice == "3":
            email = input("Enter your email: ")
            user_manager.forgot_password(email)

    while user_manager.login_status:
        print("""
1. Create product
2. Read product
3. Update product
4. Delete product
5. Buy product
6. Update password
7. Log out
""")
        choice = input("Choose one: ")
        if choice == "1":
            name = input("Enter product name: ")
            price = int(input("Enter product price: "))
            quan = int(input("Enter product quantity: "))
            product_manager.create_product(name, price, quan)
        elif choice == "2":
            print("--------- Products ---------")
            product_manager.read_product()
        elif choice == "3":
            id = int(input("Enter product number: "))
            name = input("New name: ")
            price = int(input("New price: "))
            quan = int(input("New quantity: "))
            product_manager.update_product(id, name, price, quan)
        elif choice == "4":
            id = int(input("Enter product number to delete: "))
            product_manager.delete_product(id)
        elif choice == "5":
            print("--------- Products ---------")
            product_manager.read_product()
            id = int(input("Enter product ID to buy: "))
            amount = int(input("Amount to buy: "))
            product_manager.buy_product(id, amount)
        elif choice == "6":
            old_password = input("Enter old password: ")
            new_password = input("Enter new password: ")
            user_manager.update_password(new_password=new_password, old_password=old_password)
        elif choice == "7":
            print("Logged out!")
            user_manager.login_status = False
            user_manager.main_user = False
            break
