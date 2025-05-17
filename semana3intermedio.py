#9
def filtrar_pares(lista):
    """Devuelve una lista con solo los números pares."""
    return [num for num in lista if num % 2 == 0]
#10
def palindromo(texto):
    return texto == texto[::-1]
#11
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#12    
def eliminar_duplicados(lista):
    return list(set(lista))
#13
def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero
#14    
def contar_vocales(cadena):
    return sum(1 for letra in cadena.lower() if letra in 'aeiou')
#15
def invertir_texto(texto):
    return texto[::-1]