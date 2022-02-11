

def check_email(email, user_emails):
    while "@" not in email or email in user_emails:
        if "@" not in email:
            email = input("Please, enter correct email: ").lower()
        elif email in user_emails:
            email = input("This email address is already in use. Enter another: ").lower()
    else:
        return email


def check_phone(phone):
    while "+7" not in phone:
        phone = input("""
        Please, enter correct phone. Example:
        +79999999999
        89999999999
        
        """)

