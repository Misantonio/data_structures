# Program that computes the shortest path between two places
# Compare two kink of data structures

from math import sqrt
from collections import defaultdict

def distance(placeA, placeB):
    A = df.loc[df['place'] == placeA].iloc[0]['coords']
    B = df.loc[df['place'] == placeB].iloc[0]['coords']
    return sqrt(((B[0]-A[0])**2) + ((B[1]-A[1])**2))

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.paths = []
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def printAllPathsUtil(self, u, d, visited, path):
        '''A recursive function to print all paths from 'u' to 'd'. 
        visited[] keeps track of vertices in current path. 
        path[] stores actual vertices and path_index is current 
        index in path[]'''
        # Mark the current node as visited and store in path 
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d:
            self.paths.append(str(path))
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, d, visited, path)
        path.pop()
        visited[u] = False
        
    
    def printAllPaths(self, s, d):
        visited = [False]*(self.V)
        path = []
        self.printAllPathsUtil(s, d, visited, path)


if __name__ == "__main__":
    import sys
    import pandas as pd
    from ast import literal_eval as lit_ev
    import timeit

    df = pd.read_csv("path.csv", converters={"toGo": lit_ev, "coords": lit_ev})

    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(0,4)
    g.addEdge(1,0)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,2)
    g.addEdge(3,4)
    g.addEdge(4,3)
    
    placeA = sys.argv[1]
    placeB = sys.argv[2]

    indexA = df.loc[df['place'] == placeA].index[0]
    indexB = df.loc[df['place'] == placeB].index[0]

    g.printAllPaths(indexA, indexB)
    paths = [ lit_ev(path) for path in g.paths]

    distances = []
    routes = []
    for path in paths:
        dist = 0
        route = []
        for a, b in zip(path[:-1], path[1:]):
            A = df.iloc[a]['place']
            B = df.iloc[b]['place']
            d = distance(A, B)
            dist += d
            route.append(A)
        distances.append(dist)
        route.append(placeB)
        routes.append(route)
    
    print(routes[distances.index(min(distances))])