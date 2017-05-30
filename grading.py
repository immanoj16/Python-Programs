#!/bin/python

import sys


def solve(grades):
    result = []
    for i in grades:
        if i >= 38:
            if i % 5 >= 3:
                i += (5 - i % 5)
        result.append(i)
    return result

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
