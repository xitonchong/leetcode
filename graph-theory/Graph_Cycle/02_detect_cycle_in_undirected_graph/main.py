''' algorithm:
    1. create the graph using the given number of edges and vertices.
    2. create a recursive function that have current index or vertex, visited array and parent node.
    3. mark the current node as visited.
    4. find all the vertices which are not visited and are adjacent to the current ndoe. Recusively call the function for those vergices, if the recursive function returns true return true.
    5. if the adjacent node is not parent and already visited then return true.
    6. create a wrapper class, that class the recursive function for all the vertices and if any function returns true, return true. 
    7. else if for all vertices the function returns false return false.
'''

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest):
        self.graph[src].append(dest)
        self.graph[dest].append(src)

    def isCycle(self):
        visited = [False] * self.V  #mark all vertices as unvisited

        # whatis parent?
        parent = 0 # starts from vertex 0

        for node in range(self.V):
            if not visited[node]:
                if (self.CycleUtil(node, visited, -1)) == True:
                    # if any returns True stop and return True
                    return True
        return False


    def CycleUtil(self, node, visited, parent):
        # util for recursive function
        visited[node] = True 

        # if current node hit visited node mark and i=parent, continue
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                if (self.CycleUtil(neighbor, visited, node)): # mistake from node to parent
                    return True
            elif parent != neighbor:
                return True
        return False


# O(V+E) iterate over vertices and edges once

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    print(f"1 is there a cycle? {g.isCycle()}")

    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    #g.addEdge(2, 0)
    g.addEdge(2, 3) 
    print(f"2 is there a cycle? {g.isCycle()}")