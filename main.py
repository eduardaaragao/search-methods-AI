# Artificial Intelligence

# Maria Aragão - 18545

def menu_a_star():
    origin = input('Please enter the origin location: ')
    print('Destination location: Faro')
    destination = 'Faro'
    pass


def menu_sophrega_search():
    pass


def menu_uniform_cost():
    pass


def menu_depth_limited():
    pass


def Menu():
    while True:
        print("Welcome", end="")
        print("="*10)
        destination = input('Enter the destination location: ')
        origin = input('Enter the origin location:  ')

        print('1 -------------------- Depth Limited')
        print('2 -------------------- Uniform Cost')
        print('3 -------------------- Sophrega Search')
        print('4 -------------------- A*')

        method = input('Please choose the searching method: ')

        if method == '1':
            menu_depth_limited()
            break
        elif method == '3':
            # Implementação: Maria Eduarda
            menu_a_star()


Menu()
