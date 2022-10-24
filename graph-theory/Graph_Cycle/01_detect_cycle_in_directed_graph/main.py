''' Detect cycle in directed graph
    1. start at origin node, do a depth first search. 
    2. if hit an dead end node, go back to original node, mark node as unvisited.?
    3. iterate until hit a visited node. visited node means theres a cycle.  
    4. check also if next node equal to self. (edges connect to self)


'''
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)


    def addEdges(self, src, dest):
        self.graph[src].append(dest)

    def DFSUtil(self, node, visited, parent):
        visited[node] = True
        # mark node as visited

        # do recursive serach
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                print(f"visit {neighbor}, from {node}")
                if (self.DFSUtil(neighbor, visited, node)):  # mark node as parent node
                    return True
                    # without this if-true line:  this function will return true but traverse back to original node for hit neighbors again
                    '''error without if-true line:
                    visit 1, from 0
                    visit 2, from 1
                    neighbor was visited, 0 from 2
                    visit 2, from 1
                    neighbor was visited, 0 from 2
                    neighbor was visited, 0 from 2
                    match found'''
            elif visited[neighbor] and (neighbor != node):
                print(f"neighbor was visited, {neighbor} from {node}")
                return True
            visited[neighbor] = False
            # if we didnt mark neighbor node as false when going up a node, we may encouter upper node trying to visit lower node that is marked visited by different route
            '''case 2: visit 1, from 0
            visit 2, from 1
            visit 3, from 2
            neighbor was visited, 2 from 0
            match found
            True'''
        return False


    def DFS(self):
        # mark all node as univisted
        visited = [False] * self.V 

        # iterate over all node
        for node in range(self.V):  #this works because we treat our nodes as distinct integer
            if not visited[node]: 
                # visit that node
                if (self.DFSUtil(node, visited, node)):
                    print('match found')
                    return True
        return False


''' DFS: node 0 -> 1, (queue 2) -> 2 -> 0'''


if __name__ == '__main__':
    g = Graph(4)
    g.addEdges(0, 1)
    #g.addEdges(0, 2)
    g.addEdges(1, 2)
    g.addEdges(2, 0)
    g.addEdges(2, 3)
    g.addEdges(3, 3)
    print(g.DFS())

    g = Graph(4)
    g.addEdges(0, 1)
    g.addEdges(0, 2)
    g.addEdges(1, 2)
    g.addEdges(2, 3)
    g.addEdges(3, 3)
    print(g.DFS())