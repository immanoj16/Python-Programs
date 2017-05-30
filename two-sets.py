#!/bin/python

import sys


def getTotalX(a, b):
    max_a = max(a)
    min_b = min(b)
    result = 0
    for i in range(max_a, min_b + 1):
        c = 0
        d = 0
        for j in a:
            if i % j == 0:
                c += 1
        for j in b:
            if j % i == 0:
                d += 1
        if c == len(a) and d == len(b):
            result += 1
    return result

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
total = getTotalX(a, b)
print(total)
