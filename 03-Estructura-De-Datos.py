# Listas
my_list = ["Naow", "Bryan","Kel","yurk"]
print(my_list)
my_list.append("Juan") # Insercion
my_list.append("Juan")
print(my_list)
my_list.remove("Naow") # Eliminacion
print(my_list)
print(my_list[2])
my_list[1] = "Cuervo" # Actualizacion
print(my_list)
my_list.sort() # Ordenacion
print(my_list)

# Tuplas
my_tuple = ("Brais", "Moure", "@mouredev", "36")
print(my_tuple[1]) # Acceso
my_tuple = tuple(sorted(my_tuple)) # Ordenacion
print(my_tuple)

# Sets
my_set = {"Brais", "Moure", "@mouredev", "36"}
print(my_set)
my_set.add("mouredev@mmail.com") # Inserccion
my_set.add("mouredev@mmail.com")
print(my_set)
my_set.remove("Moure") # Eliminacion
print(my_set)
my_set = set(sorted(my_set)) # No se puede ordenar
print(my_set)

# Diccionarios
my_dict = {
    "nombre":"Brais",
    "Alias":"Moure",
    "mail":"@mouredev",
    "edad":"36"
}
my_dict["mail"] = "naowcs@gmail.com" # Inserccion
print(my_dict)
print(my_dict["mail"]) # Acceso
print(my_dict)
my_dict["age"] = "38" # Actualizacion
print(my_dict)
del my_dict["Alias"]# Eliminacion
print(my_dict)
my_dict = dict(sorted(my_dict.items())) # Ordenacion
print(my_dict)