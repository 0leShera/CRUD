def user_del(email, user_emails, users_storage):

    if email in user_emails:
        choice = input(f"Are you sure you want to delete the user {email}?\nEnter 'yes' or 'not': ").lower()
        if choice == "yes" or choice == "y":
            users_storage.pop(email)
            print(f"User_email {email} deleted.")
        else:
            input("Please choice action 'create' or 'read', or 'update', or 'delete': ").lower()
        # print(f"User_email = {email} deleted.")
        # users_storage.pop(email)

        # print(f"{users_storage}")

    else:
        print(f"No user with email: {email}")
