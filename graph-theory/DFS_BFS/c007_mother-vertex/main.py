''' find mother vertex in a directed graph'''

from collections import defaultdict 

class Graph():
    def __init__(self, V):
        self.V  = V # number of vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def DFSUtil(self, src, visited):
        # mark all vertex as not visited

        visited[src] = True

        # append src vertex to queue and mark it as visited
        for neighbor in self.graph[src]:
            if not visited[neighbor]:
                # if neighbor is not visited, append to queue and mark as visited
                self.DFSUtil(neighbor, visited)
                

    def findMother(self):
        visited = [False] * (self.V)

        # to store last finished vetex (or mother vertex)
        v = 0
        for i in range(self.V):
            if visited[i] == False:
                self.DFSUtil(i, visited)
                v = i

        visited = [False]* (self.V)
        self.DFSUtil(v, visited)
        if any(i == False for i in visited):
            return -1 
        else:
            return v

# Create a graph given in the above diagram
g = Graph(7)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(4, 1)
g.addEdge(6, 4)
g.addEdge(5, 6)
g.addEdge(5, 2)
g.addEdge(6, 0)
print("A mother vertex is " + str(g.findMother()))


        

        