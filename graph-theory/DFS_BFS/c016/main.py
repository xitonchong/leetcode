
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, node, visited):

        visited[node] = 1
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                # mark node as visited
                print(f"visited {neighbor} \n")
                self.DFS(neighbor, visited)
    ''' 0-> 1 (wait 2)-> 2 -> count+1 neighbor done -> 
    '''

    def DFSUtil(self):
        # mark all node as unvisited
        #visited = [0 for _ in range(self.V)]
        visited = [False] * self.V
        count = 0

        for node in range(self.V):
            if not visited[node]:
                self.DFS(node, visited)
                count += 1
        print(count)



if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(3,4)

    g.DFSUtil()