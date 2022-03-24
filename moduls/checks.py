import re

r_mail = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
numbers = '[0-9]'
letters = '[a-zA-Z]'


def correct_email(email):
    if re.search(r_mail, email):
        return True
    else:
        return False


def check_email(email, user_emails):
    while not correct_email(email) or email in user_emails:
        if not correct_email(email):
            email = input("Please, enter correct email: ").lower()
        elif email in user_emails:
            email = input("This email address is already in use. Enter another: ").lower()
    else:
        return email


def check_phone(phone, user_phones):
    correct_phone = False
    while (len(phone) < 9 or len(phone) > 12) or not phone.isdigit() or phone in user_phones and not correct_phone:
        if (len(phone) < 9 or len(phone) > 12) or not phone.isdigit():
            phone = input("""
            Please, enter correct phone.
            Don't use '+' and letters. Example: 89997654321.
            Enter: """)
        if phone in user_phones:
            phone = input("This phone is already in use. Enter another: ")
    else:
        correct_phone = True
        return phone


def check_password(password):
    while len(password) < 7:
        password = input("""
        Please, use correct password.
        Use minimum 7 chars. Use letters and numbers.
        Enter:
        """)
    else:
        return password
