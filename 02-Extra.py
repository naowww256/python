def parametros(texto1, texto2):
    for i in range(100):
        if  i % 5 == 0 and i % 3 == 0:
            print (str(i) + ' ' + texto1 + ' y ' +texto2)
        elif i % 3 == 0:
            print(str(i) + ' ' + texto2)
        elif i%5 == 0:
            print (str(i) + ' ' + texto1)

parametros("teta","pito")