from collections import defaultdict

class Node:
    def __init__(self, src):
        self.src = src
        self.next = None


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def BFS(self, s):
        # function to print a BFS of graph
        # mark all nodes as unvisited
        visited = [False] * (max(self.graph) + 1)

        # create queue for BFS
        queue = []

        # mark the source node as visited
        queue.append(s)
        visited[s] = True

        # visit the node if not visited
        while queue:
            s = queue.pop(0)
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True 

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0,1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Breadth First Traversal starting from 2")

    g.BFS(2)



