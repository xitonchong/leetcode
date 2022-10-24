


import sys
import time


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # represent graph as connection matrix
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]


    def dijkstra(self, node, visited, path):
        ''' algorithm works as follows:
            1. init two dictionaries, visited and path; path is initialized to max values.
            path[ shortest_path, visited from vertex B]
                if not visited:
                2. DFS from origin node, update the path table if > less than current weight
            3. add node to visited after comparing.
            
        '''
        # mark node as visited 
        visited[node] = True

        for neighbor in self.graph[node]:
            #print(neighbor)
            if (neighbor > 0) and (not visited[neighbor]):
                #print(self.graph[node][neighbor], path[node])
                if (self.graph[node][neighbor] + path[node]) < path[neighbor]:
                    # if weight + current node less than initialized infiinite weight
                    path[neighbor] = self.graph[node][neighbor] + path[node]
                    #path[neighbor][1] = node  # put the visiting vertex here
                    print(f"{path[neighbor]}, visiting vertex: {path[neighbor]}")
                    time.sleep(2)
                # continue to explore the graph
                self.dijkstra(node, visited, path)
            # mark node as unvisited if explore up a node
            #visited[node] = False
        #return path




    def shortest_path(self, src):
        visited = [False] * self.V
        #path = defaultdict(str)  # 'weight, node'
        # initialized path vertices to infinity
        path = [99999 ] * self.V
        path[src] = 0

        
        for node in range(self.V):
            print(node)
            if not visited[node]:
                self.dijkstra(node, visited, path)

        print(f"shortest path: {shortest_path}")



if __name__ == '__main__':
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    g.shortest_path(0)
    