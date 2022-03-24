def user_del(email, user_emails, users_storage):

    if email in user_emails:
        user_pass = input("Enter password: ")
        if user_pass == users_storage[email]['password']:
            choice = input(f"Are you sure you want to delete the user {email}?\nEnter 'yes' or 'not': ").lower()
            if choice == "yes" or choice == "y":
                users_storage.pop(email)
                print(f"User_email {email} deleted.")
            else:
                input("Please choice action 'create' or 'read', or 'update', or 'delete': ").lower()
        else:
            print("You entered invalid password. Profile access denied.")

    else:
        print(f"No user with email: {email}")
