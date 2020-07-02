import random
import string


def private_key():
    return ''.join([random.choice(string.ascii_lowercase) for i in range(10)])
