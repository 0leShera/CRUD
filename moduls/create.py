def create_user(email, name, password, phone, user_emails, users_storage):

    user_info = [email, name, password, phone]
    user_emails.append(email)
    users_storage[email] = {"name": name,
                            "password": password,
                            "phone": phone}

    print("create_user_f = ", user_info)
