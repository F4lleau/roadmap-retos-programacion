#OPERADORES

"""
 EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

"""
def ejemplos_operadores():
    # Operadores aritméticos
    a = 10
    b = 5
    print("Aritméticos:")
    print(f"Suma: {a} + {b} = {a + b}")
    print(f"Resta: {a} - {b} = {a - b}")
    print(f"Multiplicación: {a} * {b} = {a * b}")
    print(f"División: {a} / {b} = {a / b}")
    print(f"División entera: {a} // {b} = {a // b}")
    print(f"Módulo: {a} % {b} = {a % b}")
    print(f"Exponente: {a} ** {b} = {a ** b}")

    # Operadores de comparación
    print("\nComparación:")
    print(f"{a} == {b}: {a == b}")
    print(f"{a} != {b}: {a != b}")
    print(f"{a} > {b}: {a > b}")
    print(f"{a} < {b}: {a < b}")
    print(f"{a} >= {b}: {a >= b}")
    print(f"{a} <= {b}: {a <= b}")

    # Operadores lógicos
    x = True
    y = False
    print("\nLógicos:")
    print(f"{x} and {y}: {x and y}")
    print(f"{x} or {y}: {x or y}")
    print(f"not {x}: {not x}")

    # Operadores de asignación
    c = 10
    print("\nAsignación:")
    c += 5
    print(f"c += 5: {c}")
    c -= 3
    print(f"c -= 3: {c}")
    c *= 2
    print(f"c *= 2: {c}")
    c /= 4
    print(f"c /= 4: {c}")
    c %= 3
    print(f"c %= 3: {c}")
    c **= 2
    print(f"c **= 2: {c}")

    # Operadores de identidad
    print("\nIdentidad:")
    d = [1, 2, 3]
    e = d
    f = [1, 2, 3]
    print(f"d is e: {d is e}")
    print(f"d is f: {d is f}")
    print(f"d is not f: {d is not f}")

    # Operadores de pertenencia
    print("\nPertenencia:")
    print(f"1 in d: {1 in d}")
    print(f"4 not in d: {4 not in d}")

    # Operadores a nivel de bits
    print("\nBits:")
    g = 6  # 110 en binario
    h = 2  # 010 en binario
    print(f"g & h: {g & h}")  # AND
    print(f"g | h: {g | h}")  # OR
    print(f"g ^ h: {g ^ h}")  # XOR
    print(f"~g: {~g}")  # NOT
    print(f"g << 1: {g << 1}")  # Desplazamiento a la izquierda
    print(f"g >> 1: {g >> 1}")  # Desplazamiento a la derecha

def estructuras_control():
    # Condicionales
    print("\nCondicionales:")
    a = 10
    if a > 5:
        print("a es mayor que 5")
    elif a == 5:
        print("a es igual a 5")
    else:
        print("a es menor que 5")

    # Iterativas
    print("\nIterativas:")
    print("For loop:")
    for i in range(5):
        print(f"i: {i}")

    print("While loop:")
    j = 0
    while j < 5:
        print(f"j: {j}")
        j += 1

    # Excepciones
    print("\nExcepciones:")
    try:
        k = 10 / 0
    except ZeroDivisionError:
        print("Error: División por cero.")
    finally:
        print("Bloque finally ejecutado.")

def numeros_especiales():
    print("\nNúmeros especiales:")
    for num in range(10, 56):
        if num % 2 == 0 and num != 16 and num % 3 != 0:
            print(num)

if __name__ == "__main__":
    ejemplos_operadores()
    estructuras_control()
    numeros_especiales()

"""
La f antes de las comillas en Python se utiliza para definir un f-string (formatted string literal), que es una manera conveniente y eficiente de incluir expresiones dentro de una cadena de texto. Las expresiones incluidas dentro de llaves {} se evalúan en tiempo de ejecución y se insertan en la cadena en esas posiciones.

Por ejemplo:

a = 10
b = 5
print(f"Suma: {a} + {b} = {a + b}")
En este caso, f"Suma: {a} + {b} = {a + b}" es una f-string. Las expresiones {a}, {b} y {a + b} dentro de la cadena se reemplazan por los valores de a, b y a + b, respectivamente, al momento de la ejecución. Por lo tanto, el resultado será:

Suma: 10 + 5 = 15
Las f-strings son una característica introducida en Python 3.6 y proporcionan una sintaxis más clara y concisa para el formateo de cadenas en comparación con otros métodos como el operador %, str.format() y la concatenación de cadenas.
"""