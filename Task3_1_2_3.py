'''
    Task 3 - 1
    ------------------
    Implement an unweighted and undirected graph data structure in the programming language of your choice, where the nodes consist of positive integers.
    You can either use an adjacency matrix or an adjacency list approach.
    The program should have functions for the following:
       a. adding a node to the graph.
       b. Adding an edge to the graph.
       c. Printing the graph.
    Note: You must use Object Oriented Programming for this task.

    Task 3 - 2
    ------------------
    Using the same graph structure, implement a function isConnected(G) to check whether or not the graph is connected. The output should be simply 'Yes' or 'No'.

    Task 3 - 3
    ------------------
    Implement the BFS and DFS traversals for the above graph structure. Save the nodes traversed for each of the two traversals in sequence to a text file.

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

    def isPath(self, v, w, path=[]):
        path = path + [v]
        if v == w:
            return path
        if v not in self.nodes:
            return None
        for node in self.nodes[v]:
            if node not in path:
                newpath = self.isPath(node, w, path)
                if newpath:
                    return newpath
        return None
    
    def adjacency_list(self):
        if len(self.nodes) >= 1:
                return [str(key) + ':' + str(self.nodes[key]) for key in self.nodes.keys()]  
        else:
            return dict()
                        
    def __str__(self):
        return str(self.adjacency_list())


def isConnected(g):
    is_path = True
    nodes = g.nodes.keys()
    n = len(nodes)
    for i in range(0, n):
        for j in range(i+1, n):
            path = g.isPath(nodes[i], nodes[j])
            if path == None:
                is_path = False;
                break;
        if not is_path:
            break;
    print 'Yes' if is_path else 'No'


def bfs(g):
    path=[]
    start = g.nodes.keys()[0]
    q = [start]
    while q:
        v = q.pop(0)
        if not v in path:
          path = path + [v]
          q = q + g.nodes[v]
    return path

def dfs(g):
    path=[]
    start = g.nodes.keys()[0]
    q = [start]
    while q:
        v = q.pop(0)
        if v not in path:
          path = path + [v]
          q = g.nodes[v] + q
    return path

          
###################################################################################

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

g = Graph()
g.add_node(f)
g.add_node(b)
g.add_node(a)
g.add_node(c)
g.add_node(e)
g.add_node(d)

g.add_edge(a,b)
g.add_edge(a,c)
g.add_edge(b,d)
g.add_edge(c,e)
g.add_edge(c,f)

print g

path = g.isPath(a.name,d.name)
if path != None:
    file = open(str(a.name) + '_' + str(d.name) + '_path.txt', 'w')
    file.write(str(path))
    file.close()

isConnected(g)
x = Node(7)
g.add_node(x)
print g
isConnected(g)

path = bfs(g)
print path
file = open('bfs.txt', 'w')
file.write(str(path))
file.close()

path = dfs(g)
print path
file = open('dfs.txt', 'w')
file.write(str(path))
file.close()
