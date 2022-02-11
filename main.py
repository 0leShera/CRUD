from CRUD.moduls.create import create_user
from CRUD.moduls.read import user_info, all_users_info
from CRUD.moduls.delete import user_del
from CRUD.moduls.update import *
from CRUD.moduls.help import help
from CRUD.moduls.checks import *
from CRUD.moduls.art import art


user_emails = []
user_phones = []
users_storage = {}


print(art)
help()

while True:
    action = input("Please enter create or read, or update, or delete actions: ").lower()
    if action == "create" or action == "c":
        print("action = ", action)

        email = input("Email: ").lower()
        email = check_email(email, user_emails)
        name = input("Name: ").lower()
        while not(name.strip()):
            name = input("Enter name: ").lower()
        password = input("Password: ")
        while len(password) == 0:
            password = input("Enter password: ")
        phone = input("Phone: ")
        phone = check_phone(phone, user_phones)
        create_user(email, name, password, phone, user_emails, user_phones, users_storage)
        print("user_emails = ", user_emails)
        print("users_storage = ", users_storage)

    elif action == "read_all" or action == "ra":
        print("action = ", action)
        all_users_info(users_storage)

    elif action == "read_user" or action == "ru":
        print("action = ", action)
        user_e = input("Enter user email: ").lower()
        message = user_info(user_e, user_emails, users_storage)
        # print("User = ", message)

    elif action == "update" or action == "u":
        print("action = ", action)
        user_e = input("Enter user email: ").lower()
        message = user_update(email, name, password, phone, user_emails, users_storage)

    elif action == "delete" or action == "d":
        print("action = ", action)
        user_e = input("Enter user email: ").lower()
        message = user_del(email, user_emails, users_storage)

    elif action == "help" or action == "h":
        help()

    else:
        print("Please select action again.")
