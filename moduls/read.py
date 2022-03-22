import copy


def user_info(email, user_emails, users_storage):

    if email in user_emails:
        print(f"User_email = {email}\nUser_info: {users_storage[email]}")

    else:
        print(f"No user with email: {email}")


def all_users_info(users_storage):

    users_storage_copy = copy.deepcopy(users_storage)
    keys = users_storage_copy.keys()
    for keys in users_storage_copy:
        users_storage_copy[keys]["password"] = "****"
    # print(f"copy = {users_storage_copy}")
    # print(f"orig = {users_storage}")

    for k, v in users_storage_copy.items():

        user_email = "User_email: " + k
        user_info_1 = "User_info: ", v

        print(f"{user_email}\n{user_info_1}")
