"""
Funciones definidas por el usuario
"""

# Simple

def greet():
    print("Hola, Python!")

greet()

# Con retorno

def return_greet():
    return "Hola, Python!"

greet = return_greet()
print(greet)

# Con un argumento 

def arg_greet(greet, name):
    print(f"{greet}, {name}!")

arg_greet("hola","Manolo")
arg_greet(name="Manolo",greet="hi")

#Con un argumento predeterminado

def default_arg_greet (name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Ivan")
default_arg_greet()

# Con argumentos y retorn

def return_args_greet(greet, name):
    return f"{greet}, {name}"

print(return_args_greet("Hi", "Brais"))

# Con retorno de varios valores

def multiple_return_greet():
    return "Hola", "Python"

greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un numero variable de argumentos

def variable_arg_greet (*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python", "Brais", "MoureDev", "Comunidad")

# cON UN NUMERO VARIABLE DE ARGUMENTOS CON PALABRA CLAVE

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")

print (variable_key_arg_greet(
    language="Python",
    name="Brais", 
    alias="MoureDev",
    age=36
))

"""
Funciones DENTRO DE FUNCIONES
"""

def outer_function():
    def inner_function():
        print("Funcion interna: Hola, Python!")
    inner_function()

outer_function()

"""
FUNCIONES DEL LENGUAJE (built-in)
"""

print(len("NaOw"))
print(type(36))
print("NaoW".upper())

"""
Variables locales y globales
"""

global_variable = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_variable}")


print(global_variable)
# print(local_var) No se puede acceder desde fuera de la funcion

hello_python()

"""
Extra
"""

def print_numbers(text1, text2) -> int:
    count = 0
    for number in range(1, 101):
        if  number % 3 == 0 and number % 5 == 0:
            print(text1 + text2)
        elif number % 3 == 0:
            print(text1)
        elif number % 5 == 0:
            print(text2)
        else: 
            print(number)
            count += 1
    return count

print(print_numbers("Texto 1", "Texto 2"))