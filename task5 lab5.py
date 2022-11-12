import random
import string
n = 8


def get_random_password() -> str:
    password_elements = str(string.ascii_lowercase+string.ascii_uppercase+string.digits) # TODO написать функцию генерации случайных паролей
    password = random.sample(password_elements, 8)
    return password


print(get_random_password())
