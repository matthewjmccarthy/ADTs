from Graph import Graph

g = Graph()

for i in range(10):
    g.add_vertex(i + 1)

print(g)

count = 1
for v in g.vertices():
    for u in g.vertices():
        if v != u and v.element()%2 == 0 and u.element()%2 == 0:
            g.add_edge(v, u, 1)
            count += 1

print(g)