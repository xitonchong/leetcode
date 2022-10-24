from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def addEdge(self, src, dest):
        self.graph[src].append(dest)

    def isReachable(self, u, v):
        visited = [False] * self.V 

        queue = deque()
        queue.append(u)
        visited[u] = True

        while queue:
            node = queue.popleft()

            if node == v:
                return True

            for i in self.graph[node]:
                # if i == v:
                #     return True
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

        return False


    
if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    u, v = 1, 3
    if g.isReachable(u, v):
        print("There is a path from %d to %d" % (u,v))
    else :
        print("There is no path from %d to %d" % (u,v))
    
    u = 3; v = 1
    if g.isReachable(u, v) :
        print("There is a path from %d to %d" % (u,v))
    else :
        print("There is no path from %d to %d" % (u,v))