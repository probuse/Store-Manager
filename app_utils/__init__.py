
def empty_string_catcher(value):
    value = ' '.join(value.split())
    if not value:
        return False
    return True

