from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        print(self.graph)

    def BFT(self, startingVertex):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(startingVertex)
        visited[startingVertex] = True
        while queue:
            startingVertex = queue.pop(0)
            print(startingVertex, end=" ")
            for i in self.graph[startingVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFT(self, startingVertex):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(startingVertex)
        visited[startingVertex] = True
        while queue:
            startingVertex = queue.pop()
            print(startingVertex, end=" ")
            for i in self.graph[startingVertex]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, startingVertex,val):
        visited = [False] * (len(self.graph))
        queue = []
        queue.append(startingVertex)
        visited[startingVertex] = True
        while queue:
            startingVertex = queue.pop()
            # print(startingVertex, end=" ")
            for i in self.graph[startingVertex]:

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
g.display()
g.BFT(2)
print()
g.DFT(2)
