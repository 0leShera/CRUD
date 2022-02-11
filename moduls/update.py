from CRUD.moduls.help import help


def update_name(email, users_storage):
    n_name = input(f"Your name {users_storage[email]['name']}. Enter new name: ").lower()
    users_storage[email]['name'] = n_name
    print(f"Your new name: {n_name}.")


def update_email(email, users_storage):
    n_email = input("Enter new email: ").lower()
    users_storage[email] = n_email
    print(f"Your new email: {n_email}.")


def update_phone(email, users_storage):
    n_phone = input(f"Your phone {users_storage[email]['phone']}. Enter new phone: ")
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


def user_update(email, user_emails, users_storage):

    if email in user_emails:
        choice = input("What do you want to update?\n Email, name, phone or password: ").lower()
        if choice == "email":
            update_email(email, users_storage)

        elif choice == "name":
            update_name(email, users_storage)

        elif choice == "phone":
            update_phone(email, users_storage)

        elif choice == "password":
            update_password(email, users_storage)
            # old_password = input("Enter your old password: ")
            # fail = 0
            # while old_password != users_storage[email]['password']:
            #     fail += 1
            #     old_password = input("Try again.\nEnter your old password: ")
            #     if fail == 3:
            #         break
            #         print("Access denied.")
            #         help()
            # if old_password == users_storage[email]['password']:
            #     n_password = input("Enter new password: ")
            #     n_password_2 = input("Again new password: ")
            #     while n_password != n_password_2:
            #         print("Password mismatch. Try again.")
            #         n_password = input("Enter new password: ")
            #         n_password_2 = input("Again new password: ")
            #     if n_password == n_password_2:
            #         users_storage[email]['password'] = n_password
            #         print("Your password update.")

    else:
        print(f"No user with email: {email}")


            # n_password = input(f"Your name {users_storage[email]['password']}. Enter new password: ")
            # users_storage[password]['password'] = n_password
            # print("Your password update.")
