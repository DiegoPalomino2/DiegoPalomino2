import math
from itertools import combinations


print("\n")
print(" " * 15, "┌─────────────────────────────────────────────────────────────────────────────────────┐")
print(" " * 15, "│                         Universidad Nacional de Ingeniería                          │")
print(" " * 15, "├─────────────────────────────────────────────────────────────────────────────────────┤")
print(" " * 15, "│                   Facultad de Ingeniería Industrial y de Sistemas                   │")
print(" " * 15, "├─────────────────────────────────────────────────────────────────────────────────────┤")
print(" " * 15, "│     Programa para hallar la ruta óptima mediante el uso del algoritmo de KRUSKAL    │")
print(" " * 15, "│                     en el recorrido de Iglesias en Ayacucho                         │")
print(" " * 15, "├─────────────────────────────────────────────────────────────────────────────────────┤")
print(" " * 15, "│   Realizado por: AÑACATA HERRERA GEORGE MARLOG                                      │")
print(" " * 15, "│                  APARICIO SASARI LUIS ANGEL                                         │")
print(" " * 15, "│                  NINA LABRA JARRISON                                                │")
print(" " * 15, "│                  PALOMINO MALVARTE DIEGO EDUARDO                                    │")
print(" " * 15, "│                  TORRES CRUZ YOMIRA FIORELA                                         │")
print(" " * 15, "└─────────────────────────────────────────────────────────────────────────────────────┘")


# Matriz con los datos de latitud y longitud de las 33 iglesias
lugares = [
    [1,"La Catedral",-13.16071857,-74.2251317],
    [2,"San Cristobal",-13.16801777,-74.22743725],
    [3,"La Merced",-13.16227475,-74.22562587],
    [4,"Santo Domingo",-13.15813713,-74.2258763],
    [5,"San Juan de Dios",-13.16411161,-74.22757525],
    [6,"San Francisco",-13.16279174,-74.22713251],
    [7,"Santa Clara",-13.1628912,-74.2282462],
    [8,"Santa Ana",-13.1703543,-74.23091165],
    [9,"Santa Maria Magdalena",-13.15787908,-74.22137586],
    [10,"La Compañia de Jesús",-13.16130163,-74.22668106],
    [11,"Nuestra Señora de Loreto",-13.16123372,-74.22669716],
    [12,"San Agustin",-13.15988546,-74.22494016],
    [13,"San Sebastián",-13.16339812,-74.22004163],
    [14,"Belen",-13.16438187,-74.231033],
    [15,"Santa Teresa",-13.1677331,-74.2278656],
    [16,"San Francisco de Paula",-13.15937681,-74.22723192],
    [17,"La Buena Muerte",-13.16141414,-74.22411405],
    [18,"La Amargura",-13.16085336,-74.22068211],
    [19,"Carmen Alto",-13.17590908,-74.22643954],
    [20,"Pampa San Agustin",-13.16248912,-74.22332577],
    [21,"San Juan Bautista",-13.16638356,-74.22338681],
    [22,"Templo del Soquiaqato",-13.16147879,-74.22951573],
    [23,"Conchopata",-13.16294797,-74.21743581],
    [24,"El Calvario",-13.15770799,-74.22937546],
    [25,"Nuestra Señora del Pilar",-13.1542503,-74.22505063],
    [26,"Capilla del Cementerio",-13.16762439,-74.21108161],
    [27,"Señor de Quinuapata",-13.16605285,-74.23388517],
    [28,"Capillapata",-13.16640429,-74.21827461],
    [29,"Señor de Arequipa",-13.16762021,-74.21278679],
    [30,"Virgen del Rosario de Chiquinquirá",-13.15585527,-74.22535279],
    [31,"Virgen de Fátima",-13.15853625,-74.2254974],
    [32,"Señor de Maravillas",-13.15053521,-74.22755724],
    [33,"Señor de Pampa Cruz",-13.16453149,-74.22529166],
]
print("\n******************************************************************\n")
# Pedir al usuario cuántos iglesias va a visitar
n = int(input("\n¿Cuántos Iglesias deseas recorrer? = "))

# Crear una lista para almacenar los números de las iglesias a visitar
lugares_a_visitar = []

print("\n******************************************************************\n")

print("\t\tNombres de las 33 Iglesias ")
print("------------------------------------------------------------------")
print("        1- La Catedral")
print("        2- San Cristobal")
print("        3- La Merced")
print("        4- Santo Domingo")
print("        5- San Juan de Dios")
print("        6- San Francisco")
print("        7- Santa Clara")
print("        8- Santa Ana")
print("        9- Santa Maria Magdalena")
print("        10-La Compañia de Jesús")
print("        11-Nuestra Señora de Loreto")
print("        12-San Agustin")
print("        13-San Sebastián")
print("        14-Belen")
print("        15-Santa Teresa")
print("        16-San Francisco de Paula")
print("        17-La Buena Muerte")
print("        18-La Amargura")
print("        19-Carmen Alto")
print("        20-Pampa San Agustin")
print("        21-San Juan Bautista")
print("        22-Templo del Soquiaqato")
print("        23-Conchopata")
print("        24-El Calvario")
print("        25-Nuestra Señora del Pilar")
print("        26-Capilla del Cementerio")
print("        27-Señor de Quinuapata")
print("        28-Capillapata")
print("        29-Señor de Arequipa")
print("        30-Virgen del Rosario de Chiquinquirá")
print("        31-Virgen de Fátima")
print("        32-Señor de Maravillas")
print("        33-Señor de Pampa Cruz")
print("\n******************************************************************\n")

# Pedir al usuario las iglesias a visitar
for i in range(n):
    lugar_num = int(input(f"Ingrese el número de la Iglesia {i + 1} a visitar : "))
    lugares_a_visitar.append(lugar_num)
print("\n******************************************************************\n")

# Crear la matriz nx4 con los datos de las iglesias seleccionados y la lista con los nombres de las iglesias
matriz_visitas = [lugar for lugar in lugares if lugar[0] in lugares_a_visitar]
nomlugares_a_visitar = [fila[1] for fila in lugares if fila[0] in lugares_a_visitar]

# Mostrar la lista de las iglesias a visitar 
print("\nIglesias a visitar :", nomlugares_a_visitar)
print("\n******************************************************************\n")

# Crear un diccionario con los datos de la latitud y longitud de las iglesias seleccionadas
locations = {
    row[0]: (row[2], row[3]) for row in matriz_visitas
}
output = ""
for row in matriz_visitas:
    output += f"{row[0]}: ({row[2]}, {row[3]}),  # {row[1]}\n"



#CALCULO DE LA DISTANCIA MINIMA

# Radio de la Tierra en kilómetros
R = 6371.0

# Lista de aristas (distancia entre cada par de lugares)
edges = []
aristas = []

# Calculando las distancias entre todos los pares
for (place1, coord1), (place2, coord2) in combinations(locations.items(), 2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    
    # Convertir a radianes
    lat1_rad, lon1_rad = math.radians(lat1), math.radians(lon1)
    lat2_rad, lon2_rad = math.radians(lat2), math.radians(lon2)
    
    # Diferencias
    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad
    
    # Usar la Fórmula de Haversine para calcular las distancias
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distancia en kilómetros
    
    # Guardar arista como (distancia, lugar1, lugar2)
    edges.append((distance, place1, place2))
    aristas.append((place1, place2))


# Algoritmo de Kruskal
# Ordenar las aristas por peso (distancia)
edges.sort(key=lambda x: x[0])

# Inicialización del conjunto de nodos y estructura Union-Find
parent = {place: place for place in locations}
rank = {place: 0 for place in locations}

# Funciones para Union-Find
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1, root2 = find(node1), find(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

# Encontrar el AEM
mst_weight = 0
mst_edges = []

for edge in edges:
    weight, place1, place2 = edge
    if find(place1) != find(place2):
        union(place1, place2)
        mst_weight += weight
        mst_edges.append(edge)
mst_weight, mst_edges

# Extraer solo los dos últimos elementos de cada tupla
nodoaristas = [(x[1], x[2]) for x in mst_edges]


print("\nDistancia minima recorrida (en km):", mst_weight)
print("\nAristas del recorrido para las ",n, "Iglesias:", nodoaristas)
