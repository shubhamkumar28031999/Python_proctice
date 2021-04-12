from collections import  deque

class Graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for start,end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start]=[end]


    def display(self):
        print(self.graph_dict)


    def get_paths(self, start, end, path=None):
        if path is None:
            path = []
        path =path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        paths=[]
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths=self.get_paths(node,end,path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp=self.get_shortest_path(node,end,path)
                if sp:
                    if shortest_path is None or len(sp)<len(shortest_path):
                        shortest_path=sp
        return shortest_path

    def BFT(self, startingVertex):
        queue=deque()
        queue.append(startingVertex)
        path=[]
        while queue:
            curr_vertex=queue.popleft()
            if curr_vertex not in path:
                path.append(curr_vertex)
            if curr_vertex in self.graph_dict:
                    for nodes in self.graph_dict[curr_vertex]:
                            queue.append(nodes)
        return path


    def DFT(self, startingVertex):
        queue = deque()
        queue.append(startingVertex)
        path = []
        while queue:
            curr_vertex = queue.pop()
            if curr_vertex not in path:
                path.append(curr_vertex)
            if curr_vertex in self.graph_dict:
                for nodes in self.graph_dict[curr_vertex]:
                    queue.append(nodes)
        return path
if __name__=="__main__":
    routes=[
        ('Mumbai','Paris'),
        ('Mumbai','Dubai'),
        # ('Paris','Dubai'),
        ('Paris','New York'),
        ('Dubai','New York'),
        ('New York','Toronto'),
    ]

    route_graph=Graph(routes)
    start="New York"
    end="Dubai"
    print(route_graph.display())
    print(route_graph.BFT(start))
    print(route_graph.DFT(start))
