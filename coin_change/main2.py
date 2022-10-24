

def countN(array, N):
    # array is a  list of coins possible for change
    table = [0] * (N + 1)

    table[0] = 1 # there is 1 way to sum of 0 coins, by putting 0 coins

    for coin in array:
        for n in range(N+1):
            if coin <= n:
                table[n] += table[n - coin]
                print(table)
    return table[N]

if __name__ == '__main__':
    array = [1, 5, 10]
    N = 10
    print(countN(array, N))
