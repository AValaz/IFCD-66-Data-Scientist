## Ejercicio 151

class Libro:
    def __init__(self, titulo, autor, ISBN, ano_publicacion, estado):
    # Atributos de instancia
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.ano_publicacion = ano_publicacion
        self.estado = 'disponible'

    def __str__(self):
        return f"El título del libro es {self.titulo}, su autor es {self.autor} y su ISBN {self.ISBN} mientras que su estado es {self.estado}"
    
    def prestar(self):
        # Accediendo a los atributos de instancia
        if self.estado == 'disponible':
            self.estado == 'prestado'
            return True
        return False
    
    def devolver(self):
        if self.estado == 'prestado':
            self.estado = 'disponible'
            return True
        return False

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados= []

    def pedir_libro(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            return True
        return False
    
    def devolver_libro(self, libro):
        if libro.devolver():
            self.libros_prestados.remove(libro)
            return True
        return False
    
    def __str__(self):
        return f"El usuario es {self.nombre} con ID {self.id_usuario} - Tiene estos libros prestados:  {[libro.titulo for libro in self.__libros_prestados]}"
    
class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros_disponibles = []
        self.__usuarios_registrados = []

    def registrar_libro(self, libro):
        self.__libros_disponibles.append(libro)
    
    def registrar_usuario(self, usuario):
        self.__usuarios_registrados.append(usuario)
    
    def buscar_libro(self, isbn):
        for libro in self.__libros_disponibles:
            if libro.isbn == isbn:
                return libro
        return None
    
    def buscar_usuario(self, id_usuario):
        for usuario in self.__usuarios_registrados:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None
    
    def __str__(self):
        return f"Biblioteca: {self.__nombre}\nLibros disponibles: {[libro.titulo for libro in self.__libros_disponibles]}\nUsuarios registrados: {[usuario.nombre for usuario in self.__usuarios_registrados]}"