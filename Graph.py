class Graph:
    def __init__(self):
        ''' self._vertices = {Vertex : [Edge, Edge]}
            Maps Vertex objects to a list of each of 
            their adjacent Edges'''
        self._vertices = {}

    def __str__(self):
        outstr = '\n--------Graph---------\nVertices: '
        for v in self.vertices():
            outstr += f'{v}, '
        outstr += '\nEdges: '
        for e in self.edges():
            outstr += f'{{({e.vertices()[0]}, {e.vertices()[1]}), w = {e.element()}}}, '
        outstr += '\n'

        return outstr

    def vertices(self):
        vert_list = []
        for v in self._vertices:
            vert_list.append(v)
        return vert_list # returns a list of Vertex objects

    def edges(self):
        edge_list = []
        for v in self._vertices: # v = Vertex object
            for e in v.adjList():
                if e not in edge_list:
                    edge_list.append(e)
        return edge_list

    def add_vertex(self, element):
        node = Vertex(element)
        self._vertices[node] = node.adjList()

    def add_edge(self, x, y, label):
        if x in self.vertices() and y in self.vertices():
            edge = Edge(x, y, label)

            x.add_edge(edge)
            y.add_edge(edge)
            self._vertices[x], self._vertices[y] = x.adjList(), y.adjList()

    
    def degree(self, x):
        return len(x.adjList())

    def get_edge(self, x, y):
        for e in self.edges():
            if x == e.opposite(y):
                return e

    def get_edges(self, x):
        output = []
        for e in x.adjList():
            output.append(e)

        return output


    def remove_vertex(self, v):
        for e in self.get_edges(v):
            self.remove_edge(e)
        self._vertices.pop(v)

    def remove_edge(self, e):
        v1, v2 = e.vertices()
        v1._adjlist.remove(e)
        v2._adjlist.remove(e)


    def num_vertices(self):
        return len(self._vertices)

    def num_edges(self):
        return len(self.edges())


class Vertex:
    def __init__(self, element):
        self._element = element # int or str
        self._adjlist = []      # [Edge] list of edges

    def __str__(self):
        outstr = f'{self._element}'
        return outstr

    def element(self):
        return self._element

    def adjList(self):
        return self._adjlist

    def add_edge(self, edge):
        for e in self.adjList():
            if edge == e:
                return
        self._adjlist.append(edge) # adds a {(Vertex, Vertex) : int} pair to _adjlist

class Edge:
    def __init__(self, v1, v2, label):
        self._v1 = v1       # Vertex object
        self._v2 = v2       # Vertex object
        self._label = label # int

    def __str__(self):
        outstr = f'{self._v1.element()} -----{self._label}----- {self._v2.element()}'
        return outstr

    def __eq__(self, other):
        if self.element() == other.element():
            u1, u2 = other.vertices()
            if self._v1 == u1 and self._v2 == u2:
                return True
            elif self._v1 == u2 and self._v2 == u1:
                return True
        return False

    def vertices(self):
        return self._v1, self._v2   # return two Vertex objects

    def opposite(self, v): # v = Vertex object
        if v == self._v1:
            return self._v2
        elif v == self._v2:
            return self._v1
        else:
            return None

    def element(self):
        return self._label

if __name__ == '__main__':
    graph = Graph()

    for i in range(3):
        graph.add_vertex(i + 1)
    vertices = graph.vertices()

    graph.add_edge(vertices[0], vertices[1], 1)
    graph.add_edge(vertices[1], vertices[2], 2)
    graph.add_edge(vertices[0], vertices[2], 6.5)

    print(f'vertices() = {[x.element() for x in graph.vertices()]}')
    print(f'edges() = {[x.__str__() for x in graph.edges()]}')

    print(graph)
    print(f'num_vertices() = {graph.num_vertices()}, num_edges = {graph.num_edges()}')
    print(f'degree(vertices[0]) = {graph.degree(vertices[0])}')
    print(f'get_edge({vertices[2].element()}, {vertices[1].element()}) = {graph.get_edge(vertices[2], vertices[1])}')
    print(f'get_edges({vertices[0].element()}) = {[x.vertices()[1].element() for x in graph.get_edges(vertices[0])]}')

    graph.remove_edge(graph.get_edge(vertices[0], vertices[2]))

    print(f'remove_edge(get_edge({vertices[0].element()}, {vertices[2].element()})) = {[x.__str__() for x in graph.edges()]}')
    print(f'''get_edges({vertices[0]}) = {[x.element() for x in graph.get_edges(vertices[0])]},
get_edges({vertices[2]}) = {[x.element() for x in graph.get_edges(vertices[2])]}''')

    graph.remove_vertex(vertices[0])
    print(graph)