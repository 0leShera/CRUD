from CRUD.moduls.help import help


def user_update(email, name, password, phone, user_emails, users_storage):

    if email in user_emails:
        choice = input("What do you want to update?\n Email, name, phone or password: ").lower()
        if choice == "email":
            n_email = input("Enter new email: ").lower()
            users_storage[email] = n_email

        elif choice == "name":
            n_name = input(f"Your name {users_storage[email]['name']}. Enter new name: ").lower()
            users_storage[email]['name'] = n_name
            print("Your name update.")

        elif choice == "phone":
            n_phone = input(f"Your phone {users_storage[email]['phone']}. Enter new phone: ")
            users_storage[email]['phone'] = n_phone
            print("Your phone update.")

        elif choice == "password":
            old_password = input("Enter your old password: ")
            fail = 0
            while old_password != users_storage[email]['password']:
                fail += 1
                old_password = input("Try again.\nEnter your old password: ")
                if fail == 3:
                    break
                    print("Access denied.")
                    help()
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

    else:
        print(f"No user with email: {email}")


            # n_password = input(f"Your name {users_storage[email]['password']}. Enter new password: ")
            # users_storage[password]['password'] = n_password
            # print("Your password update.")
