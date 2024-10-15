class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return f'({self.vertex_number})'


nodes = []
for i in range(7):
    nodes.append(Node(i))
nodes[1].edge(nodes[3])
nodes[1].edge(nodes[6])
nodes[2].edge(nodes[6])
nodes[3].edge(nodes[3])
nodes[3].edge(nodes[4])
nodes[5].edge(nodes[2])
nodes[6].edge(nodes[3])
nodes[6].edge(nodes[4])
nodes[6].edge(nodes[5])