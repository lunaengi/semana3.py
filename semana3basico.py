#1
print(saludo_personalizado("Juan"))
#2
def filtrar_pares(lista):
    """Devuelve una lista con solo los números pares."""
    return [num for num in lista if num % 2 == 0]

#3
def par_o_impar(numero):
    return "Par" if numero % 2 == 0 else "Impar"
#4
def es_mayor_de_edad(edad):
    return "Mayor de edad" if edad >= 18 else "Menor de edad"
#5
def celsius_a_fahrenheit(grados_celsius):
    return (grados_celsius * 9/5) + 32
#6
def area_triangulo(base, altura):
    return (base * altura) / 2
#7
def mayor_de_lista(lista):
    return max(lista)
#8
def contar_vocales(cadena):
    return sum(1 for letra in cadena.lower() if letra in 'aeiou')

    
