class Articulo:
    def __init__(self,codigo,nombre,precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo
    def set_codigo(self,valor):
        self.__codigo=valor

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,valor):
        self.__nombre=valor

    def get_precio(self):
        return self.__precio
    def set_precio(self,valor):
        self.__precio=valor

    
    def calcular_subtotal(self, unidades):
        subtotal=unidades * self.get_precio()
        return subtotal

    def __str__(self):
        return "El codigo es {} el Nombre es {} y el precio es S/.{}".format(self.__codigo, self.__nombre, self.__precio)

class Pedido:
    def __init__(self):
        self.articulos=[]
        self.cantidades=[]

    def total_pedido(self):
        #calcular los subtotales parciales
        total=0
        for a,c in zip(self.articulos, self.cantidades):
            total=total + a.calcular_subtotal(c)
        return total

    def mostrar_pedido(self):
        for a,c in zip(self.articulos, self.cantidades):
            print("Ariculo:",a.get_nombre(),"PrecioUnit:",a.get_precio()," cantidad", c,"sub total: ",c * a.get_precio())

    def añadir_articulo(self,arti,cantidad):
        #validamos las entradas
        #si arti NO es un articulo
        if not isinstance(arti,Articulo):
            raise Exception("El articulo ingresado NO es un articulo")
        if not isinstance(cantidad,int):
            raise Exception("La cantidad ingresada NO es un numero")
        if cantidad<0:
            raise Exception("La cantidad ingresada debe ser mayor a cero")
        #verificar si el articulo existe
        #si existe, agregar la cantidad indicada
        if arti in self.articulos:
            posicion=self.articulos.index(arti)
            self.cantidades[posicion]=self.cantidades[posicion] + cantidad
        else:#en caso no exista el articulo
            self.articulos.append(arti)
            self.cantidades.append(cantidad)

    def eliminar_articulo(self,arti):
        if not isinstance(arti,Articulo):
            raise Exception("El articulo ingresado NO es un articulo")
        if arti in self.articulos:
            posicion=self.articulos.index(arti)
            del self.articulos[posicion]
            del self.cantidades[posicion]


class manejador:
    def __init__(self):
    self.opcion=-1
    self.lista_articulos=[]
    self.pe=Pedido()

    def menuOpciones(self):
        print("MENU GENERAL DE OPCIONES")
        print("----------------")
        print("(1). ARTICULOS")
        print("(2). PEDIDOS")
        print("(0). SALIR")
        self.opcion=int(input("INGRESE SU OPCION: "))

    def menuOpcionesArticulos(self):
        print("MENU DE OPCIONES ARTICULOS")
        print("---------------------------")
        print("(1). CREAR ARTICULOS")
        print("(2). MOSTRAR ARTICULOS")
        print("(0). REGRESAR")
        print("(4). TERMINAR")

        self.opcion=int(input("INGRESE SU OPCION: "))
        if self.opcion==0:
            self.regresar(3)
        elif self.opcion==1:
            self.crearArticulo()
            self.regresar(1)
        elif self.opcion==2:
            for i in lista_articulos:
                print(i)
            input("Presione una tecla para continuar...")
            self.regresar(1)
        elif self.opcion==4:
            self.salir()

    def menuOpcionesPedidos(self):
        print("MENU DE OPCIONES PEDIDOS")
        print("------------------------")
        print("(1). AÑADIR ARTICULO AL PEDIDO")
        print("(2). ELIMINAR ARTICULO DEL PEDIDO")
        print("(3). MOSTRAR PEDIDO")
        print("(0). REGRESAR")
        print("(4). TERMINAR")
        self.opcion=int(input("INGRESE SU OPCION: "))
        if self.opcion==0:
            self.regresar(3)
        elif self.opcion==1:
            arti,cant=elegir_articulo("agregar")
            pe.añadir_articulo(arti,cant)
            regresar(2)
        elif opcion==2:
            arti=elegir_articulo("eliminar")
            pe.eliminar_articulo(arti)
            regresar(2)
        elif opcion==3:
            #mostramos el pedido y el total del pedido
            print("EL PEDIDO REALIZASO ES:")
            pe.mostrar_pedido()
            print("El total del pedido es: ",pe.total_pedido())
            input("Presione una teclar para continuar...")
            regresar(2)
        elif opcion==4:
            salir()

    def elegir_articulo(self,eleccion):
        j=1
        for i in self.lista_articulos:
            print(j, "." , i.get_nombre())
            j=j+1
        opcion=int(input("ELIJA UN ARTICULO: "))
        art=self.lista_articulos[opcion-1]
        if eleccion=="agregar":
            cantidad=int(input("Ingrese una cantidad:"))
            return art,cantidad
        elif eleccion=="eliminar":
            return art

    def regresar(self,menu): #OOOJOOO
        self.opcion=menu


    def crearArticulo(self):
        codigo=int(input("Ingrese el codigo del articulo: "))
        nombre=input("Ingrese el nombre del articulo: ")
        precio=float(input("Ingrese el precio del articulo: "))
        articulo=Articulo(codigo,nombre,precio)
        lista_articulos.append(articulo)

    def salir(self):
        print("FIN DEL PROGRAMA")
        quit
######################################
menuOpciones()
while(opcion!=0):
    menuOpciones()
    if opcion==1:
        menuOpcionesArticulos()
    elif opcion==2:
        menuOpcionesPedidos()   
    elif opcion==3:
        menuOpciones()
    elif opcion==0:
        salir()

print("Fin del programa")
#menuOpciones()
'''

#creamos los articulos(objetos)
art1=Articulo("A0001","Borrador",1)
art2=Articulo("A0002","Cuaderno",5)
art3=Articulo("A0003","Lapicero",2)
#mostramos los articulos
print(art1)
print(art2)
print(art3)


for i in range(cant):
    print("Ingrese articulo ",i + 1, ":")
    #########
    nom = input("Ingrese nombre del articulo: ")
    #########
    pre=float(input("Ingrese precio del articulo: "))
    #########
    cod=input("Ingrese el codigo del articulo: ")
    art=Articulo(cod,nom,pre)



cant=int(input("INGRESE CANTIDAD DE ARTICULOS"))
for i in range(cant):
    print("Ingrese articulo ",i + 1, ":")







#probamos los get y set
art1.set_nombre("Folder")
print(art1)

#comprobamos el subtotal del articulo
print(art1.calcular_subtotal(3))
print(art2.calcular_subtotal(1))
print(art3.calcular_subtotal(2))
'''
#print("############# PEDIDOS #############")
"""
craer una lista de articulos y una lista de cantidades
HACER UN METODO QUE AÑADA Y OTRO QUE ELIMINE articulos
VERIFICAR SI ES UN ARTICULO Y PRECIO VALUDO SINO DELVOLVER
UNA EXCEPCION
AL ELIMINAR VERIFICAR QUE LO QUE SE DESEA ELIMINAR SEA UN
ARTICULO Y EN BASE A LA POSICION DEL ARTICULO EN LA LISTA
SI EL ARTICULO EXISTE AGREGAR LA CANTIDAD AL ARTICULO YA
EXISTENTE
"""
'''
#los articulos
#lista_articulos=[art1,art2,art3]
#las cantidades
#lista_cantidades=[3,1,2]
#craemos el pedido
#pe=Pedido(lista_articulos,lista_cantidades)
try:
    print("####AÑADIMOS 3 ARTICULOS####")
    #creamos el pedido
    pe=Pedido()
    pe.añadir_articulo(art1,3)
    pe.añadir_articulo(art2,1)
    pe.añadir_articulo(art3,2)
    #mostramos el pedido y el total del pedido
    print("EL PEDIDO REALIZADO ES :")
    pe.mostrar_pedido()
    print("El total de pedidos es: ", pe.total_pedido())

    #eliminamos 1 articulo del peido
    print("####ELMINIAMOS 1 ARTICULO####")
    pe.eliminar_articulo(art1)
    pe.eliminar_articulo(art3)
    print("EL PEDIDO REALIZADO AHORA ES :")
    pe.mostrar_pedido()
    print("El total de pedidos es: ", pe.total_pedido())
except Exception as ex:
    print(ex)


'''