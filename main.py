# Artificial Intelligence
from aestrela import Grafo, AEstrela
from cities import *
from queue import PriorityQueue
from graphs import *
import os

connected_cities = get_connected_cities()
straight_line_cities = get_straight_line_cities()
FaroStraightDistance = get_FaroStraightDistance()


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
    os.system('cls')
    grafo = Grafo()
    grafo.mostrar_cidades()
    verified_key = False

    while not verified_key:
        key = int(input('Por favor, selecione o código correspondente à cidade de origem: '))
        verified_key = grafo.validar_key(key)
        if verified_key:
            os.system('cls')
            print('Vamos começar nossa viagem...')
            busca_estrela = AEstrela(grafo.faro)  # Definindo o objetivo do algoritmo
            cidade_origem = grafo.get_cidade_using_key(key)
            busca_estrela.buscar(cidade_origem)  # Definindo a origem do algoritmo
        else:
            print('O código inserido não é válido.')


def return_distance(source_city, destination_city, distanceObj):
    return distanceObj.get((source_city, destination_city)) if distanceObj else 1


def heuristic_search(graph, source_city, destination_city, straightDistance):
    border = PriorityQueue()  # cities that does border with city that we are iterating
    border.put((0, source_city, source_city))  # First City
    path_traveled = ""  # final path traveled
    print('\nIteração 0')
    print(source_city)
    i = 1
    while True:

        value, actual_node, path = border.get()  # Get node with the smaller value
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
            border.put((return_distance(node, destination_city, straightDistance), node,
                        path + " -> " + node))  # Add border cities to the queue
            path_traveled = str(border.queue[0][2])
        print(sorted(border.queue))  # Sort by value
        if border.queue[0][1] is not destination_city:
            print('Ir para a cidade: ' + str(border.queue[0][1] + '.'))
        i = i + 1


def menu_uniform_cost(origin, destination):
    # recebemos as variáveis do input do menu, e convertemos o destino para variável
    # para que o possa invocar do grafo
    strRoot = origin
    root = globals()[strRoot]
    # aqui criamos a prirodade de queue dos caminhos
    queue = PriorityQueue()
    queue.put((0, [root]))
    # com este while vamos iterar os itens que estão na queue
    while not queue.empty():
        # obter o item de mais alta prioridade
        pair = queue.get()
        current = pair[1][-1]
        # se for o destino que queremos, devolvemos o caminho
        if current.nome == destination:
            print(pair[1])
            return pair[1]
        # senão vamos adicionar todas as distâncias entre cidades à queue
        for caminho in current.children:
            # criamos um novo caminho com a cidade e a distância
            novoCaminho = list(pair[1])
            novoCaminho.append(caminho.destino)
            # depois ligamos o novo caminho à queue com prioridade
            queue.put((pair[0] + caminho.custo, novoCaminho))


def depth_limited(graph, source_city, destination_city, level_limit):
    border = []  # cities that does border with city that we are iterating
    actual_level = 0  # Level in the graph
    border.append(
        {"source_city": source_city, "actual_level": actual_level}
    )
    visited = []  # Cities already visited

    if int(level_limit) == 0:
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
        if len(border) == 0:
            print("\n")
            print("*" * 150)
            print("\nNão foi encontrado itenerário dentro do limite máximo de cidades a percorrer.\n\n")
            return

        i = i + 1


def menu_custo_uniforme():
    origin = ''
    destination = ''
    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nInsira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)

    verify_city = False
    while not verify_city:
        destination = input('\nInsira a cidade de destino: ')
        verify_city = verifyCityGraph(destination)
    menu_uniform_cost(origin, destination)


def menu_profundidade_limitada():
    origin = ''
    destination = ''

    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nPor favor, insira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)

    verify_city = False

    while not verify_city:
        destination = input('\nPor favor, insira a cidade de destino: ')
        verify_city = verifyCityGraph(destination)

    level_limit = input('\nInsira o limite máximo de cidades a percorrer:  ')

    depth_limited(connected_cities, origin, destination, level_limit)


def menu_procura_sofrega():
    origin = ''
    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nInsira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)
    heuristic_search(straight_line_cities, origin, "Faro", FaroStraightDistance)


def Menu():
    print("*" * 100)
    print("Bem vindo")
    while True:
        print('1 -------------------- Profundidade Limitada')
        print('2 -------------------- Custo uniforme')
        print('3 -------------------- Procura sôfrega(Destino: Faro)')
        print('4 -------------------- A*(Destino: Faro)')
        print('0 -------------------- Sair')

        method = input('Por favor, escolha o método de procura que deseja: ')

        if method == '1':
            menu_profundidade_limitada()
        elif method == '2':
            menu_custo_uniforme()
        elif method == '3':
            menu_procura_sofrega()
        elif method == '4':
            menu_a_star()
        elif method == '0':
            print('Tchauzinho =)')
            break
        else:
            print('Opção não válida.')


Menu()
