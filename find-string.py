string = raw_input().strip()
sub_string = raw_input().strip()

count = 0
print len(string)
print len(sub_string)
for i in range(len(string) - len(sub_string) + 1):
    if (string[i:i + len(sub_string)] == sub_string):
        count += 1

print count
