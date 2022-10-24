#https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
from collections import defaultdict

class Node():
    def __init__(self, node):
        self.node = node
        self.other = None


class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)


    def DFS_util(self, node, visited):
        # this is a recursive function that collects visited node along the way
        visited.add(node)
        print(node, end=' ')
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.DFS_util(neighbor, visited)

    def DFS(self, start_node):
        visited = set()
        self.DFS_util(start_node, visited)


g = Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print('Followking is Depth First Search from vertex 2')

g.DFS(2)