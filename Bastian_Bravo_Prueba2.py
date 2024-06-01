lista_compras = []

nombre = input("\nBienvenido a su lista de compra, por favor ingrese su nombre: \n")

print(f"Hola, {nombre}")

rep = True
while rep:
    seleccion = int(input("\nPor favor seleccione una de las siguientes opciones digitando el numero correspondiente\n 1-. Agregar Producto y Cantidad\n 2-. Ver Lista\n 3-. Salir\n"))

    if seleccion > 3 or seleccion <= 0:
        print("Su seleccion esta fuera de los limites.\n")
    
    if seleccion == 1:
        agregar = input("Ingrese el producto y la cantidad correspondiente\n")
        lista_compras.append(agregar)
    
    if seleccion == 2:
        print("Aqui esta su lista\n",lista_compras)
        print ("Tiene una extension de dos productos", len(lista_compras))
        if len(lista_compras) == (0):
            print("La lista esta vacia\n")
    
    if seleccion == 3:
        rep = False
        print("Aqui esta su lista\n",lista_compras, "\n Gracias por contar con nuestra ayuda")
    
    