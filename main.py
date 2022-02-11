from CRUD.moduls.create import create_user
from CRUD.moduls.read import user_info, all_users_info
from CRUD.moduls.delete import user_del
from CRUD.moduls.update import user_update
from CRUD.moduls.help import help
from CRUD.moduls.checks import check_email, check_phone


user_emails = []
users_storage = {}
# email_correct = False


# def check_email(email, user_emails):
#     while "@" not in email or email in user_emails:
#         if "@" not in email:
#             email = input("Please, enter correct email: ").lower()
#         elif email in user_emails:
#             email = input("This email address is already in use. Enter another: ").lower()
#     else:
#         return email

help()

while True:
    action = input("Please enter create or read, or update, or delete actions: ").lower()
    if action == "create" or action == "c":
        print("action = ", action)

        email = input("Email: ").lower()
        email = check_email(email, user_emails)
        name = input("Name: ").lower()
        password = input("Password: ")
        phone = input("Phone: ")
        create_user(email, name, password, phone, user_emails, users_storage)
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
