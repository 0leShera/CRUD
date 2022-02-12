from CRUD.moduls.help import help
from CRUD.moduls.checks import *


def update_name(email, users_storage):
    n_name = input(f"Your name {users_storage[email]['name']}. Enter new name: ").lower()
    users_storage[email]['name'] = n_name
    print(f"Your new name: {n_name}.")


def update_email(email, users_storage, user_emails):
    n_email = input("Enter new email: ").lower()
    n_email = check_email(email, user_emails)
    users_storage[n_email] = users_storage.pop(email)
    user_emails.append(n_email)
    print(f"Your new email: {n_email}.")


def update_phone(email, phone, users_storage, user_phones):
    n_phone = input(f"Your phone {users_storage[email]['phone']}. Enter new phone: ")
    n_phone = check_phone(phone, user_phones)
    users_storage[email]['phone'] = n_phone
    print(f"Your new phone: {n_phone}.")


def update_password(email, users_storage):
    old_password = input("Enter your old password: ")
    fail = 0
    while old_password != users_storage[email]['password']:
        fail += 1
        old_password = input("Try again.\nEnter your old password: ")
        if fail == 3:
            help()
            print("Access denied.")
            # break
    if old_password == users_storage[email]['password']:
        n_password = input("Enter new password: ")
        n_password_2 = input("Again new password: ")
        while n_password != n_password_2:
            print("Password mismatch. Try again.")
            n_password = input("Enter new password: ")
            n_password_2 = input("Again new password: ")
        if n_password == n_password_2:
            users_storage[email]['password'] = n_password
            print("Your password update.")


def user_update(email, name, password, phone, user_emails, users_storage, user_phones):

    if email in user_emails:
        choice = input("What do you want to update?\n Email, name, phone or password: ").lower()
        if choice == "email":
            update_email(email, users_storage, user_emails)

        elif choice == "name":
            update_name(email, users_storage)

        elif choice == "phone":
            update_phone(email, phone, users_storage, user_phones)

        elif choice == "password":
            update_password(email, users_storage)

        # next_choice = input("Want to change something else: 'yes' or 'not'? ").lower()
        # if next_choice == "yes" or next_choice == "y":
        #     user_update(email, name, password, phone, user_emails, users_storage, user_phones)

    else:
        print(f"No user with email: {email}")


