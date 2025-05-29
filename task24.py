def is_valid_email(email):
    return not email.startswith("@") and email.endswith(".com")

print(is_valid_email("user@example.com"))   # True
print(is_valid_email("@example.com"))       # False
print(is_valid_email("user@example.net"))   # False