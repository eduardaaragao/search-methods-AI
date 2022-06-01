# Artificial Intelligence
from cities import *
from queue import PriorityQueue

connected_cities = get_connected_cities()
straight_line_cities = get_straight_line_cities()
FaroStraightDistance = get_FaroStraightDistance()

# Maria Aragão - 18545


#Verify if the city exists on graph
def verifyCityGraph(city):
    if not city in connected_cities.keys():
        print("Coloque uma cidade válida dentro destas apresentadas: " + ",".join(connected_cities))
        return False
    else:
        return True

#Verify if is a number
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

def return_distance(source_city, destination_city, distanceObj):
    return distanceObj.get((source_city, destination_city)) if distanceObj else 1

def heuristic_search(graph, source_city, destination_city,straightDistance):
    border = PriorityQueue() #cities that does border with city that we are iterating
    border.put((0, source_city, source_city)) #First City
    path_traveled = "" #final path traveled
    print('\nIteração 0')
    print(source_city)
    i = 1
    while True:

        value, actual_node, path = border.get() #Get node with the smaller value
        border.queue.clear()  # Delete border cities from last city visited

        if actual_node == destination_city:
            print('-' * 100)
            print('Cidade destino escolhida ' + destination_city)
            print('Caminho percorrido ' + path_traveled + '.')
            print('Fim')
            return

        print('-' * 100)
        print('Iteração ' + str(i))
        for node in graph[actual_node]:
            border.put((return_distance(node, destination_city, straightDistance), node, path + " -> " + node)) # Add border cities to the queue
            path_traveled = str(border.queue[0][2])
        print(sorted(border.queue)) #Sort by value
        if border.queue[0][1] is not destination_city:
            print('Ir para a cidade: ' + str(border.queue[0][1] + '.'))
        i = i + 1


def menu_uniform_cost():
    pass


def depth_limited(graph, source_city, destination_city, level_limit):
    border = [] #cities that does border with city that we are iterating
    actual_level = 0 #Level in the graph
    border.append(
        {"source_city":source_city,"actual_level":actual_level}
    )
    visited = [] #Cities already visited

    if(int(level_limit) == 0):
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
        print('Estou em ' + actual_node['source_city'] + ' sendo a cidade percorrida número ' + str(actual_node['actual_level'] + 1)+ '. Limite ' + str(actual_node['actual_level']) + '.')  # printa o no atual

        #Destination found
        if actual_node['source_city'] == destination_city:
            print('*' * 150)
            print('Chegamos a ' + destination_city + ' sendo a cidade percorrida número ' + str(actual_node['actual_level'] + 1) + '. Limite ' + str(actual_node['actual_level']) + '.')
            print('Locais Explorados: ')
            print(visited)
            print('Total de iterações: ', i)
            return
        else:
            print('Nó escolhido para abrir ' + actual_node['source_city'])

        f = 0
        for node in graph[actual_node['source_city']]:
            #If city is not visited and is not upper that our level limit on graph
            if not any(x['source_city'] == node for x in visited) and actual_node['actual_level'] + 1 <= int(level_limit):
                border.insert(f,
                              {"source_city":node,"actual_level":actual_node['actual_level'] + 1}
                )
                f = f + 1

        print('-' * 150)
        print('Na lista para visitar --> ', border)
        print('Na lista já visitado --> ', visited)

        # No more options to iterate
        if(len(border) == 0):
            print("\n")
            print("*"*150)
            print("\nNão foi encontrado itenerário dentro do limite máximo de cidades a percorrer.\n")
            return

        i = i + 1



def Menu():
    while True:
        print()
        print("Welcome", end="")
        print("="*10)

        print('1 -------------------- Profundidade Limitada')
        print('2 -------------------- Custo uniforme')
        print('3 -------------------- Procura sôfrega(Destino: Faro)')
        print('4 -------------------- A*(Destino: Faro)')

        method = input('Please choose the searching method: ')

        verifyCity = False
        while verifyCity == False:
            origin = input('\nInsira a cidade de origem:  ')
            verifyCity = verifyCityGraph(origin)

        if method == '1':
            verifyCity = False
            while verifyCity == False:
                destination = input('\nInsira a cidade de destino: ')
                verifyCity = verifyCityGraph(destination)

            verifyNumberVar = False
            while verifyNumberVar == False:
                level_limit = input('\nInsira o limite máximo de cidades a percorrer:  ')
                verifyNumberVar = verifyNumber(level_limit)
            depth_limited(connected_cities, origin, destination, level_limit)
        elif method == '3':
            heuristic_search(straight_line_cities, origin, "Faro", FaroStraightDistance)


Menu()
