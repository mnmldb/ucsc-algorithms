###########################################################
# All imports as in HackerRank
###########################################################
import math
import os
import random
import re
import sys

# 39 - 43
class Node:
    def __init__(self, n:'int'):
        self._name = n
        self._fanouts = {} # dict of fanouts of edges. Key is other (int), Value is cost
        # self._fanins = {} # List of fanouts of edges

# 45 - 74
#############################################
# Time THETA(1)
# IDEA 1
# If we have multiple edges, we need to store only ONE lowest edge
# Let us 1-2-10, 1-2-5, 1-2-1, 1-2-100
# that's why: self._fanouts = {} # dict of fanouts of edges. Key is other (int), Value is cost
#############################################
def create_edge(f:'Node', t:'Node', w:'float', fanout:'bool'):
    if fanout == True:
        e = t._name
        # is edge e already in f fanout
        if e in f._fanouts: #O(1)
            ## already there. Put keep the lowest cost
            v = f._fanouts[e] #O(1)
            if w < v:
                f._fanouts[e] = w # insert lowest value. O(1)
        else:
            # First time
            f._fanouts[e] = w
    else:
        e = t._name
        # is edge e already in f fanins
        if e in f._fanins: # O(1)
            ## already there. Put keep the lowest cost
            v = f._fanins[e] # O(1)
            if w < v:
                f._fanins[e] = w # insert lowest value. O(1)
        else:
            # First time
            f._fanins[e] = w

# 77 - 98
#############################################
# Time: THETA(V + E)
# Space: THETA(V)
#############################################
def build_node_and_edge(node_list:'list', f:'int', t:'int', w:'double', dir:'int'):
    node_from = node_list[f]
    if node_from == None:
        node_from = Node(f)
        node_list[f] = node_from
    
    node_to = node_list[t]
    if node_to == None:
        node_to = Node(t)
        node_list[t] = node_to
    
    # NOW create edges
    create_edge(node_from, node_to, w, True)
    # f->t implies t has a fanin of f
    # create_edge(node_to, node_from, w, False)
    if dir == True:
        create_edge(node_to, node_from, w, True)
        # create_edge(node_from, node_to, w, False)

# 100 - 291?
class Dijkstra2:
    def __init__(self, t, n, e, node_list, start_city, ns, undirected, hacker_rank_flow):
        self._t = t # Name of the graph
        self._n = n # number of nodes
        self._e = e # list of edges. Each edge has from, to, and weight
        self._node_array = node_list
        self._start_city = start_city
        self._ns = ns # node start. For HackerRank always 1
        self._undirected = undirected # Always False for HackerRank
        self._hacker_rank_flow = hacker_rank_flow # Always True for HackerRank
    
    def get_path(self):
        self._alg()
        # WRITE YOUR CODE in _alg
        ## YOU CAN HAVE ANY NUMBER OF CLASSES AND FUNCTION
        for i in self._path:
            print(i, end=' ')
        print()
        return self._path
    
    def _alg(self):
        pass
        self._alg1()
    
    class Node_data:
        def __init__(self, n, cost, f, visited):
            self._name = n
            self._cost = cost
            # self._from = f
            self._visited = visited
        
        ## Override __lt__ in Python 3, __cmp__ only in Python 2
        def __lt__(self, rhs:'Node_data')->'bool':
            if self._cost < rhs._cost: # Change to > for max heap
                return True
            return False

    #############################################
    # Time: O(V + E)
    # Space: O(V)
    #############################################
    def _write_dot(self):
        pass

    #############################################
    # Time: THETA(V + E)
    # Space: THETA(V)
    #############################################
    def _build_graph(self):
        if self._node_array == None:
            self._node_array = []
            n = self._n + self._ns
            for i in range(n):
                self._node_array.append(None)
            for e in self._e:
                build_node_and_edge(self._node_array, e[0], e[1], e[2], self._undirected)

    #############################################
    # Time: O(V log V)
    # Space: THETA(V)
    #############################################
    def _setup(self):
        n = self._n + self._ns
        for i in range(self._ns):
            self._node_data_array.append(None)
        for i in range(self._ns, n): # O(V)
            c = self._infinity
            if i == self._start_city:
                c = 0
            nd = Dijkstra2.Node_data(i, c, i, False)
            self._node_data_array.append(nd)
            if c == 0:
                # IDEA 4. DO NOT STORE ALL NODES IN HEAP. STORE AS REQUIRED
                heapq.heappush(self._min_heap, nd) # O(log(V))
                self._number_of_nodes_added_to_heap = self._number_of_nodes_added_to_heap + 1
        assert(len(self._min_heap) == 1) # ONLY 1 is stored to start with

    #############################################
    # Time: O(V)
    # Space: THETA(V)
    #############################################
    def _fill_shortest_cost(self):
        n = self._n + self._ns
        num_to_append = self._n - 1 # Because startCity should not be included
        for i in range(self._ns, n):
            nd = self._node_data_array[i]
            if nd == None:
                # Node which is unreachable
                self._path.append(-1)
            else:
                if nd._name == self._start_city:
                    # WE should not fill array or print in hacker
                    pass
                else:
                    w = nd._cost
                    if w == self._infinity:
                        self._path.append(-1)
                    else:
                        pass
                        # TBC

    #############################################
    # Time: O(log V)
    # Space: THETA(1)
    #############################################
    def _relax(self, s:'Node', f:'Node', itr:'int', cost_s_to_f:'float'):
        # We know the best way to got to s
        cost_of_visiting_s = self._node_data_array[s._name]._cost
        assert(cost_of_visiting_s != self._infinity)
        # What is the cost to go from s to f
        # This is given by user
        assert(cost_s_to_f != self._infinity)
        cost = cost_of_visiting_s + cost_s_to_f
        fnode = self._node_data_array[f._name]
        best_cost_know_of_fnode_at_this_time = fnode._cost
        if cost < best_cost_know_of_fnode_at_this_time:
            # Make a deep copy of the object, before you change
            # IDEA 2. YOU CANNOT DELETE arbitrary node in head
            r = copy.deepcopy(fnode) # O(1)
            assert(id(r) != id(fnode))
            # Let the OLD high cost node be in the heap.
            # Deleting arbitrary node in MINHEAP is O(n).
            # So leave it as VISITED. Note it is in the heap
            fnode._visited = True # So that we will not use it.Let it be in heap
            # That means if a better path
            r._cost = cost
            r._from = s._name # WE visited this city from s
            r._visited = False
            # Inserts the relaxed node r into minheap. O(log V)
            heapq.heappush(self._min_heap, r) # O(log V)
            self._number_of_nodes_added_to_heap = self._number_of_nodes_added_to_heap + 1
            # IDEA 3. We have the concept of _node_data_array and work with integer
            # This idea is working because we never store node in edge
            # Instead we store a number. As we put r in that position f
            # all edges have the correct node.
            # It is impossible to change all the edges when pointers change
            self._node_data_array[f._name] = r # NOW a[f] has the correct inserted node. O(1)
            assert(self._node_data_array[f._name]._name == r._name)
            assert(self._node_data_array[f._name]._cost == r._cost)
    
    #############################################
    # Time: O(V log V)
    # Space: THETA(1)
    #############################################
    def _Dijkstraalg(self):
        itr = 0
        while len(self._min_heap):
            # Retrieves and removes the heap of this queue,
            nd = heapq.heappop(self._min_heap) # O(log V)
            assert(nd != None)
            if nd._visited == False: # This also takes care of node which is relaxed
                s = nd._name
                n = self._node_array[s] # Working Node
                if n != None: # This can happen because some nodes may be ever included in the graph
                    itr = itr + 1
                    cost_of_visiting_n = self._node_data_array[n._name]._cost
                    if cost_of_visiting_n == self.infinity:
                        continue # This can happen because of unconnected component
                    # For each fanout relax
                    # Go through dict of fanouts
                    # Note Key is Edge. Value is
                    for e, v in n._fanouts.items():
                        f = self._node_data_array[e] # e is e._other as we separted key and value
                        self._relax(n, f, itr, v)
                    nd._visited = True # For printing T in debug mode

    def _Dijkstra(self):
        self._number_of_nodes_added_to_heap = 0
        self._setup()
        self._Dijkstraalg()
        self._fill_shortest_cost()
    
    def _alg1(self):
        self._number_of_nodes_added_to_heap = 0
        self._infinity = 9999999999
        self._min_heap = [] # minheap of Node_data
        self._node_data_array = [] # list of Node_data. This cannot be bigger than numV

        self._build_graph()
        self._write_dot()
        self._Dijkstra()

###########################################################
# WRITE CODE BELOW ENDS
###########################################################

# 308 - 313
###########################################################
# Interface of HackerRank Changed
###########################################################
def shortestReachMainChanged(n, node_list:'list', s)->'list of path of size n-1':
    d = Dijkstra2('', n, None, node_list, s, 1, True, True)
    return d.get_path()

# 315 - 334
###########################################################
# Testing on one graph. YOU CANNOT CHANGE
###########################################################
def test1(t, n, e, node_list, start_city, ns, undirected, hacker_rank_flow, expected_answer):
    d = Dijkstra2(t, n, e, node_list, start_city, ns, undirected, hacker_rank_flow)
    dpath = d.get_path()
    if dpath != expected_answer:
        print('Expected answer is:')
        print(expected_answer)
        print('Your answer is:')
        print(dpath)
        assert(False)

# 337 - 480
###########################################################
# This is my main. YOU CANNOT CHANGE
###########################################################
def jag_main():
    t = '1' # name of the graph
    n = 4 # Number of nodes in the graph
    e = [
        [1, 2, 24],
        [1, 4, 20],
        [3, 1, 3],
        [4, 3, 12]
    ]
    start_city = 1
    nodeStart = 1 # HackerRank startCitys from 1
    undirected = True # Undirected graph
    hacker_rank_flow = False
    expected_answer = [24, 3, 15]
    test1(t, n, e, None, start_city, nodeStart, undirected, hacker_rank_flow, expected_answer)

    # a few tests continue

    print('All tests in jag_main passed. Let us see whether you pas hacker_rank_main')

# 483 - 506
###########################################################
# This is exactly main of HackerRank but changed edges to list of codes
###########################################################
def hacker_rank_main_changed():
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[m])
        node_list = []
        for i in range(n + 1):
            node_list.append(None)
        for _ in range(m):
            edge = list(map(int, input().rstrip().split()))
            f = edge[0]
            t = edge[1]
            w = edge[2]
            if f > t:
                temp = f
                f = t
                t = temp
            build_node_and_edge(node_list, f, t, w, True) # always undirected graph
        s = int(input())
        shortestReachMainChanged(n, node_list, s)

# 508 - 526
###########################################################
# This is exactly main of HackerRank. DO NOT CHANGE
###########################################################
def hacker_rank_main_asis():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        nm = input().split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []
        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))
        s = int(input())
        result = shortestReach(n, edges, s)
        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

# 529 - 537
###########################################################
# start up
# Change True to False, when you submit for HackerRank
###########################################################
if __name__ == '__main__':
    #Run 1 of the 3 below
    #jag_main()
    #hacker_rank_main_asis()
    hacker_rank_main_changed()