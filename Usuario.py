from logger_base import log

# Clase usuario
class Usuario:
    def __init__(self,username = None, password = None):
        self._username = username
        self._password = password

    # Metodo str
    def __str__(self):
        return f'''
            Usuario: {self._username}, Password: {self._password}
        '''

    # Getters and Setters
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self,username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self,password):
        self._password = password

# Prueba objeto Usuario
if __name__ == '__main__':
    admin = Usuario('Nicolas','1234')
    log.info(admin)