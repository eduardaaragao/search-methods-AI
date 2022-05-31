class Node(object):
    def __init__(self, label: str = None):
        self.label = label
        self.children = []

    def __lt__(self, other):
        return self.label < other.label

    def __gt__(self, other):
        return self.label > other.label

    def __repr__(self):
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, node, cost=1):
        edge = Edge(self, node, cost)
        self.children.append(edge)

class Edge(object):
    def __init__(self, source: Node, destination: Node, cost: int = 1):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return '{}: {}'.format(self.cost, self.destination.label)


Aveiro = Node('Aveiro')
Braga = Node('Braga')
Bragança = Node('Bragança')
Beja = Node('Beja')
CasteloBranco = Node('Castelo Branco')
Coimbra = Node('Coimbra')
Évora = Node('Évora')
Faro = Node('Faro')
Guarda = Node('Guarda')
Leiria = Node('Leiria')
Lisboa = Node('Lisboa')
Porto = Node('Porto')
VilaReal = Node('Vila Real')
Viseu = Node('Viseu')
Setúbal = Node('Setúbal')
VianaDoCastelo = Node('Viana do Castelo')
Santarém = Node('Santarém')
Portalegre = Node('Portalegre')

Aveiro.add_child(Porto, 68)
Aveiro.add_child(Viseu, 95)
Aveiro.add_child(Coimbra, 68)
Aveiro.add_child(Leiria, 115)

Braga.add_child(VianaDoCastelo, 48)
Braga.add_child(VilaReal, 106)
Braga.add_child(Porto, 53)

Bragança.add_child(VilaReal, 137)
Bragança.add_child(Guarda, 202)

Beja.add_child(Évora, 78)
Beja.add_child(Faro, 152)
Beja.add_child(Guarda, 142)

CasteloBranco.add_child(Coimbra, 159)
CasteloBranco.add_child(Guarda, 106)
CasteloBranco.add_child(Portalegre, 80)
CasteloBranco.add_child(Évora, 203)

Coimbra.add_child(Viseu, 96)
Coimbra.add_child(Leiria, 67)
Coimbra.add_child(Aveiro, 68)
Coimbra.add_child(CasteloBranco, 159)

Évora.add_child(Lisboa, 150)
Évora.add_child(Santarém, 117)
Évora.add_child(Portalegre, 131)
Évora.add_child(Setúbal, 103)
Évora.add_child(Beja, 78)
Évora.add_child(CasteloBranco, 203)

Faro.add_child(Setúbal, 249)
Faro.add_child(Lisboa, 299)
Faro.add_child(Beja, 152)

Guarda.add_child(VilaReal, 157)
Guarda.add_child(Viseu, 85)
Guarda.add_child(Bragança, 202)
Guarda.add_child(CasteloBranco, 106)

Leiria.add_child(Lisboa, 129)
Leiria.add_child(Santarém, 70)
Leiria.add_child(Aveiro, 115)
Leiria.add_child(Coimbra, 67)

Lisboa.add_child(Santarém, 78)
Lisboa.add_child(Setúbal, 50)
Lisboa.add_child(Évora, 150)
Lisboa.add_child(Faro, 299)
Lisboa.add_child(Leiria, 129)

Portalegre.add_child(CasteloBranco, 80)
Portalegre.add_child(Évora, 131)

Porto.add_child(VianaDoCastelo, 71)
Porto.add_child(VilaReal, 116)
Porto.add_child(Viseu, 133)
Porto.add_child(Aveiro, 68)
Porto.add_child(Braga, 533)

Santarém.add_child(Évora, 117)
Santarém.add_child(Leiria, 70)
Santarém.add_child(Lisboa, 78)

Setúbal.add_child(Beja, 142)
Setúbal.add_child(Évora, 103)
Setúbal.add_child(Faro, 249)
Setúbal.add_child(Lisboa, 50)

VianaDoCastelo.add_child(Braga, 48)
VianaDoCastelo.add_child(Porto, 71)

VilaReal.add_child(Viseu, 110)
VilaReal.add_child(Braga, 106)
VilaReal.add_child(Bragança, 137)
VilaReal.add_child(Guarda, 157)
VilaReal.add_child(Porto, 116)

Viseu.add_child(Aveiro, 95)
Viseu.add_child(Coimbra, 96)
Viseu.add_child(Guarda, 65)
Viseu.add_child(Porto, 133)
Viseu.add_child(VilaReal, 110)
