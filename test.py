from logger_base import log
from Objetos import Objetos
from ObjetoDao import ObjetoDao

print('Bienvenido a nuestra aplicacion'.center(50,'+'))
while True:
    print('''
    Ingrese alguna de las opciones disponibles:
    1. Listar todos los objetos existentes
    2. Insertar un objeto nuevo
    ''')
    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        objetos = ObjetoDao.seleccionar()
        for objeto in objetos:
            log.info(objeto)

    if opcion == 2:
        nombre = input('Ingrese el nombre del producto: ')
        descripcion = input('Ingrese la descripcion del producto: ')
        precio = float(input('Ingrese el precio del producto: '))
        cantidad = int(input('Ingrese el stock del producto: '))
        objeto = Objetos(nombre=nombre, descripcion=descripcion, precio=precio, cantidad=cantidad)
        registros_insertados = ObjetoDao.insertar(objeto)


