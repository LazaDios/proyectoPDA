#Metodo hash 
class Tablahash:
    
    #Metodo constructor 
    def __init__(self):
        self.tamano = 500
        self.lista = [
            [] for i in range(self.tamano) #Utilizamos una matriz , llenamos automaticamente con un ciclo
            ]

    #Obtener el indice
    def Hash(self,idx):
        indice = 0
        for letras in idx:
            indice += ord(letras)#ord , para obtener ASCII
        return indice % self.tamano

    #Agregando el elemento a la lista luego de generar el indice con la tecnica de hash    
    def agregar(self,idx,nuevoV):
        indice = self.Hash(idx)
        enc = False
        for elemento in self.lista[indice]:
            if elemento[0] == idx:
                enc  = True
        if not enc:
            self.lista[indice].append([idx,nuevoV])
        else:
            return enc         

    #Buscar un elemento con la clave(idx) proporcionada
    def busqueda(self,idx):
        indice = self.Hash(idx)
        enc = False
        for i,elemento in enumerate(self.lista[indice]):
            if (elemento[0] == idx):
                return elemento[1],(indice,i)
                enc = True
            else:
                enc = False
        return enc
    #Borrar un elemento con la clave proporcionada
    def borrar_elemento(self,idx):
        indice = self.Hash(idx)
        for i,elemento in enumerate(self.lista[indice]):
            if elemento[0] == idx:
                del self.lista[indice][i]

