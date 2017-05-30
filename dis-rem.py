n = raw_input()
s = set(map(int, raw_input().split()))
print s
no_c = int(raw_input())
for i in range(no_c):
    x = raw_input().split()
    # print c
    # if c[0] == 'pop':
    #     s.pop()
    # if c[0] == 'remove':
    #     s.remove(int(c[1]))
    # if c[0] == 'discard':
    #     s.discard(int(c[1]))

    # eval('s.{0}({1})'.format(raw_input().split()))
    try:
        int(x[1])
    except IndexError:
        eval('s.%s' % x[0])
    else:
        eval('s.%s(%d)' % (x[0], int(x[1])))

print sum(s)
