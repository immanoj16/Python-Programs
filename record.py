
import sys


def getRecord(s):
    g = p = s[0]
    h = l = 0
    for i in s:
        if i > p:
            p = i
            h += 1
        if i < g:
            g = i
            l += 1
    return [h, l]

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
