# Artificial Intelligence
from cities import *
from queue import PriorityQueue
from graphs import *

connected_cities = get_connected_cities()


# Maria Aragão - 18545


# Verify if the city exists on graph
def verifyCityGraph(city):
    if not city in connected_cities.keys():
        print("Coloque uma cidade válida dentro destas apresentadas: " + ",".join(connected_cities))
        return False
    else:
        return True


# Verify if is a number
def verifyNumber(number):
    if not number.isnumeric():
        print("Coloque um numero válido")
        return False
    else:
        return True


def menu_a_star():
    origin = input('Please enter the origin location: ')
    print('Destination location: Faro')
    destination = 'Faro'
    pass


def menu_sophrega_search():
    pass


def menu_uniform_cost(origin, destination):
    strRoot = origin
    goal = destination
    root = globals()[strRoot]
    Procura(root, goal)

def Procura(root, goal):
    queue = PriorityQueue()
    queue.put((0, [root]))
    while not queue.empty():
        pair = queue.get()
        current = pair[1][-1]
        if current.label == goal:
            print(pair[1])
            return pair[1]
        for edge in current.children:
            new_path = list(pair[1])
            new_path.append(edge.destination)
            queue.put((pair[0] + edge.cost, new_path))
pass


def depth_limited(graph, source_city, destination_city, level_limit):
    border = []  # cities that does border with city that we are iterating
    actual_level = 0  # Level in the graph
    border.append(
        {"source_city": source_city, "actual_level": actual_level}
    )
    visited = []  # Cities already visited

    if (int(level_limit) == 0):
        print("\n")
        print("*" * 150)
        print("\nLimite é de 0 cidades para percorrer")
        return

    i = 1
    print('Cidade inicial escolhida: ' + source_city)
    while True:
        print('Iteração - ', i)
        actual_node = border.pop(0)  # Removes first element of the list

        visited.append(actual_node)  # Add to visited cities
        print('Estou em ' + actual_node['source_city'] + ' sendo a cidade percorrida número ' + str(
            actual_node['actual_level'] + 1) + '. Limite ' + str(
            actual_node['actual_level']) + '.')  # printa o no atual

        # Destination found
        if actual_node['source_city'] == destination_city:
            print('*' * 150)
            print('Chegamos a ' + destination_city + ' sendo a cidade percorrida número ' + str(
                actual_node['actual_level'] + 1) + '. Limite ' + str(actual_node['actual_level']) + '.')
            print('Locais Explorados: ')
            print(visited)
            print('Total de iterações: ', i)
            return
        else:
            print('Nó escolhido para abrir ' + actual_node['source_city'])

        f = 0
        for node in graph[actual_node['source_city']]:
            # If city is not visited and is not upper that our level limit on graph
            if not any(x['source_city'] == node for x in visited) and actual_node['actual_level'] + 1 <= int(
                    level_limit):
                border.insert(f,
                              {"source_city": node, "actual_level": actual_node['actual_level'] + 1}
                              )
                f = f + 1

        print('-' * 150)
        print('Na lista para visitar --> ', border)
        print('Na lista já visitado --> ', visited)

        # No more options to iterate
        if (len(border) == 0):
            print("\n")
            print("*" * 150)
            print("\nNão foi encontrado itenerário dentro do limite máximo de cidades a percorrer.\n")
            return

        i = i + 1


def Menu():
    while True:
        print()
        print("Welcome", end="")
        print("=" * 10)

        verifyCity = False
        while verifyCity == False:
            destination = input('\nInsira a cidade de destino: ')
            verifyCity = verifyCityGraph(destination)
        verifyCity = False
        while verifyCity == False:
            origin = input('\nInsira a cidade de origem:  ')
            verifyCity = verifyCityGraph(destination)

        print('1 -------------------- Profundidade Limitada')
        print('2 -------------------- Custo uniforme')
        print('3 -------------------- Procura sôfrega(Destino: Faro)')
        print('4 -------------------- A*(Destino: Faro)')

        method = input('Please choose the searching method: ')

        if method == '1':
            verifyNumberVar = False
            while verifyNumberVar == False:
                level_limit = input('\nInsira o limite máximo de cidades a percorrer:  ')
                verifyNumberVar = verifyNumber(level_limit)
            depth_limited(connected_cities, origin, destination, level_limit)
        elif method == '2':
            # Implementar Joaquim
            menu_uniform_cost(origin, destination)
        elif method == '3':
            # Implementação: Maria Eduarda
            menu_a_star()


Menu()
