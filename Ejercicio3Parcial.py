from collections import deque


class Mision:
    def __init__(self, planeta, objetivo, recompensa):
        self.planeta = planeta
        self.objetivo = objetivo
        self.recompensa = recompensa


# Pila de la bitácora de Boba Fett
pila_bitacora = deque()

# Funciones para resolver las actividades

# a. Mostrar los planetas visitados en el orden en que realizó las misiones


def mostrar_planetas_visitados(pila):
    planetas = []
    for mision in pila:
        planetas.append(mision.planeta)
    return planetas

# b. Determinar cuántos créditos galácticos recaudó en total


def calcular_creditos_recaudados(pila):
    total_creditos = 0
    for mision in pila:
        total_creditos += mision.recompensa
    return total_creditos

# c. Determinar el número de la misión en la que capturó a Han Solo y en qué planeta fue


def buscar_mision_han_solo(pila, objetivo):
    num_mision = 1
    for mision in pila:
        if mision.objetivo == objetivo:
            return num_mision, mision.planeta
        num_mision += 1
    return None, None


# Ejemplo de carga de la bitácora con misiones
pila_bitacora.append(Mision("Tatooine", "Bounty1", 100))
pila_bitacora.append(Mision("Hoth", "Bounty2", 200))
pila_bitacora.append(Mision("Endor", "Han Solo", 500))
pila_bitacora.append(Mision("Bespin", "Bounty3", 300))

# Resolver las actividades

# a. Mostrar los planetas visitados en el orden en que realizó las misiones
planetas_visitados = mostrar_planetas_visitados(pila_bitacora)
print("Planetas visitados:", planetas_visitados)

# b. Determinar cuántos créditos galácticos recaudó en total
total_creditos = calcular_creditos_recaudados(pila_bitacora)
print("Créditos galácticos recaudados:", total_creditos)

# c. Determinar el número de la misión en la que capturó a Han Solo y en qué planeta fue
num_mision_han_solo, planeta_han_solo = buscar_mision_han_solo(
    pila_bitacora, "Han Solo")
if num_mision_han_solo:
    print("Han Solo fue capturado en la misión número",
          num_mision_han_solo, "en el planeta", planeta_han_solo)
else:
    print("Han Solo no fue capturado en ninguna misión.")
