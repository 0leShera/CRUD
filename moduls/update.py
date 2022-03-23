from CRUD.moduls.help import help
from CRUD.moduls.checks import *


def update_name(email, users_storage):
    print(f"Your name {users_storage[email]['name']}.")
    users_storage[email]['name'] = None
    n_name = input("Enter new name: ").lower()
    users_storage[email]['name'] = n_name
    print(f"Your new name: {n_name}.")


def update_email(email, users_storage, user_emails):
    old_email = email
    user_emails.remove(email)      # Удалить старый email из базы
    # print(user_emails)
    # print(users_storage)
    email = None
    email = input("Enter new email: ").lower()
    email = check_email(email, user_emails)
    users_storage[email] = users_storage.pop(old_email)
    user_emails.append(email)
    # print(user_emails)
    print(f"Your new email: {email}.")


def update_phone(email, phone, users_storage, user_phones):
    print(f"Your phone {users_storage[email]['phone']}.")
    user_phones.remove(users_storage[email]['phone'])
    # print(user_phones)
    users_storage[email]['phone'] = None
    phone = input("Enter new phone: ")
    # phone = n_phone
    phone = check_phone(phone, user_phones)
    users_storage[email]['phone'] = phone
    user_phones.append(phone)
    print(f"Your new phone: {phone}.")
    # print(user_phones)


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


def user_update(email, phone, user_emails, users_storage, user_phones):
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
