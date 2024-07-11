"""
EXTRA
"""

def my_agenda():

    agenda = {}

    while True:

        print("1. Insertar contacto")
        print("2. Buscar contacto")
        print("3. Actualizar contacto")
        print("4. Borrar contacto")
        print("5. Salir")

        option = input ("\nSelecciona una opcion :")

        match option:
            case "1":
                name = input ("Introduce un nombre")
                phone = input ("Introduce el telefono")
                if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                    agenda[name] = phone
                else:
                    print("Debes introducir un numero de telefono con maximo de 11 digitos.")
                pass
            case "2":
                name = input ("Introduce el nombre a buscar:")
                if name in agenda:
                    print(f"El numero de telefono de {name} es {agenda[name]}")
                else:
                    print(f"El contacto {name} no existe")    
                pass
            case "3":
                name = input ("Introduce el nombre del contacto a actualizar")
                if name in agenda:
                    phone = input ("Introduce el telefono")
                    if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
                        agenda[name] = phone
                    else:
                        print("Debes introducir un numero de telefono con maximo de 11 digitos.")
                else:
                    print(f"El contacto {name} no existe")  
                pass
            case "4":
                name = input ("Introduce el nombre del contacto a eliminar")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe")  
                pass
            case "5":
                print ("Saliendo de la agenda.")
                break
            case _:
                print("Opcion no valida. Elige una opcion del 1 al 5.")


my_agenda()