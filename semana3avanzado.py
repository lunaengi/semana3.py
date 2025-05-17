#16
import re

def validar_contrasena(contrasena):
    return (len(contrasena) >= 8 and
            re.search(r"[A-Z]", contrasena) and
            re.search(r"[a-z]", contrasena) and
            re.search(r"[0-9]", contrasena) and
            re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena))
import random

#17
def lanzar_dado():
    return random.randint(1, 6)

#18
def suma_elementos_unicos(lista):
    return sum(set(lista))
import random
import string

#19
def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

#20
def composicion(func1, func2):
    return lambda x: func2(func1(x))