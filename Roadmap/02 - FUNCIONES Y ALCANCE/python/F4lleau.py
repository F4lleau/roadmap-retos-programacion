"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 """
 
 # Función sin parámetros ni retorno
def funcion_sin_parametros():
    print("Esta es una función sin parámetros ni retorno.")

# Función con uno o varios parámetros
def funcion_con_parametros(param1, param2):
    print(f"Esta es una función con parámetros: {param1} y {param2}")

# Función con retorno
def funcion_con_retorno(a, b):
    return a + b

# Función dentro de una función
def funcion_externa():
    print("Esta es la función externa.")

    def funcion_interna():
        print("Esta es la función interna.")
    
    funcion_interna()

# Ejemplo de función ya creada en el lenguaje (uso de len)
def uso_de_funcion_existente():
    lista = [1, 2, 3, 4, 5]
    longitud = len(lista)
    print(f"La longitud de la lista es: {longitud}")

# Variables locales y globales
global_var = "Soy global"

def variable_local_global():
    local_var = "Soy local"
    print(local_var)
    print(global_var)

# Dificultad extra: función que recibe dos cadenas y retorna un número
def dificultad_extra(cadena1, cadena2):
    contador = 0
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print(cadena1 + cadena2)
        elif num % 3 == 0:
            print(cadena1)
        elif num % 5 == 0:
            print(cadena2)
        else:
            print(num)
            contador += 1
    return contador

# Llamadas a las funciones
print("Ejemplos de funciones básicas:")
funcion_sin_parametros()
funcion_con_parametros("Hola", "Mundo")
resultado = funcion_con_retorno(5, 7)
print(f"Resultado de la función con retorno: {resultado}")
funcion_externa()
uso_de_funcion_existente()
variable_local_global()

print("\nDificultad extra:")
numero_de_numeros = dificultad_extra("Fizz", "Buzz")
print(f"Número de veces que se ha impreso un número: {numero_de_numeros}")
