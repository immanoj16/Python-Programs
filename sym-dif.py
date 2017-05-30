# a, b = [set(raw_input().split()) for _ in range(4)][1::2]
# print '\n'.join(sorted(a ^ b, key=int))

raw_input()
a = set(map(int, raw_input().split()))
raw_input()
b = set(map(int, raw_input().split()))
for c in sorted(a ^ b):
    print c
