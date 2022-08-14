from Graph import Graph, Edge

class DirectedGraph(Graph):
    def __init__(self):
        self._vertices = {}

    def add_edge(self, x, y, label):
        if x in self.vertices() and y in self.vertices():
            edge = DirectedEdge(x, y, label)

            x.add_edge(edge)
            y.add_edge(edge)
            self._vertices[x], self._vertices[y] = x.adjList(), y.adjList()

    def in_degree(self, v):
        inlist = []
        edges = v.adjList()
        for e in edges:
            if e.vertices()[1] == v:
                inlist.append(1)
        return len(inlist)

    def out_degree(self, v):
        outlist = []
        edges = v.adjList()
        for e in edges:
            if e.vertices()[0] == v:
                outlist.append(1)
        return len(outlist)

    def get_in_edges(self, v):
        pass

    def get_out_edges(self, v):
        pass

class DirectedEdge(Edge):
    def __init__(self, v1, v2, label):
        super().__init__(v1, v2, label)

    def __str__(self):
        outstr = f'{self._v1.element()} -----{self._label}----> {self._v2.element()}'
        return outstr

    def __eq__(self, other):
        if self.element() == other.element() and self.get_start() == other.get_start() and self.get_end() == other.get_end():
            return True
        return False

    def get_start(self):
        return self._v1

    def get_end(self):
        return self._v2

if __name__ == '__main__':
    dE1 = DirectedEdge(1, 2, 1)
    dE2 = DirectedEdge(2, 1, 1)
    dE3 = DirectedEdge(2, 1, 1)

    print(f'{bool(dE1 == dE2)}, {bool(dE2 == dE3)}') 

    print(f'{dE1.get_start()}, {dE1.get_end()}')

    dG = DirectedGraph()
    for i in range(3):
        dG.add_vertex(i + 1)
    vertices = dG.vertices()

    dG.add_edge(vertices[0], vertices[1], 1)
    dG.add_edge(vertices[1], vertices[0], 1)
    dG.add_edge(vertices[2], vertices[1], 1)
    print(dG)
    for i in range(3):
        print(f'{dG.in_degree(vertices[i])}, {dG.out_degree(vertices[i])}')
