n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
a = map(int, raw_input().strip().split(' '))

mods = [0] * k
for i in range(n):
    mods[a[i] % k] += 1
count = 0
for i in range(int(k / 2) + 1):
    if i == 0:
        count += int(mods[0] * (mods[0] - 1) / 2)
    elif float(i) == (k / 2):
        count += int(mods[int(k / 2)] * (mods[int(k / 2)] - 1) / 2)
    else:
        count += int(mods[i] * mods[k - i])

print (count)
