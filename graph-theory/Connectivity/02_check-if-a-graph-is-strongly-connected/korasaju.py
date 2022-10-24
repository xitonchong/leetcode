'''

Following is Korasaju's DFS based simple algorithm that does two DFS traversals of graphs
1. initialize all vertices as not visited
2. do a DFS traversal of graph starting from any arbitraru vertex v. If DFS traversal doesn't visit all vertices, then return False.
3. reverse all arcs (or find transpose or reverse of graph)
4. mark all vertices as not-visited in reversed graph.
5. do a DFS traversal of reversed graph starting from same vertex v. If DFS traversal doens't visit all vertices, then return false, otherwise return True.
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)


    def DFS(self, node, visited):
        visited[node] = True

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited)

    def getTranspose(self):
        t_graph = Graph(self.V)

        for src in self.graph:
            for dest in self.graph[src]:
                t_graph.addEdge(dest, src)

        return t_graph

    def isSC(self):
        # init all vertices as not visited
        visited = [False] * self.V 

        self.DFS(0, visited) #  do not need to iterate all vertices
                
        if any(i == False for i in visited):
            return False

        # step 3: create a reverse graph;
        g_transpose = self.getTranspose()
        #print(g_transpose.graph, self.graph)

        # mark all visited as false
        visited = [False] * self.V 
        g_transpose.DFS(0, visited)

        if any(i == False for i in visited):
            return False 
        return True


    
if __name__ == '__main__':
    # Create a graph given in the above diagram
    g1 = Graph(5)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)
    g1.addEdge(3, 0)
    g1.addEdge(2, 4)
    g1.addEdge(4, 2)
    print("Yes" if g1.isSC() else "No")
    
    g2 = Graph(4)
    g2.addEdge(0, 1)
    g2.addEdge(1, 2)
    g2.addEdge(2, 3)
    print("Yes" if g2.isSC() else "No")