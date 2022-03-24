import json


def create_user(email, name, password, phone, user_emails, user_phones, users_storage):
    user_info = [email, name, password, phone]
    user_emails.append(email)
    users_storage[email] = {"name": name,
                            "password": password,
                            "phone": phone}

    # print("create_user_f = ", user_info)
    user_phones.append(phone)
    return users_storage


def write_json(users_dict):
    try:
        data = json.load(open("users.json"))
    except:
        data = []

    data.append(users_dict)

    with open("users.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


