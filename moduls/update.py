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
    user_emails.remove(email)  # Удалить старый email из базы
    # print(user_emails)
    # print(users_storage)
    # email = None
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


def correct_password(n_password_1, n_password_2):
    if len(n_password_1) >= 7 and len(n_password_2) >= 7:
        return True


def update_password(email, users_storage):
    #  Для смены пароля необходимо корректно ввести старый.
    #  Всего есть 3 попытки, после которых пользователя перебрасывает в главное меню.
    old_password = input("Enter your old password: ")
    fail = 3
    while old_password != users_storage[email]['password']:
        fail -= 1
        old_password = input(f"Try again. There are {fail} attempts left.\nEnter your old password: ")
        if fail == 1:
            print("You entered 3 invalid passwords. Profile access denied.")
            break

    # Когда пароль введен верно, его можно изменить.
    if old_password == users_storage[email]['password']:
        n_password_1 = input("Enter new password: ")
        n_password_2 = input("Again new password: ")
        # До тех пор пока новый пароль не подтвержден.
        while n_password_1 != n_password_2 or not correct_password(n_password_1, n_password_2):
            if n_password_1 != n_password_2:
                print("Passwords mismatch. Try again.")
            elif not correct_password(n_password_1, n_password_2):
                print("Passwords invalid. Try again.")
            n_password_1 = input("Enter new password. Use min 7 chars: ")
            n_password_2 = input("Again new password. Use min 7 chars: ")

        # Если пароль подтвержден.
        if n_password_1 == n_password_2 and correct_password(n_password_1, n_password_2):
            users_storage[email]['password'] = n_password_1
            print("Your password update.")


def user_update(email, phone, user_emails, users_storage, user_phones):
    if email in user_emails:
        choice = input("-- What do you want to update?\nEmail, name, phone or password: ").lower()
        if choice == "email" or choice == "1":
            update_email(email, users_storage, user_emails)

        elif choice == "name" or choice == "2":
            update_name(email, users_storage)

        elif choice == "phone" or choice == "3":
            update_phone(email, phone, users_storage, user_phones)

        elif choice == "password" or choice == "4":
            update_password(email, users_storage)

        next_choice = input("Want to change something else: 'yes' or 'not'? ").lower()
        if next_choice == "yes" or next_choice == "y":
            if email not in user_emails:
                email = input("Enter user email: ").lower()
            user_update(email, phone, user_emails, users_storage, user_phones)

    else:
        print(f"No user with email: {email}")
