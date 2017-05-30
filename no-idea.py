n, m = raw_input().split()
# arr = [int(x) for x in raw_input().split()]
# A = [int(x) for x in raw_input().split()]
# B = [int(x) for x in raw_input().split()]

arr = raw_input().split()
A = set(raw_input().split())
B = set(raw_input().split())

# print sum((i in A) - (i in B) for i in arr)
# print '{}\n{}'.format(m, n)
# print arr
# print A
# print B

c = 0
for i in arr:
    if i in A:
        c += 1
    if i in B:
        c -= 1

print c
