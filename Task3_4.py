'''
    Task 3 - 4
    ------------------
    Adapt your graph structure from the previous week to support weights for the edges and implement Dijkstra's algorithm.
    The output of the program should be the total cost and the actual path found.
'''

import sys

class Node:
    def __init__(self, label):
        self.label = label

class Edge:
    def __init__(self, to_node, weight):
        self.to_node = to_node
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = dict()

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, weight):
        edge = Edge(to_node, weight)
        if from_node.label in self.edges:
            from_node_edges = self.edges[from_node.label]
        else:
            self.edges[from_node.label] = dict()
            from_node_edges = self.edges[from_node.label]
        from_node_edges[to_node.label] = edge


def min_cost(q, cost):
    min_node = None
    for node in q:
        if min_node == None:
            min_node = node
        elif cost[node] < cost[min_node]:
            min_node = node

    return min_node

def dijkstra(graph, start):
    q = set()
    cost = {}
    prev = {}

    for v in graph.nodes:       
        cost[v] = sys.maxint      
        prev[v] = sys.maxint      
        q.add(v)                

    cost[start] = 0

    while q:
        v = min_cost(q, cost)
        q.remove(v)
        if v.label in graph.edges:
            for _, w in graph.edges[v.label].items():
                temp = cost[v] + w.weight
                if temp < cost[w.to_node]:
                    cost[w.to_node] = temp
                    prev[w.to_node] = v

    return cost, prev


def path(prev, from_node):
    previous_node = prev[from_node]
    route = [str(from_node.label)]
    while previous_node != sys.maxint:
        route.append(str(previous_node.label))
        temp = previous_node
        previous_node = prev[temp]

    route.reverse()
    return route

###################################################################################

graph = Graph()
a = Node(1)
graph.add_node(a)
b = Node(2)
graph.add_node(b)
c = Node(3)
graph.add_node(c)
d = Node(4)
graph.add_node(d)
e = Node(5)
graph.add_node(e)
f = Node(6)
graph.add_node(f)
g = Node(7)
graph.add_node(g)

graph.add_edge(a, b, 4)
graph.add_edge(a, c, 3)
graph.add_edge(a, e, 7)
graph.add_edge(b, c, 6)
graph.add_edge(b, d, 5)
graph.add_edge(c, d, 11)
graph.add_edge(c, e, 8)
graph.add_edge(d, e, 2)
graph.add_edge(d, f, 2)
graph.add_edge(d, g, 10)
graph.add_edge(e, f, 5)
graph.add_edge(f, g, 3)

cost, prev = dijkstra(graph, a)
print 'path : ' + str(path(prev, g))
print 'cost : ' + str(cost[g])
