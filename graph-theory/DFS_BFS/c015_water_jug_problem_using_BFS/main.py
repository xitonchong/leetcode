
from collections import deque


def BFS(a, b, target):
    m = {}
    isSovlable = False
    path = []

    # queue to maintain states
    q = deque()

    q.append((0,0))

    while len(queue) != 0:
        u = q.popleft()
        if ((u[0], u[1]) in m):
            continue
        if ((u[0] > a) or (u[0]<0) or
            (u[1] > b) or (u[1]<0)):
            continue
        
        # filling the vector for constructing the solution path
        path.append((u[0], u[1]))

        # mark state as visited
        m[(u[0], u[1])] = 1

        # if we reach solution state, put ans=1
        if u[0]==a and u[1]==b:
            isSovlable = True

        



if __name__ == '__main__':
    jug1, jug2, target = 4, 3, 2
    BFS(jug1, jug2, target)


