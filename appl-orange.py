#!/bin/python

import sys


s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))

# print sum([1 for i in apple if (a + i) >= s and (a + i) <= t])
# print sum([1 for i in orange if (b + i) >= s and (b + i) <= t])

c = 0
d = 0
for i in apple:
    if a + i >= s and a + i <= t:
        c += 1

for i in orange:
    if b + i >= s and b + i <= t:
        d += 1

print c, '\n', d
