# Session 22 - Custom Exceptions


class AgeError(Exception):
    """Custom exception for age-related errors."""

    pass


def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative!")


try:
    check_age(-5)
except AgeError as e:
    print("Error:", e)
