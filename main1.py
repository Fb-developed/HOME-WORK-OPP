from datetime import datetime


class  User:

    def __init__(self,username,password,email):
        self.username = username
        self.password = password
        self.email = email


    def __str__(self):
        return self.username
    


class UserManager:

    login_status = False
    main_username = None

    def registation(self, username, password, email):
        with open('users.txt', 'a+') as file:
            file.seek(0)
            users = file.readlines()
            for user in users:
                data_username = user.split('-')[0]
                data_email = user.split('%')[1][:-1]

                if username == data_username or email == data_email:
                    print('User with this email or username exist')
                    return
            user = User(username,password,email)
            file.write(f"{user.username}-{user.password}%{user.email}\n")
            with open(f"{user.username}.txt",'w'):
                pass
            print("Succesfully registred!")


    def login(self,username,password):
        with open('users.txt','r') as file:
            users = file.readlines()
            for user in users:
                data_username = user.split('-')[0]
                data_password = user.split('%')[0].split('-')[1]
                if data_username == username:
                    if data_password == password:
                        print("You logged in!")
                        UserManager.login_status = True
                        UserManager.main_username = username
                        return
            print("Your password or username is incorect!")


class Task:

    def __init__(self,title,description,deadline):
        self.username = UserManager.main_username
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now().strftime('%d-%m-%Y')
        self.is_completed = False

    def __str__(self):
        return self.title
    

class TaskManager:

    def create_task(self,title,description,deadline):
        with open(f"{UserManager.main_username}.txt",'a+') as file:
            task = Task(title,description,deadline)
            file.write(f"{task.title} - {task.description} - {task.deadline} - {task.created_at}%{task.is_completed}")
            print("Task aded sucsessufily!")

    
    def read_all_task(self):
        with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()
                for i, name in enumerate(tasks):
                    print(f"{i}. {name.strip()}")


    def update_task(self,id):
        with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()

                if id < 0 or id >= len(tasks):
                    print("Invalid task ID.")
                    return

                title = input("Enter new title: ")
                description = input("Enter new description: ")
                deadline = input("Enter new deadline (dd-mm-yyyy): ")

                created_at = datetime.now().strftime('%d-%m-%Y')
                is_completed = tasks[id].split('%')[1].strip()

                tasks[id] = f"{title} - {description} - {deadline} - {created_at}%{is_completed}\n"

                with open(f"{UserManager.main_username}.txt", 'w') as file:
                    file.writelines(tasks)

                print("Task updated successfully.")

        
    def delete_task(self,id):
        with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()

                if id < 0 or id >= len(tasks):
                    print("Invalid task ID.")
                    return

                del tasks[id]

                with open(f"{UserManager.main_username}.txt", 'w') as file:
                    file.writelines(tasks)

                print("Task deleted successfully.")


    def make_completed(self,id):
         with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()

                if id < 0 or id >= len(tasks):
                    print("Invalid task ID.")
                    return

                parts = tasks[id].split('%')
                tasks[id] = f"{parts[0]}%True\n"

                with open(f"{UserManager.main_username}.txt", 'w') as file:
                    file.writelines(tasks)

                print("Task marked as completed.")


    def get_task_by_id(self,id):
        with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()

                if id < 0 or id >= len(tasks):
                    print("Invalid task ID.")
                    return

                print(tasks[id].strip())


    def get_completed_task(self):
         with open(f"{UserManager.main_username}.txt", 'r') as file:
                tasks = file.readlines()
                for task in tasks:
                    if '%True' in task:
                        print(task.strip())


manager = UserManager()
manager.registation('admin1','12345','admin1@mail.ru')
manager.login('admin1','12345')

task_manager = TaskManager()
task_manager.create_task('Task 1', 'Description for task 1', '15-06-2025')
task_manager.read_all_task()
# task_manager.make_completed
