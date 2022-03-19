opcion = 1
listaProductos=[]
productos={}
while(opcion!=0):
    print()
    print("1. Digitar 1 para recibir {código, nombre, precio} de un producto")
    print("2. Digitar 2 para mostrar todos los productos registrados")
    print("3. Digitar 3 para permitir buscar por código un producto y editar el preciode este")
    print("4. Digitar 4 para permitir buscar por código un producto y eliminar elproducto")
    print("5. Digitar 0 para SALIR")
    print()
    print()
    opcion =int(input("Digite una opcion: "));
    if(opcion==1):
        longitud=int(input("Digite la cantidad de productos que desea ingresar: "))
        for i in range(longitud):
            productos={'codigo':int(input("digite el codigo del producto: ")),'nombre':input("digite el nombre del producto: "),'precio':int(input("digite el precio del producto: "))}
            listaProductos.append(productos)
    elif(opcion==2):
        k=len(listaProductos)
        for i in range(k):    
            print(listaProductos[i])
    elif(opcion==3):
        codigo=int(input("digite el codigo del producto a buscar: "))
        for elem in listaProductos:      
            if(codigo==elem['codigo']):
                print(elem)
                elem['precio']=int(input('digite el nuevo precio: '))
                print(elem)
    elif(opcion==4):
        codigo=int(input("digite el codigo del producto a eliminar: "))
        for elem in listaProductos:      
            if(codigo==elem['codigo']):
                listaProductos.remove(elem)
                print(listaProductos)
    else:
        print("Salimos")