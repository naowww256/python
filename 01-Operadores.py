# Ejemplos utilizando todo tipo de operadores
# Operadores aritméticos
suma = 1 + 2
resta = 4 - 1
multiplicacion = 3 * 5
division = 15 / 3
potencia = 2*4
resto = 13 % 2
division_numero_entero = 25 // 4

# Operadores relacionales
mayor = 6 > 3
menor = 2 < 4
igual = 3 == 3
mayor_igual = 10 >= 12
menor_igual = 10 <= 12
diferente = 10 != 12

# Operadores bit a bit
a = 1
b = 2
resultado = a & b #Realiza bit a bit la operación AND en los operandos
resultado = a | b
resultado = a ^ b
resultado = ~a
resultadp = a >> b
resultado = a << b

# Operadores de asignación
c = 3
c += 5
c -= 5
c= 2
c /= 3

# Operadores lógicos
d = 10
e = 15
f = 20

d > e and e > f
d > e or e < f
not e

# Ejemplos de estructuras de control
# Condicionales
variable_1 = 20
variable_2 = 15
if variable_1 < variable_2:
    print ('La variable 1 es menor que la variable 2')
elif variable_1 > variable_2:
    print ('La variable 1 es mayor que la variable 2')
else:
    print ('La variable 1 es igual a la variable 2')

# Bucles for
for i in range(5):
    print(i)

# Bucles while
x = 0
while x < 10:
    print(x)
    x += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")