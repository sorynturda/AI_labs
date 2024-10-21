import random
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from signal import sigwait


class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def getEdges(self):
        a = []
        for i in self.neighbours:
            a.append([self.vertex_number, i])
        return a

    def printNeighbours(self):
        for neighbour in self.neighbours:
            print(self, neighbour, sep='->')

    def getOutDegree(self):
        return len(self.neighbours)

    def getVertexNumber(self):
        return self.vertex_number

    def removeNeighbours(self):
        factor = int(len(self.neighbours) * 0.8)
        for i in range(factor):
            self.neighbours.remove(random.choice(self.neighbours))
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
# print(highestDegree)

subgraphNodes = list(set(random.choices(nodes[1:len(nodes)+1], k=int((len(nodes)-1)*0.6))))

a = []
for it in subgraphNodes:
    for pair in it.getEdges():
        a.append(pair)

A = np.matrix(a)
G = nx.from_numpy_array(A)
nx.draw(G)
plt.show()

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
