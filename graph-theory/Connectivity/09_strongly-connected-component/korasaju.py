from collections import defaultdict, deque


'''
Korasaju algorithm
What is strongly connected component? It is cluster of vertices which can formed a closed path 
1.  To find SCC, you need to iterate from the weakest link. i.e a leaf
2.  do a DFS and store the sequence in a stack.
3.  iterate from the bottom of the stack of nodes and feed into a reversed graph. 
4.  you should be able to get strongly connected component in this way.
'''


class Graph:
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = defaultdict(list)


    def addEdge(self,  src, dest):
        self.graph[src].append(dest)

    def getTranspose(self):
        g = Graph(self.V)

        for u in self.graph:
            for v in self.graph[u]:
                g.addEdge(v, u) # reverse the order
        return g


    def OrderFill(self, node,  visited, stack):
        visited[node] = True

        for i in self.graph[node]:
            if not visited[i]:
                self.OrderFill(i, visited, stack)
        stack = stack.append(node)
        

    def DFSUtil(self, node, visited):
        visited[node] = True
        print(node, end="")
        
        for i in self.graph[node]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def SCC(self):
        visited = [False] * self.V 

        # init empty stack
        stack = []
        for node in range(self.V):
            if not visited[node]:
                self.OrderFill(node, visited, stack)

        gr = self.getTranspose()
        print(gr.graph)
        visited = [False] * (self.V)

        while stack:
            node = stack.pop() # pop takes off last of the stack, while deque.popleft() takes off the bottom of the stack
            if not visited[node]:
                gr.DFSUtil(node, visited)
                print('')


if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    g.SCC()