from Graph import Graph

def dept_first_search(graph, v):
    graph_dict = {v:None}
    _dept_first_search(graph, v, graph_dict)
    return graph_dict

def _dept_first_search(graph, v, marked):
    for e in v.adjList():
        w = e.opposite(v)
        if w not in marked:
            marked[w] = e
            _dept_first_search(graph, w, marked)

          

if __name__ == '__main__':
    g = Graph()

    for i in range(3):
        g.add_vertex(i + 1)

    vertices = g.vertices()

    g.add_edge(vertices[0], vertices[1], 1)
    g.add_edge(vertices[1], vertices[2], 1)

    print(f'{[x.element() for x in dept_first_search(g, vertices[0])]}')
