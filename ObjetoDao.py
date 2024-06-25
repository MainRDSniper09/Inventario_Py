# Se importa clase CursorDelPool
from CursorDelPool import CursorDelPool
# Se importa clase logger
from logger_base import log
from Objetos import Objetos

class ObjetoDao:

    _SELECCIONAR = 'SELECT * FROM objetos ORDER BY id_producto'
    _INSERTAR = 'INSERT INTO objetos(nombre,descripcion,precio,cantidad) VALUES(%s,%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE objetos SET nombre=%s, descripcion=%s, precio=%s, cantidad=%s WHERE id_producto=%s'
    _ELIMINAR = 'DELETE FROM objetos WHERE id_producto=%s'

    # Metodo seleccionar
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            objetos = []
            for registro in registros:
                objeto = Objetos(registro[0], registro[1], registro[2], registro[3], registro[4])
                objetos.append(objeto)
            return objetos

    # Metodo insertar
    @classmethod
    def insertar(cls,objeto):
        with CursorDelPool() as cursor:
            log.info(
                f'Objeto a ingresar {objeto}')
            valores = (objeto.nombre, objeto.descripcion, objeto.precio, objeto.cantidad)
            cursor.execute(cls._INSERTAR, valores)
            log.info(
                f'Objeto insertado correctamente: {objeto}')
            return cursor.rowcount

    # Metodo actulizar
    @classmethod
    def actualizar(cls, objeto):
        with CursorDelPool() as cursor:
            valores = (objeto.id_produto, objeto.nombre, objeto.descripcion, objeto.precio, objeto.cantidad)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.info(f'Objeto actualizado correctamente: {objeto}')
            return cursor.rowcount

    # Metodo eliminar
    @classmethod
    def eliminar(cls, objeto):
        with CursorDelPool() as cursor:
            valores = (objeto.id_produto,)
            cursor.execute(cls._ELIMINAR, valores)
            log.info(f'Objeto eliminado correctamente {objeto}')
            return cursor.rowcount

# Prueba de nuestra clase
if __name__ == '__main__':
    objetos = ObjetoDao.seleccionar()
    for objeto in objetos:
        log.info(objeto)


