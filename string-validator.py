s = raw_input()
# commands = "isalnum() isalpha() isdigit() islower() isupper()"
# print "\n".join(str(any(eval("c."+cmd)  for c in s)) for cmd in commands.split())

print any(c.isalnum() for c in s)
print any(c.isalpha() for c in s)
print any(c.isdigit() for c in s)
print any(c.islower() for c in s)
print any(c.isupper() for c in s)
