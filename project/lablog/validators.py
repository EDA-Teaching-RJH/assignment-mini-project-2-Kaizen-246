# This file contains validation functions using regular expressions
import re
# Validates email format using regex pattern matching
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.fullmatch(pattern, email) is not None