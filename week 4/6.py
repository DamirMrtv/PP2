import re

s = int(input())
a = []
for i in range(s):
    l = input()
    a.append(l)


x = re.findall(r"#",a)
print(x)
