def whoGetsTheCatch(n, x, X, V):
    Y = [0] * n
    for i in range(n):
        if X[i] < x:
            Y[i] = (x - X[i]) / V[i]
        else:
            Y[i] = (X[i] - x) / V[i]

    result = min(Y)
    c = 0
    for i in range(n):
        if result == Y[i]:
            loc = i
            c += 1
    if c > 1:
        return -1
    else:
        return loc

n, x = raw_input().strip().split(' ')
n, x = [int(n), int(x)]
X = map(int, raw_input().strip().split(' '))
V = map(int, raw_input().strip().split(' '))
result = whoGetsTheCatch(n, x, X, V)
print(result)
