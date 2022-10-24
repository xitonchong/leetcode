
from collections import defaultdict, namedtuple


''' we are given a matrix that contains different values in each cell.
     this is a undirected graph: 2 ways 
    each node has weighted
    do not need to represent as graph, it is better off as matrix format
'''

def DFS(n, m, adj, visited, N, M): 
    visited[n][m] = 1
    print(f" visiting {n} {m} {adj[n][m]}")
    # DOWN CASE
    if (n+1 < N and \
        adj[n][m] >= adj[n+1][m] and \
        visited[n+1][m] == 0):
        DFS(n+1, m, adj, visited, N, M )
    
    # UP CASE
    if (n-1 >= 0 and \
        adj[n][m] >= adj[n-1][m] and \
        visited[n-1][m] == 0):
        DFS(n-1, m, adj, visited, N, M)

    # LEFT CASE
    if (m-1 >= 0 and \
        adj[n][m] >= adj[n][m-1] and \
        visited[n][m-1] == 0):
        DFS(n, m-1, adj, visited, N, M)

    # right case
    if (m+1 < M  and \
        adj[n][m] >= adj[n][m+1] and \
        visited[n][m+1] == 0):
        DFS(n, m+1, adj, visited, N, M)




def MinSource(adj, N, M):
    # mark all nodes as unvisited
    visited = [[0 for _ in range(N)] for _ in range(M)]

    # origin coordinates are selected based on highest value in the matrix
    x = []
    for n in range(N):
        for m in range(M):
            x.append([adj[n][m], [n, m]])
    x.sort()


    for i in range(len(x), -1, -1):
        # [i][1][0] refers to n 
        #print(i)
        if not visited[ x[i-1][1][0] ][ x[i-1][1][1] ]:
            print(f"{x[i-1][1][0]} {x[i-1][1][1]}")
            DFS(x[i-1][1][0], 
                x[i-1][1][1],
                adj, visited, N, M)
            


    DFS(n, m , adj, visited, N, M)

    # how to get the largest path
    # there need to be a variable that stores visited path


if __name__ == '__main__':
    N = 2
    M = 2

    adj = [[3, 3], 
           [1, 1]]

    N, M = 3,3
    adj =  [[1,2,3], 
            [2,3,1], 
            [1,1,1]]

    N, M = 4, 4
    adj =  [[1, 2, 3, 3], 
            [3, 1, 3, 4], 
            [1, 2, 3, 3], 
            [3, 2, 1, 1]]
    MinSource(adj, N, M)
