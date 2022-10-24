#include<bits/stdc++.h>

using namespace std;

class Graph{

public:
    map<int, bool> visited;
    map<int, list<int>> adj;
    // function to add an edge to graph
    void addEdge(int v, int u);
    void DFS(int v);

};


void Graph::addEdge(int v, int u){
    adj[v].push_back(u); // add u to list
}

void Graph::DFS(int v){
    // mark the node as visited
    visited[v] = true;
    cout << v << " ";
    // recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for (i=adj[v].begin(); i != adj[v].end(); ++i){
        if (! visited[*i]){
            DFS(*i);
        }
    }
}

int main(){
    Graph g;
    g.addEdge(0,1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "followi0ng is depth  first traversal"
            " starting from vertex 2 \n";
    g.DFS(2);
}