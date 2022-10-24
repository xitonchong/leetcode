
#include<iostream>
#include<list>


using  namespace std;

class Graph{
    int V;
    // Pointer to an array containing adjacency
    // lists
    list<int> *adj;

public:
    Graph(int V); //constructor
    
    //function to add an edge to graph
    void addEdge(int v, int w);

    //prints BFS traversal from a given source s
    void BFS(int s);

};

Graph::Graph(int V){
    this-> V = V; // the arros operator exists to accss the members of the structure or the unions using pointers.
    adj = new list<int>[V];
}

void Graph::addEdge(int v, int w){
    adj[v].push_back(w); // add w to v's list
}

void Graph::BFS(int s){
    //mark all the vertices as not visited
    bool *visited = new bool[V];
    for (int i=0; i<V;i++)
        visited[i] = false;
    
    //create a queue for BFS
    list<int> queue;

    visited[s] = true;
    queue.push_back(s);
    
    // 'i' will be used to get all adjacent 
    //  vertices of a vertex
    list<int>::iterator i;

    while (!queue.empty()){
        // dequeue a vertex from queue and print it
        s = queue.front();
        cout << s << " ";
        queue.pop_front();

        // get all adjacent vertices of the dequeud vertex s. If a adjacen has not been visited, then mark it visited and enqueue it
        for (i = adj[s].begin(); i != adj[s].end(); ++i ){
            if (!visited[*i]){
                visited[*i] = true;
                queue.push_back(*i);
            }        
        }
    }
}

int main(){
    // create a graph given in the above program
    Graph graph(4);
    graph.addEdge(0,1);
    graph.addEdge(0,2);
    graph.addEdge(1,2);
    graph.addEdge(2,0);
    graph.addEdge(2,3);
    graph.addEdge(3,3);

    cout << " Following is Breadth First Traversal "
         << " (starting from vertex 2) \n";

    graph.BFS(2);
    
    return 0;
}