import random
import string
n = 8


def get_random_password() -> str:
    password_elements = str(string.ascii_lowercase+string.ascii_uppercase+string.digits) # TODO написать функцию генерации случайных паролей
    password_ = random.sample(password_elements, n)
    password = ",".join(password_)
    return password


print(get_random_password())
