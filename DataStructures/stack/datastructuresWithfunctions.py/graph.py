from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, v, u):

        self.graph[v].append(u)
        self.graph[u].append(v)

    def print(self):
        for key, value in self.graph.items():
            print(key, ":", value)


def solve(edge):
    g = Graph()
    for i in edge:
        g.add_edge(i[0], i[1])
    g.print()


solve([[1, 2], [2, 3], [4, 2]])
