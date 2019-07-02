#! -*- coding:utf-8 -*-

from collections import defaultdict
from queue import Queue


"""
there are two ways to represent graph
1. as a collection of adjacency lists
2. as a adjacency matrix
"""

class GraphNode:
    def __init__(self, v, neighbors):
        self.value = v
        self.neighbors = neighbors

        self.color = None
        self.depth = 0
        self.parent = None

graphs = []
graphs.append('A', ['B', 'D'])
graphs.append('B',  ['A', 'C', 'D'])
graphs.append('C', ['B'])
graphs.append('D', ['A', 'B'])

white = "white"
black = 'black'
gray = 'gray'

def BFS(G, s):
    for node in graphs:
        node.color = white
        node.parent = None
        node.depth = 0
    s.color = gray
    s.depth = 0
    s.parent = None
    q = Queue()
    q.put(s)
    while len(q) > 0:
        u = q.get()
        for n in u.neighbors:
