from logger_base import log

# Creacion clase objetos
class Objetos:
    def __init__(self, id_producto = None, nombre = None, descripcion = None, precio = None, cantidad = None):
        self._id_producto = id_producto
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._cantidad = cantidad

# Metodo Str
    def __str__(self):
        return f'''
            ID producto: {self._id_producto}, Nombre: {self._nombre}, 
            Descripcion: {self._descripcion}, Precio: {self._precio},
            Cantidad: {self._cantidad}
        '''

# Getters and Setters
    @property
    def id_producto(self):
        return self._id_producto
    @id_producto.setter
    def id_producto(self,id_producto):
        self._id_producto = id_producto

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self,descripcion):
        self._descripcion = descripcion

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad

# Prueba crear un Objeto
if __name__ == '__main__':
    objetoUno = Objetos(1,'Clorox','Limpiado multiusos',20000.0,5)
    log.info(objetoUno)