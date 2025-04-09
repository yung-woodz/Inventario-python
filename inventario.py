class Admin:
    def __init__(self, nombre, apellidos, username, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.username = username
        self.password = password
        
        with open('Admin.txt', 'w') as fichero:
            fichero.write(f"{self.nombre} {self.apellidos} {self.username} {self.password}")

    @staticmethod
    def verificarLogin(username, password):
        with open('Admin.txt', 'r') as fichero:
            lines = fichero.readlines()
            
            for line in lines:
                userData = line.strip().split()

                if len(userData) == 5:
                    savedUsername = userData[-2]
                    savedPassword = userData[-1]
            
                    if username == savedUsername and password == savedPassword:
                        return True
                    
            return False
            
class Users:
    def __init__(self, nombre, apellidos, username, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.username = username
        self.password = password

        with open('Users.txt', 'a') as fichero:
            fichero.write(f"{self.nombre} {self.apellidos} {self.username} {self.password}")

    @staticmethod
    def verificarLogin(username, password):
        with open('Users.txt', 'r') as fichero:
            lines = fichero.readlines()
            
            for line in lines:
                userData = line.strip().split()

                if len(userData) == 5:
                    savedUsername = userData[-2]
                    savedPassword = userData[-1]
            
                    if username == savedUsername and password == savedPassword:
                        return True
                    
            return False


def main():
    print("### Sistema de Login ###")
    choice = input("Deseas registrarte? (s/n): ").lower()

    if choice == "s":
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        username = input("Usuario: ")
        password = input("Contraseña: ")

        Users(nombre, apellidos, username, password)

        print("Registro exitoso!!")

    print("\n### Iniciar sesion ###")
    login_username = input("Usuario: ")
    login_password = input("Contraseña: ")

    if Users.verificarLogin(login_username, login_password):
        print("Login iniciado")
    else:
        print("Datos incorrectos")


if __name__ == "__main__":
    main()


