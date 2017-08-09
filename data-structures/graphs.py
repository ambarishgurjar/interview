# dem graphs: collection of nodes
# DIRECTED
# UNDIRECTED
# CONNECTED 
# ACYLCIC

# TWO TYPES OF REPRESENTATION

# Adjacency List
# node: stores adjacent vertices

# ID: string, weight: int


# see https://www.python.org/doc/essays/graphs/ as a reference
class Node:
	''' Using dictionaries for implementation
	'''
	def __init__(self, ID,  weight):
		self.ID = ID
		self.weight = weight
		self.connections = {}
	def connect(self, other):
		self.connections[other.ID] = other.weight
		return other.ID
	def getConnections(self):
		return self.connections.keys()

class Graph(Node):
	def __init__(self):
		self.nodes = {}
		self.size = len(self.nodes)

	def add(self, Node):
		# Node already initialized
		# adding Node's connecting vertices to graph

		for conn in Node.connections.keys():
			if Node.ID in self.nodes.keys():
				self.nodes[Node.ID].append(eval(conn))
			else: 
				self.nodes[Node.ID] = eval(conn).ID

	def insert(self, ID, weight):
		vertex = Node.__init__(self, ID, weight)
		self.add(vertex)

a = Node('a', 5)
b = Node('b', 4)
c = Node('c', 4)
a.connect(b)
a.connect(c)
# print(a.getConnections())
# print(a.connections)
G = Graph()
G.add(a)
print(G.nodes)




# Adjacency Matrix
# N x N boolean matrix, matrix[i][j] true = edge between vertex i and j
# UNDIRECTED: symmetric matrix


