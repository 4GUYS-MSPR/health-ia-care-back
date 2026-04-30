import random
import string

from app.models.client import Client

def gen_code():
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def gen_client_code():
    while True:
        code = gen_code()
        if not Client.objects.filter(code=code).exists():
            return code
