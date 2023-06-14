from collections import deque

# Crear una pila de superhéroes
pila_superheroes = []


class Superheroe:
    def __init__(self, nombre_superheroe, nombre_personaje, grupo, anio_aparicion):
        self.nombre_superheroe = nombre_superheroe
        self.nombre_personaje = nombre_personaje
        self.grupo = grupo
        self.anio_aparicion = anio_aparicion

# Función para determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje


def buscar_capitana_marvel(lista):
    for superheroe in lista:
        if superheroe.nombre_superheroe == "Capitana Marvel":
            return superheroe.nombre_personaje
    return "No se encontró a Capitana Marvel en la lista"

# Función para almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola


def superheroes_guardianes_galaxia(lista):
    cola_guardianes = deque()
    for superheroe in lista:
        if superheroe.grupo == "Guardianes de la galaxia":
            cola_guardianes.append(superheroe)
    return cola_guardianes, len(cola_guardianes)

# Función para mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"


def mostrar_superheroes_grupo_descendente(lista, grupo1, grupo2):
    superheroes_grupo = []
    for superheroe in lista:
        if superheroe.grupo == grupo1 or superheroe.grupo == grupo2:
            superheroes_grupo.append(superheroe)
    superheroes_grupo.sort(key=lambda x: x.nombre_superheroe, reverse=True)
    for superheroe in superheroes_grupo:
        print(superheroe.nombre_superheroe)

# Función para listar los superhéroes cuyo nombre de personaje tiene un año de aparición posterior a 1960


def listar_superheroes_posterior_a_1960(lista):
    for superheroe in lista:
        if superheroe.nombre_personaje and superheroe.anio_aparicion > 1960:
            print(superheroe.nombre_superheroe)

# Función para corregir el nombre del superhéroe "Black Widow"


def corregir_nombre_superheroe(lista, superheroe_actual, nuevo_nombre):
    for superheroe in lista:
        if superheroe.nombre_superheroe == superheroe_actual:
            superheroe.nombre_superheroe = nuevo_nombre
            superheroe.nombre_personaje = nuevo_nombre

# Función para agregar personajes de una lista auxiliar a la lista principal, si no están cargados


def agregar_personajes(lista_principal, lista_auxiliar):
    for personaje in lista_auxiliar:
        if personaje not in lista_principal:
            lista_principal.append(personaje)

# Función para mostrar todos los personajes que comienzan con C, P o S


def mostrar_personajes_letras(lista):
    letras_permitidas = ["C", "P", "S"]
    for superheroe in lista:
        if superheroe.nombre_personaje and superheroe.nombre_personaje[0] in letras_permitidas:
            print(superheroe.nombre_personaje)


# Resolver las tareas
# h. Cargar al menos 20 superhéroes a la lista (El punto h  lo tuve que poner aca porque no encontre forma de dejarlo al final)
pila_superheroes.append(Superheroe(
    "Spider-Man", "Peter Parker", "Avengers", 1962))
pila_superheroes.append(Superheroe(
    "Captain America", "Steve Rogers", "Avengers", 1941))
pila_superheroes.append(Superheroe("Thor", "", "Avengers", 1962))
pila_superheroes.append(Superheroe(
    "Vlanck Widow", "Natasha Romanoff", "Avengers", 1964))
pila_superheroes.append(Superheroe(
    "Hawkeye", "Clint Barton", "Avengers", 1964))
pila_superheroes.append(Superheroe(
    "Black Panther", "T'Challa", "Avengers", 1966))
pila_superheroes.append(Superheroe("Doctor Strange", "", "", 1963))
pila_superheroes.append(Superheroe("Ant-Man", "Scott Lang", "Avengers", 1962))
pila_superheroes.append(Superheroe("Wasp", "Hope van Dyne", "Avengers", 1963))
pila_superheroes.append(Superheroe("Vision", "", "Avengers", 1968))
pila_superheroes.append(Superheroe(
    "Scarlet Witch", "Wanda Maximoff", "Avengers", 1964))
pila_superheroes.append(Superheroe("Falcon", "Sam Wilson", "Avengers", 1969))
pila_superheroes.append(Superheroe(
    "War Machine", "James Rhodes", "Avengers", 1979))
pila_superheroes.append(Superheroe(
    "Winter Soldier", "Bucky Barnes", "Avengers", 2005))
pila_superheroes.append(Superheroe(
    "Captain Marvel", "Carol Danvers", "", 1968))
pila_superheroes.append(Superheroe(
    "Groot", "", "Guardianes de la galaxia", 1960))
pila_superheroes.append(Superheroe(
    "Gamora", "", "Guardianes de la galaxia", 1975))
pila_superheroes.append(Superheroe(
    "Drax the Destroyer", "", "Guardianes de la galaxia", 1973))
pila_superheroes.append(Superheroe(
    "Rocket Raccoon", "", "Guardianes de la galaxia", 2008))
pila_superheroes.append(Superheroe(
    "Star-Lord", "Peter Quill", "Guardianes de la galaxia", 1976))
pila_superheroes.append(Superheroe(
    "Blanck Widow", "Natasha Romanoff", "Avengers", 1964))

# a. Determinar si "Capitana Marvel" está en la lista y mostrar su nombre de personaje
nombre_personaje_capitana_marvel = buscar_capitana_marvel(pila_superheroes)
print("Nombre de personaje de Capitana Marvel:",
      nombre_personaje_capitana_marvel)

# b. Almacenar los superhéroes que pertenezcan al grupo "Guardianes de la galaxia" en una cola e indicar cuántos son
cola_guardianes_galaxia, cantidad_guardianes_galaxia = superheroes_guardianes_galaxia(
    pila_superheroes)
print("Superhéroes del grupo Guardianes de la galaxia:",
      cantidad_guardianes_galaxia)

# c. Mostrar de manera descendente los superhéroes que pertenecen al grupo "Los cuatro fantásticos" y "Guardianes de la galaxia"
print("Grupo descendente")
mostrar_superheroes_grupo_descendente(
    pila_superheroes, "Los cuatro fantásticos", "Guardianes de la galaxia")

# d. Listar los superhéroes cuyo nombre de personaje tiene un año de aparición posterior a 1960
print("Superheroes post 1960")
listar_superheroes_posterior_a_1960(pila_superheroes)

# e. Corregir el nombre del superhéroe "Black Widow" a "Natasha Romanoff"
print("Nombre corregido:")
corregir_nombre_superheroe(pila_superheroes, "Vlanck Widow", "Black Widow")

# Mostrar el nombre corregido
for superheroe in pila_superheroes:
    if superheroe.nombre_superheroe == "Black Widow":
        print(superheroe.nombre_superheroe)
        break

# f. Agregar personajes de una lista auxiliar a la lista principal, si no están cargados
lista_auxiliar = [
    Superheroe("Black Cat", "Felicia Hardy", "", 1979),
    Superheroe("Hulk", "", "Avengers", 1962),
    Superheroe("Rocket Racoonn", "", "Guardianes de la galaxia", 1976),
    Superheroe("Loki", "", "Avengers", 1962)]

agregar_personajes(pila_superheroes, lista_auxiliar)

# g. Mostrar todos los personajes cuyo nombre comienza con C, P o S
print("Personajes cuyo nombre comienza con C, P o S")
mostrar_personajes_letras(pila_superheroes)
