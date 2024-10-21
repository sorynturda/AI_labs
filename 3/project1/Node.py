import random


class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def printNeighbours(self):
        for neighbour in self.neighbours:
            print(self, neighbour, sep='->')

    def getOutDegree(self):
        return len(self.neighbours)

    def __str__(self):
        return f'({self.vertex_number})'


def printGraph(nodes):
    for i in range(1, len(nodes)):
        nodes[i].printNeighbours()

nodes = [0]

with open("graph1.txt", 'r') as f:
    n = int(f.readline())
    for i in range(1,n+1):
        nodes.append(Node(i))
    for line in f:
        edge = line.split()
        nodes[int(edge[0])].edge(int(edge[1]))

highestDegree = -1e9
for i in range(len(nodes)-1):
    highestDegree = max(highestDegree, nodes[i+1].getOutDegree())
print(highestDegree)

subgraphNodes = random.choices(nodes, k=int((len(nodes))*0.6))
for node in subgraphNodes:
    print(node)

# for i in range(7):
#     nodes.append(Node(i))
# nodes[1].edge(nodes[3])
# nodes[1].edge(nodes[6])
# nodes[2].edge(nodes[6])
# nodes[3].edge(nodes[3])
# nodes[3].edge(nodes[4])
# nodes[5].edge(nodes[2])
# nodes[6].edge(nodes[3])
# nodes[6].edge(nodes[4])
# nodes[6].edge(nodes[5])

# 5
# 1 2
# 1 3
# 2 1
# 2 5
# 3 1
# 3 5
# 4 5
# 4 1
# 5 3
