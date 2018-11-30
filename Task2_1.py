'''
    Task 2 - 1
    ------------------
    Implement an unweighted and undirected graph data structure in the programming language of your choice, where the nodes consist of positive integers.
    You can either use an adjacency matrix or an adjacency list approach.
    The program should have functions for the following:
       a. adding a node to the graph.
       b. Adding an edge to the graph.
       c. Printing the graph.
    Note: You must use Object Oriented Programming for this task.
'''

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = []
        
    def add_neighbor(self, neighbor):
        if neighbor.name not in self.neighbors:
            self.neighbors.append(neighbor.name)
            neighbor.neighbors.append(self.name)
            self.neighbors = sorted(self.neighbors)
            neighbor.neighbors = sorted(neighbor.neighbors)
        
    def __repr__(self):
        return str(self.neighbors)

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node):
        self.nodes[node.name] = node.neighbors
            
    def add_edge(self, node_from, node_to):
            node_from.add_neighbor(node_to)
            self.nodes[node_from.name] = node_from.neighbors
            self.nodes[node_to.name] = node_to.neighbors
    
    def adjacency_list(self):
        if len(self.nodes) >= 1:
                return [str(key) + ':' + str(self.nodes[key]) for key in self.nodes.keys()]  
        else:
            return dict()
                        
    def __str__(self):
        return str(self.adjacency_list())

###################################################################################

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

g = Graph()
g.add_node(a)
g.add_node(b)
g.add_node(c)
g.add_node(d)
g.add_node(e)

g.add_edge(a,b)
g.add_edge(a,c)
g.add_edge(b,c)
g.add_edge(b,d)
g.add_edge(c,e)
g.add_edge(d,b)
g.add_edge(e,d)

print g
