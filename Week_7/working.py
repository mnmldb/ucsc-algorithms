# input
def shortestReach(n, edges, s):
    pass

n = 4
edges = [[1, 2, 24], [1, 4, 20], [3, 1, 3], [4, 3, 12]]
s = 1

# data structures
class Node:
    def __init__(self, name):
        self.name = name # name of the node (1, 2, 3, ...)
        self.visited = False # default status is unvisited
        self.value = 'L' # default value is infinity
        self.fanout = [] # create an empty list for fanout
    def setFanOut(self, out, cost):
        self.fanout.append([out, cost]) # [[2, 24], [4, 20], [3, 3]]
    def setValue(self, value):
        self.value = value # total cost from the starting point
    def setVisited(self):
        self.visited = True


# create list of node for BFS
listOfNodes = [None] * (n + 1) # n + 1 as 0 is not used for nodes

for e in edges: # [1, 2, 24]
    # forward
    if listOfNodes[e[0]] is None:
        node = Node(e[0])
        node.setFanOut(e[1], e[2])
        listOfNodes[e[0]] = node
    else:
        listOfNodes[e[0]].setFanOut(e[1], e[2])
    
    # backward
    if listOfNodes[e[1]] is None:
        node = Node(e[1])
        node.setFanOut(e[0], e[2])
        listOfNodes[e[1]] = node
    else:
        listOfNodes[e[1]].setFanOut(e[0], e[2])