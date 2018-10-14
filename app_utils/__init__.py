import re


def empty_string_catcher(value):
    value = ' '.join(value.split())
    if not value:
        return False
    return True



def is_string(value):
    if isinstance(value, str):
        return True
    return False

