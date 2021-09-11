from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Graph:
    def __init__(self):
        self._adjacency_list = {}

    def add_node(self, value):

        vertex = Vertex(value)

        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):

        if start_vertex not in self._adjacency_list:
            raise ValueError('Start vertex not exist in the graph')
        if end_vertex not in self._adjacency_list:
            raise ValueError('End Vertex not exist in the graph')

        self._adjacency_list[start_vertex].append(Edge(end_vertex, weight))
        return self._adjacency_list[start_vertex][0]

   
