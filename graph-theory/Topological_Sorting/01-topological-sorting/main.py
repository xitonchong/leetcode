'''
topological sorting only works for directed acyclic graph

definition:
    directed acyclic graph: the graph is directed and will never form a closed loop.
'''
from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def topologicalUtil(self, node, visited, stack):
        visited[node] = True


        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self.topologicalUtil(neighbor, visited, stack)
        
        stack.append(node)  # higher hierarchy at the back
        return stack



    def topological_sorting(self):

        # iterate all nodes

        # if node is a leaf, push to a list
        # if visited go to the next node

        # if node has edges, push the last leaf first before traversing up to the parent node recursively.
        visited = [False] * self.V
        stack = []

        for node in range(self.V):
            if not visited[node]:
                stack = self.topologicalUtil(node, visited, stack)
        print(f"stack is leaf to origin {stack}")
        print(f"stack is origin to leaf {stack[::-1]}")


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(5, 2)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)
    g.topological_sorting()
    ''' yeeay, we have done it!!!'''