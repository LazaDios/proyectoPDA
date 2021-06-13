
from os import system #Para borrar consola
from funcion_hast import Tablahash
from sys import exit



#Funcion para limpiar Pantalla
def limpiar():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("clr")
        #Funcion para limpiar Pantalla
















# Clase/objeto Articulo, donde contiene sus datos
class Articulo:
    
    #Constructor, asigna las respectivas variables que se pasan con los parametros
    def __init__(self,referencia=None,distribuidora=None,nombre_art=None,cantidad_art=None,precio=None,fecha_salida=None):
        self.referencia = referencia
        self.distribuidora = distribuidora
        self.nombre_art = nombre_art
        self.cantidad_art = cantidad_art
        self.precio = precio
        self.fecha_salida = fecha_salida
    
    # Registra un articulo, continua de la opcion 2 del main.py
    def registrar_articulo(self,referencia):
        #Distribuidora
        self.distribuidora = input('Ingrese la distribuidora: ')
        validar_distribuidora = validar_cadena(self.distribuidora)
        while validar_distribuidora["status"] == False: 
            print(validar_distribuidora["error_message"])
            self.distribuidora = input('Ingrese la distribuidora: ')
            validar_distribuidora = validar_cadena(self.distribuidora)
        #Nombre
        self.nombre_art = input('Ingrese nombre del articulo: ')
        validar_nombre_art = validacionCadenaAlfa(self.nombre_art,30)
        while validar_nombre_art["status"] == False:
            print(validar_nombre_art["error_message"])
            self.nombre_art = input('Ingrese nombre del articulo: ')
            validar_nombre_art = validacionCadenaAlfa(self.nombre_art,30)
        #Cantidad
        self.cantidad_art = input('Ingrese la cantidad del articulo en inventario: ')
        validar_cantidad = validar_entero_positivo(self.cantidad_art)
        while validar_cantidad["status"] == False:
            print(validar_cantidad["error_message"])
            self.cantidad_art = input('Ingrese la cantidad del articulo en inventario: ')
            validar_cantidad = validar_entero_positivo(self.cantidad_art)
        #Precio
        self.precio = input('Ingrese el precio del articulo: ')
        validar_precio = validar_decimal_positivo(self.precio)
        while validar_precio["status"] == False:
            print(validar_precio["error_message"])
            self.precio = input('Ingrese el precio del articulo: ')
            validar_precio = validar_decimal_positivo(self.precio)

        self.referencia = referencia
        
        # inicializamos la fecha
        self.fecha_salida = {"Dia":'0',"Mes":'0',"Año":'0'}
    
    # Registra la fecha de salida de un articulo
    def registrar_fecha_salida(self):
        print('\n\tFecha de salida del articulo\n')
        #Dia
        dia = input('Dia: ')
        validar_dia = validar_numero_entero(dia)
        while validar_dia["status"] == False:
            print(validar_dia["error_message"])
            dia = input('Dia: ')
            validar_dia = validar_numero_entero(dia)
        #Mes
        mes = input('Mes: ')
        validar_mes = validar_numero_entero(mes)
        while validar_mes["status"] == False:
            print(validar_mes["error_message"])
            mes = input('Mes: ')
            validar_mes = validar_numero_entero(mes)
        #Año
        ano = input('Año: ')
        validar_ano = validar_numero_entero(ano)
        while validar_ano["status"] == False:
            print(validar_ano["error_message"])
            ano = input('Año: ')
            validar_ano = validar_numero_entero(ano)
        #Se registra la fecha de salida
        self.fecha_salida = {"Dia":dia,"Mes":mes,"Año":ano}
    
    # Muestra el articulo
    def mostrar_articulo(self):
        print('\n\t..:INFORMACION DEL ARTICULO:..\n')
        print(f'Referencia: {self.referencia}')
        print(f'Distribuidora: {self.distribuidora}')
        print(f'Nombre: {self.nombre_art}')
        print(f'Cantidad en inventario: {self.cantidad_art}')
        print(f'Precio: {self.precio}$')
        print(f'Fecha de salida: {self.fecha_salida["Dia"]}/{self.fecha_salida["Mes"]}/{self.fecha_salida["Año"]}')
    
    # Abre un menu para modificar el articulo
    def modificar_articulo(self):
        print('\n\t..:MODIFICAR ARTICULO:..')
        print('[1]. Modificar referencia')
        print('[2]. Modificar distribuidora')
        print('[3]. Modificar nombre del articulo')
        print('[4]. Modificar precio')
        print('[5]. Modificar cantidad del articulo en inventario')
        print('[6]. Modificar fecha de salida del articulo ')
        opc = input('Digite una opcion: ')
        
        validar_opcion = validar_numero_entero(opc)
        while validar_opcion["status"] == False:
            print(validar_opcion["error_message"])
            opc = input('Digite una opcion: ')
            validar_opcion = validar_numero_entero(opc)
        
        opc = int(opc)
        #Modifica referencia
        if opc == 1:
            referencia = input('Indique la nueva referencia: ')
            validar_referencia = validacionCadenaAlfa(referencia,10)
            while validar_referencia["status"] == False:
                print(validar_referencia["error_message"])
                referencia = input('Indique la nueva referencia: ')
                validar_referencia = validacionCadenaAlfa(referencia,10)
            self.referencia = referencia
        #Modifica distribuidora
        elif opc == 2:
            distribuidora = input('Ingrese la distribuidora: ')
            validar_distribuidora = validar_cadena(distribuidora)
            while validar_distribuidora["status"] == False:
                print(validar_distribuidora["error_message"])
                distribuidora = input('Ingrese la distribuidora: ')
                validar_distribuidora = validar_cadena(distribuidora)
            self.distribuidora = distribuidora
        #Modifica nombre
        elif opc == 3:
            nombre_art = input('Ingrese nombre del articulo: ')
            validar_nombre_art = validacionCadenaAlfa(nombre_art,30)
            while validar_nombre_art["status"] == False:
                print(validar_nombre_art["error_message"])
                nombre_art = input('Ingrese nombre del articulo: ')
                validar_nombre_art = validacionCadenaAlfa(nombre_art,30)
            self.nombre_art = nombre_art
        #Modifica Precio
        elif opc == 4:
            precio = input('Ingrese el precio del articulo: ')
            validar_precio = validar_decimal_positivo(precio)
            while validar_precio["status"] == False:
                print(validar_precio["error_message"])
                precio = input('Ingrese el precio del articulo: ')
                validar_precio = validar_decimal_positivo(precio)
            self.precio = precio
        # Modifica cantidad
        elif opc == 5:
            cantidad_art = input('Ingrese la nueva  cantidad del articulo en inventario: ')
            validar_cantidad = validar_entero_positivo(cantidad_art)
            while validar_cantidad["status"] == False:
                print(validar_cantidad["error_message"])
                cantidad_art = input('Ingrese la nueva cantidad del articulo en inventario: ')
                validar_cantidad = validar_entero_positivo(cantidad_art)
            self.cantidad_art = cantidad_art
        # Modifica la fecha de salida
        elif opc == 6:
            self.registrar_fecha_salida()
        # Ninguna de las anteriores
        else:
            print('\n<--Opcion invalida-->\n')
    






























#****************************************************************************************************************
#validaciones

# Verifica si una cadena solo contiene letras y numeros y que este no se pase del limite de letras
def validacionCadenaAlfa(cadena_alfanumerica,max_tam):
    #Que no se pase del tamaño
    if len(cadena_alfanumerica) <= max_tam and len(cadena_alfanumerica) > 0:
        contador_letra = 0
        contador_numero = 0
        for caracter in cadena_alfanumerica: #Cada caracter de la cadena
            if ord(caracter) > 64 and ord(caracter) < 91 or ord(caracter) > 96 and ord(caracter) < 123: #Letras
                contador_letra+=1
            elif ord(caracter) > 47 and ord(caracter) < 58: #0-9
                contador_numero+=1
            elif caracter == ' ':
                contador_letra+=1
            else:
                return {"error_message":'Error ingrese solo numeros o letras',"status":False}
        
        #Solo cuenta si tiene numeros y letras, si hay un caracter diferente, habran menos letras y numeros de lo que deberia tener
        if contador_letra+contador_numero == len(cadena_alfanumerica): 
            return {"error_message":None,"status":True}
        else:
            return {"error_message":f"Error introduzca denuevo, debe contener solo numeros y letras","status":False}
    else:
        return {"error_message":f"El nombre del articulo o la referencia debe ser menor o igual  a {max_tam} caracteres","status":False}

#Verifica que una cadena solo contenga letras y que este no se pase del limite
def validar_cadena(distribuidora):
    contador_caracteres = 0
    max_tam = 30
    if len(distribuidora)<= max_tam:
        for caracter in distribuidora: #Cada caracter de la cadena
            if ord(caracter) > 64 and ord(caracter) < 91 or ord(caracter) > 96 and ord(caracter)< 123: #Letras
                contador_caracteres+=1
            elif caracter == ' ':
                contador_caracteres+=1
        if contador_caracteres == len(distribuidora):
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"Debe indicar solo letras","status":False}
    else:
        return {"error_message":"El nombre de la distribuidora debe ser menor o igual  a 25 caracteres","status":False}


#Verifica que el valor sea un numero
def validar_numero_entero(numero):
    numero = str(numero)
    valido = False
    for caracter in numero: #Cada caracter de la cadena
        if ord(caracter) > 47 and ord(caracter) < 58: #Cada caracter debe ser de 0 a 9
            valido = True
        else:
            valido = False
    if valido == True:
        return {"error_message":None,"status":True}
    else:
        return {"error_message":"Debe indicar un numero entero","status":False}
        
#Verifica que el valor sea un numero mayor a 0
def validar_entero_positivo(numero):
    try: #Si no lanza una expecion, es un numero
        if int(numero) >= 0: # Debe ser mayor a 0
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"El numero debe ser mayor a cero","status":False}
    except:
        return {"error_message":"Debe indicar un numero entero","status":False}

#Verifica que el valor sea un numero decimal
def validar_numero_decimal(numero):
    try: #Si no lanza una expecion, es un numero decimal
        numero = float(numero)
        return {"error_message":None,"status":True}
    except:
        return {"error_message":"Debe indicar un numero decimal","status":False}

#Verifica que el valor sea un numero decimal mayor a 0
def validar_decimal_positivo(numero):
    try: #Si no lanza una expecion, es un numero decimal
        if float(numero) >= 0: # Debe ser mayor a 0
            return {"error_message":None,"status":True}
        else:
            return {"error_message":"El numero debe ser mayor a cero","status":False}
    except:
        return {"error_message":"Debe indicar un numero decimal","status":False}


#****************************************************************************************************************









def generar_tabla_hash(registros):
    articulos = Tablahash()

    for elemento in registros:
        articulos.agregar(elemento.referencia,elemento) #ciclo para el indice
    return articulos


"""MANIPULACION DEL ARCHIVO.TXT"""
#Se cargan los registros que se encuentran en el archivo .txt
def leerArchi():
    registros = []
    try: # Si no sucede una expecion, se leen las lineas
        for line in open('ARTICULOS.txt','r'): #Cada linea del archivo
            if '*' in line.split(',')[0]: #Verifica que no haya sido eliminado (que tenga * al final)
                continue
            #Divide la linea y se les asigna en los parametros de abajo
            referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida = line.split(',') 
            fecha_salida = fecha_salida.split('/') #La fecha se separa (volviendo un arreglo de string)
            #La fecha se reagrupa indicando dia, mes y año
            fecha_salida = { "Dia":fecha_salida[0] , "Mes":fecha_salida[1], "Año":fecha_salida[2].split('\n')[0]}
            # Se genera el articulo
            articulo = Articulo(referencia,distribuidora,nombre_art,cantidad_art,precio,fecha_salida)
            registros.append(articulo)
    except:
        file = open('ARTICULOS.txt','x')
        file.close()
    
    # Se generan la tabla hash de todos los registros
    articulos = generar_tabla_hash(registros)
    return articulos

#Se actualiza la informacion del archivo, cuando se haga insercion,modificacion o eliminacion de un registro
def actualizar_archivo(infoProductos):
    file = open('ARTICULOS.txt','w')
    for lista in infoProductos.lista: #Para cada elemento del arreglo
        if len(lista) > 0:
            for articulo in lista: #Para cada articulo
                #Escribe en el archivo lo correspodiente
                file.write(
                    
                    articulo[1].referencia+','+articulo[1].distribuidora+','+articulo[1].nombre_art+','+articulo[1].cantidad_art+','+articulo[1].precio+','+articulo[1].fecha_salida["Dia"]+'/'+articulo[1].fecha_salida["Mes"]+'/'+articulo[1].fecha_salida["Año"]+'\n'
                )
        
    file.close()
    infoProductos = leerArchi() #sera igual a lo que tengamos guardado
    return infoProductos


 ########## Cada funcion que determina los procesos de menu ################################
# Opcion 6: se listan los registros que tengan una fecha del 2020
def listar_vendidos_fecha(fecha,infoProductos):
    for lista in infoProductos.lista:
        if len(lista) > 0:
            for articulo in lista:
                if int(articulo[1].fecha_salida["Año"]) == fecha:
                    articulo[1].mostrar_articulo()
    input('\nPresione enter para volver al menu')

# Opcion 5: se listan los articulos que tienen una cantidad en inventario mayor a 0
def listar_articulos_disponibles(infoProductos):
    for lista in infoProductos.lista:
        if len(lista) > 0:
            for articulo in lista:
                if int(articulo[1].cantidad_art) > 0:
                    articulo[1].mostrar_articulo()
    input('\nPresione enter para volver al menu.')

# Opcion 3: Modifica un registro
# NOTA: Aqui solo se busca la referencia, las modificaciones se realizan en articulo.py
def modificar_articulo(infoProductos):
    referencia = input('Indique referencia del articulo a modificar: ')
    validar_referencia = validacionCadenaAlfa(referencia,10)
    while validar_referencia["status"] == False:
        print(validar_referencia["error_message"])
        referencia = input('Indique referencia del articulo a modificar: ')
        validar_referencia = validacionCadenaAlfa(referencia,10)

    if infoProductos.busqueda(referencia) != False:  
        articulo_indice = infoProductos.busqueda(referencia)[1]
        infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].modificar_articulo() #Continua en articulo.py
        actualizar_archivo(infoProductos)
        input('Presione enter para volver al inicio')

    else:
        print('\n<--Articulo no encontrado-->\n')
        input('Presione enter para volver al inicio')

# Opcion 4: Se modifica la cantidad de existencia de un articulo en el inventario
def registrar_venta_compra_articulo(infoProductos):
    referencia = input('Indique la referencia del articulo: ') #Se toma la referencia del articulo
    tipo_modificacion = None
    if infoProductos.busqueda(referencia) != False: #Se busca el articulo dentro del arreglo
        print('\n1. Compra')  #Opciones para saber si se sumara o restara de la cantidad de existencia
        print('2. Venta\n')
        tipo_modificacion = input('\nDigite una opcion: ')
        validar_entrada_cadena = validar_numero_entero(tipo_modificacion) #se valida que sea un numero el que introduzca el usuario
        while validar_entrada_cadena["status"] == False: #mientras no sea un numero se repetira
            print(validar_entrada_cadena["error_message"])
            tipo_modificacion = input('\nDigite una opcion: ')
            validar_entrada_cadena = validar_numero_entero(tipo_modificacion)
        
        tipo_modificacion = int(tipo_modificacion)
        articulo_indice = infoProductos.busqueda(referencia)[1] #se toma el indice donde se encuentra el registro dentro del arreglo
        infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].mostrar_articulo() #mostrando los datos del articulo
        cantidad_art = input('\nIngrese la cantidad de articulos: ')
        
        validar_cantidad_art = validar_numero_entero(cantidad_art)
        while validar_cantidad_art["status"] == False: #mientras no sea un numero entero se repetira
            print(validar_cantidad_art["error_message"])
            cantidad_art = input('\nIngrese la cantidad de articulos: ')
            validar_cantidad_art = validar_numero_entero(cantidad_art)
        
        cant_actual = int(infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].cantidad_art) #se toma la cantidad actual del registro
        cantidad_art = int(cantidad_art) #cantidad que se añadira
        
        if tipo_modificacion == 1: #validar si es suma o resta lo que se realizara
            nueva_cantidad = cantidad_art+cant_actual
        else:
            if cant_actual < cantidad_art: #se debe vender una cantidad menor a la que esta en existencia
                input('No puedes vender mas de lo que tienes, presiona enter pasa salir')
                return 0
            nueva_cantidad = cant_actual-cantidad_art
            infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].registrar_fecha_salida()
        nueva_cantidad = str(nueva_cantidad) #se convierte a string para guardarse en el archivo
        infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].cantidad_art = nueva_cantidad #se le añade la nueva cantidad al registro
        actualizar_archivo(infoProductos) # seactualiza el archivo y el arreglo

    else:
        input('<--El articulo no esta registrado, pulse enter para volver al inicio-->')

# Opcion 7: se elimina un registro del arreglo y se marca con un * en el archivo de datos
def eliminar_articulo(infoProductos):
    referencia = input('Indique la referencia del articulo: ')
    if infoProductos.busqueda(referencia) != False: #El articulo debe existir
        articulo_indice = infoProductos.busqueda(referencia)[1]
        infoProductos.lista[articulo_indice[0]][articulo_indice[1]][1].referencia+='*' #la referencia se marca con *
        actualizar_archivo(infoProductos)
        print('Articulo eliminado exitosamente')
    else:
        print('No existe el articulo')
    input('<--pulse enter para volver al inicio-->')

# Opcion 2: agregar un registro al arreglo y al archivo de datos.
def agregar_articulo(infoProductos):
    referencia = input('Ingrese la referencia: ')
    validar_referencia = validacionCadenaAlfa(referencia,10)
    while validar_referencia["status"] == False:
        print(validar_referencia["error_message"])
        referencia = input('Ingrese la referencia: ')
        validar_referencia = validacionCadenaAlfa(referencia,10)
    if infoProductos.busqueda(referencia):
        print('\n<--Ya se encuentra registrado-->')
        input('\nPresione enter para volver al inicio')
    else:
        articulo = Articulo()
        articulo.registrar_articulo(referencia) #Continua en articulo.py
        file = open('ARTICULOS.txt','a')
        file.write(
            articulo.referencia+','+articulo.distribuidora+','+articulo.nombre_art+','+articulo.cantidad_art+','+articulo.precio+','+articulo.fecha_salida["Dia"]+'/'+articulo.fecha_salida["Mes"]+'/'+articulo.fecha_salida["Año"]+'\n'
        )
        file.close()
        infoProductos.agregar(articulo.referencia,articulo)

# Opcion 1: buscar y mostrar informacion sobre un articulo
def consultar_articulo(infoProductos):
    referencia = input('\nIngrese la referencia: ') #se toma la referencia
    validar_referencia = validacionCadenaAlfa(referencia,10)
    while validar_referencia["status"] == False:
        print('\n'+validar_referencia["error_message"]+'\n')
        referencia = input('Ingrese la referencia: ')
        validar_referencia = validacionCadenaAlfa(referencia,10)
    if infoProductos.busqueda(referencia): #se valida que el registro exista
        articulo = infoProductos.busqueda(referencia) #si existe se musetra
        articulo,articulo_posicion = articulo[0],articulo[1]
        articulo.mostrar_articulo()
        input('\n\t<--Presione enter para volver al menu-->')
    else:
        input('\n\tEl articulo no existe, <--Presiona una tecla para volver al menu-->')

#menu de opciones
def menu(infoProductos):
    opc = None 
    while opc != 8:
        infoProductos = actualizar_archivo(infoProductos) #el archivo es actualizado y el arreglo cada vez que se muestra el menu
        print('***** SELECCIONE UNA OPCION *****') 
        print('***** 1- Agregar articulo   *****')
        print('***** 2- Consultar articulo *****')
        print('***** 3- Editar  articulo   *****')
        print('** 4-Compra o venta de articulo**')
        print('***** 5- Mostrar articulo   *****')
        print('*** 6-Articulos vendidos en 2020*')
        print('***** 7- Eliminar articulo  *****')
        print('***** 8- Salir del programa *****')
        opc = input('\nIngrese una opcion: ')
       
        
        try: #Execion 
            opc = int(opc)
        except:
            print('\n<--Error ingrese solo numeros-->\n')
            opc = input('Ingrese una opcion: ')
        system("clr")
        if opc == 1: #Consulta
            
            agregar_articulo(infoProductos)
            
            
        elif opc == 2: #Agregar
            consultar_articulo(infoProductos)
            

        elif opc == 3: #Modificar
            modificar_articulo(infoProductos)
            

        elif opc == 4: #Compra/Venta
            registrar_venta_compra_articulo(infoProductos)
            

        elif opc == 5: #Listar
            listar_articulos_disponibles(infoProductos)
            system("cls")

        elif opc == 6: #Listar vendidos 2020
            listar_vendidos_fecha(2020,infoProductos)
            

        elif opc == 7: # Eliminar
            eliminar_articulo(infoProductos)
            
        elif opc == 8: # Salir
            exit()


def ejecutar():
    #Campos en el Txt , lectura principal
    infoProductos = leerArchi() 
    menu(infoProductos)

ejecutar()