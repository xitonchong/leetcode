

        

# undirected graph
from collections import deque, defaultdict

adj = defaultdict(list)

def addEdge(u, v):
    adj[u].append(v)
    adj[v].append(u)

def BFSsearch(parent_node, count_level):
    vertices = 1000
    visited = [False] * vertices
    level = [0] * vertices

    queue = deque()

    queue.append(parent_node)
    visited[parent_node]=True

    while len(queue) > 0:
        parent_node = queue.popleft()
        for branch in adj[parent_node]:
            if not visited[branch]:
                visited[branch] = True
                queue.append(branch)
                level[branch] = level[parent_node] + 1
    count =0
    # count the level if matches level of branch
    for branch in range(vertices):
        if level[branch] == count_level:
            count += 1 
    return count



    

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.origin = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s, l):
        # mark all the vertices
        level = [0] *self.V 
        visited = [False] * self.V
        # create a deque, a list with O(1) time when traversing front or back pop
        queue = deque()
        visited[s] = True
        queue.append(s)
        level[s] = 0
        while len(queue) > 0:
            s = queue.popleft()

            # get all adjacent vertices
            # if it has not been visited, markt it visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
                    level[i] = level[s] + 1

        count = 0
        for i in range(self.V):
            if level[i] == l:
                count += 1
        return count

# Driver code
if __name__ == '__main__':
     
    # Create a graph given
    # in the above diagram
    g = Graph(6)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 5)
  
    level = 2
  
    print(g.BFS(0, level))

    # non class method
    addEdge(0, 1)
    addEdge(0, 2)
    addEdge(1, 3)
    addEdge(2, 4)
    addEdge(2, 5)

    print(BFSsearch(0, 2))