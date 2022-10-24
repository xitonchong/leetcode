#include<bits/stdc++.h>
using namespace std;

//https://www.geeksforgeeks.org/graph-and-its-representations/


// a utility function to add edge in an undirected graph. 
void addEdge(vector<int> adj[], int u, int v){
    adj[u].push_back(v);
    adj[v].push_back(u);
}

// A utility function to print the adjacent list 
// representation of graph
void printGraph(vector<int> adj[], int V){
    for (int v=0; v < V; ++v){
        cout << "\n Adjacent list of vertex"
             << v << "\n head ";
        for (auto x: adj[v])
            cout << "-> " << x;
        printf("\n");
    }
}

int main(){
    int V = 5;
    vector<int> adj[V];
    addEdge(adj, 0, 1);
    addEdge(adj, 0, 4);
    addEdge(adj, 1, 2);
    addEdge(adj, 1, 3);
    addEdge(adj, 1, 4);
    addEdge(adj, 2, 3);
    addEdge(adj, 3, 4);
    printGraph(adj, V);
    return 0;
}