from lablog.validators import is_valid_email

email = input("Enter email: ")

if is_valid_email(email):
    print("Valid email")
else:
    print("Invalid email")