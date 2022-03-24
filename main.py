from CRUD.moduls.create import *
from CRUD.moduls.read import user_info, all_users_info
from CRUD.moduls.delete import user_del
from CRUD.moduls.update import *
from CRUD.moduls.help import help
from CRUD.moduls.checks import *
from CRUD.moduls.art import *


user_emails = []
user_phones = []
users_storage = {}


def enter_email():
    email = input("Enter user email: ").lower()
    while not (email.strip()):
        email = input("Enter email: ")
    return email


def CRUD():
    print("\n*** Enter 'help' to use tips. ***")
    while True:
        action = input("\n-- Please enter create or read, or update, or delete actions: ").lower()
        if action == "create" or action == "c":
            # print("action = ", action)

            email = input("Email: ").lower()
            email = check_email(email, user_emails)

            name = input("Name: ")
            while not(name.strip()):
                name = input("Enter name: ")

            password = input("Password (Use min 7 chars): ")
            password = check_password(password)

            phone = input("Phone (Don't use '+'): ")
            phone = check_phone(phone, user_phones)

            create_user(email, name, password, phone, user_emails, user_phones, users_storage)
            write_json(create_user(email, name, password, phone, user_emails, user_phones, users_storage))

            # Очистить все переменные после создания пользователя?
            email = None
            name = None
            password = None
            phone = None

            # print("user_emails = ", user_emails)
            print("users_storage = ", users_storage)

        elif action == "read_all" or action == "ra":
            # print("action = ", action)
            all_users_info(users_storage)

        elif action == "read_user" or action == "ru":
            # print("action = ", action)
            email = enter_email()
            user_info(email, user_emails, users_storage)

        elif action == "update" or action == "u":
            # print("action = ", action)
            email = enter_email()
            user_update(email, phone, user_emails, users_storage, user_phones)

        elif action == "delete" or action == "d":
            # print("action = ", action)
            email = enter_email()
            user_del(email, user_emails, users_storage)

        elif action == "help" or action == "h":
            help()

        else:
            print("Please select action again.")


print(art)
start = input("Do you want to use the crud app?\nEnter 'yes' to start, 'no' to exit: ")
if start == "no" or start == "n":
    print("Goodbye!")
elif start == "yes" or start == "y":
    print(art2)
    CRUD()

