#!/bin/python

t = int(raw_input().strip())
for a0 in xrange(t):
    a = fib = 1
    b = s = 2
    n = long(raw_input().strip())
    while fib <= n:
        if fib % 2 == 0:
            s += fib
        fib = a + b
        a = b
        b = fib
        print fib

    print s
