import re


def is_valid_re(pattern):
    try:
        re.compile(pattern)
    except re.error:
        return False
    return True
