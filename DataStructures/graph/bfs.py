from collections import defaultdict


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def breadth_first_search(self, x):
        visited = {}
        for key, _ in self.graph.items():
            visited[key] = False
        queue = []
        queue.append(x)
        visited[x] = True

        while queue:
            q = queue.pop(0)
            print(q, end=" ")
            for i in self.graph[q]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.breadth_first_search(2)
