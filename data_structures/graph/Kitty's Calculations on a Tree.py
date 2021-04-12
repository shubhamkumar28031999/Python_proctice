from collections import  deque
from itertools import combinations

class graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
            if end in self.graph_dict:
                self.graph_dict[end].append(start)
            else:
                self.graph_dict[end]=[start]

    def display(self):
        print(self.graph_dict)

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

if __name__=="__main__":
    arr,quer=map(int,input().split())
    routes=[]
    for _ in range(arr-1):
        routes.append(list(map(int,input().split())))
    route_graph = graph(routes)
    for _ in range(quer):
        n=int(input())
        temp=0
        temp_arr=list(map(int,input().split()))
        if n>1:
            index=combinations(temp_arr,2)
            for x,y in index:
                # print(route_graph.get_shortest_path(x,y))
                temp+=x*y*(len(route_graph.get_shortest_path(x,y))-1)
        print(temp)

