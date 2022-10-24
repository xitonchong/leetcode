# Python3 program to find minimum initial
# vertices to reach whole matrix
MAX = 100
  
# (n, m) is current source cell from which
# we need to do DFS. N and M are total no.
# of rows and columns.
def dfs(n, m, visit, adj, N, M):
     
    # Marking the vertex as visited
    visit[n][m] = 1
  
    # If below neighbor is valid and has
    # value less than or equal to current
    # cell's value
    if (n + 1 < N and
        adj[n][m] >= adj[n + 1][m] and
        not visit[n + 1][m]):
        dfs(n + 1, m, visit, adj, N, M)
  
    # If right neighbor is valid and has
    # value less than or equal to current
    # cell's value
    if (m + 1 < M and
        adj[n][m] >= adj[n][m + 1] and
        not visit[n][m + 1]):
        dfs(n, m + 1, visit, adj, N, M)
  
    # If above neighbor is valid and has
    # value less than or equal to current
    # cell's value
    if (n - 1 >= 0 and
        adj[n][m] >= adj[n - 1][m] and
        not visit[n - 1][m]):
        dfs(n - 1, m, visit, adj, N, M)
  
    # If left neighbor is valid and has
    # value less than or equal to current
    # cell's value
    if (m - 1 >= 0 and
        adj[n][m] >= adj[n][m - 1] and
        not visit[n][m - 1]):
        dfs(n, m - 1, visit, adj, N, M)
 
def printMinSources(adj, N, M):
 
    # Storing the cell value and cell
    # indices in a vector.
    x = []
     
    for i in range(N):
        for j in range(M):
            x.append([adj[i][j], [i, j]])
  
    # Sorting the newly created array according
    # to cell values
    x.sort()
  
    # Create a visited array for DFS and
    # initialize it as false.
    visit = [[False for i in range(MAX)]
                    for i in range(N)]
     
    # Applying dfs for each vertex with
    # highest value
    for i in range(len(x) - 1, -1, -1):
         
        # If the given vertex is not visited
        # then include it in the set
        if (not visit[x[i][1][0]][x[i][1][1]]):
            print('{} {}'.format(x[i][1][0],
                                 x[i][1][1]))
             
            dfs(x[i][1][0],
                x[i][1][1],
                visit, adj, N, M)
         
# Driver code
if __name__=='__main__':
 
    N = 2
    M = 2
  
    adj = [ [ 3, 3 ], [ 1, 1 ] ]
    
    N, M = 4, 4
    adj =  [[1, 2, 3, 3], 
            [3, 1, 3, 4], 
            [1, 2, 3, 3], 
            [3, 2, 1, 1]]
    printMinSources(adj, N, M)
 
# This code is contributed by rutvik_56