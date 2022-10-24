'''Implement a undirected graph'''

class AdjNode:
    def __init__(self, node):
        self.node = node
        self.next = None


class Graph():
    def __init__(self, V):
        self.vertices = V 
        self.graph = [None]* self.vertices

    def addEdge(self, src, dest):
        # adding dest node to the source node
        node = AdjNode(dest)
        node.next = self.graph[src] # the next of a node is a node appending to next
        self.graph[src] = node # rewrite the graph with the updated node

        # adding src node to the dest node
        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    # function to print the graph
    def print_graph(self):
        for i in range(self.vertices):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.node), end="")
                temp = temp.next
            print("\n")

if __name__ == '__main__':
    V = 5
    graph = Graph(V)
    graph.addEdge(0,1)
    graph.addEdge(0,4)
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(1,4)
    graph.addEdge(2,3)
    graph.addEdge(3,4)

    graph.print_graph()
