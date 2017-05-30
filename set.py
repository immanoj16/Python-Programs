n = int(raw_input())
# arr = map(int, raw_input().split())
arr = set(map(int, raw_input().split()))

print sum(arr) / float(len(arr))
