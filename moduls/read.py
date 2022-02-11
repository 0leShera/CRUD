def user_info(email, user_emails, users_storage):

    if email in user_emails:
        print(f"User_email = {email}\nUser_info: {users_storage[email]}")

    else:
        print(f"No user with email: {email}")


def all_users_info(users_storage):
    # users_storage_copy = users_storage.copy()
    # for password in users_storage_copy[email]:
    #     password = "*****"

    for k, v in users_storage.items():

        user_email = "User_email: " + k
        user_info_1 = "User_info: ", v
        # user_info_1["password"] = "******"
        # print(users_storage)

        print(f"{user_email}\n{user_info_1}")