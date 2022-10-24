'''given a directed graph, find out if a vertex v is reachable from another vertex u for all vertex pairs (u,v) in the given graph.
Here reachable means that there is a path from vertex u to v.'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V= vertices
 
        # default dictionary to store graph
        self.graph= defaultdict(list)
 
        # To store transitive closure
        self.tc = [[0 for j in range(self.V)] for i in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)
 


    def DFSUtil(self, src, visited):
        # mark the node as visited
        visited[src] = True

        for neighbor in self.graph[src]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)
        return visited

    def transitiveClosure(self):
        
        # iterate over all vertices
        for v in range(self.V):
            visited = [False] * (self.V)
            visited = self.DFSUtil(v, visited)
            # available vertex are now marked with true now
            # update transitive matrix
            visited_array = [ int(x==True) for x in visited]
            self.tc[v] = visited_array


        return self.tc

g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print("Transitive closure matrix is", g.transitiveClosure())
            
#Transitive closure matrix is [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 1]]