from main import UserManager, ProductManager

user_manager = UserManager()
product_manager = ProductManager()

while True:
    if not user_manager.login_status:
        print("""
1. Registration
2. Login
""")
    choise = input("choose one: ")
    if choise == "1":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        email = input("Enter your email: ")
        user_manager.registation(username,password,email)
        continue
    elif choise == "2":
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_manager.login(username,password)
    while UserManager.login_status:
        print("""
1. Created product
2. Read product
3. Update product
4. Delete product
5. Buy product
6. Exit
""")
        choise = input("choose one: ")
        if choise == "1":
            name = input("Enter product name: ")
            price = int(input("Enter price product: "))
            quan = int(input("Enter quan product: "))
            product_manager.create_product(name,price,quan)
        elif choise == "2":
            print("--------------- Products ---------------")
            print()
            product_manager.read_product()
            print()
            print("=" * 38)
        elif choise == "3":
            id = int(input("Enter you product number: "))
            name = input("Enter new name for update: ")
            price = input("Enter new price for update: ")
            quan = input("Enter new quan for update: ")
            product_manager.update_product(id,name,price,quan)
        elif choise == '4':
            id = int(input("Enter you product number for delete: "))
            product_manager.delete_product(id)
        elif choise == "5":
            print("--------------- Products ---------------")
            print()
            product_manager.read_product()
            print()
            print("=" * 38)
            id = int(input("Enter id to buy: "))
            amount = int(input("Amount to buy: "))
            product_manager.buy_product(id, amount)
        elif choise == "6":
            break
        