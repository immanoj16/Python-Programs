#!/bin/python


def solve(n, s, d, m):
    c = 0
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            c += 1
    return c

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)

# def getWays(squares, d, m):
#     tp = (len(squares)-m) + 1 #total number of pieces possible
#     return len([1 for i in range(tp) if sum(squares[i:i+m])==d])
