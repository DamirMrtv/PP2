import re

s = int(input())
a = []
for i in range(0,s):
    l = input()
    a.append(l)

for k in a:
    x = re.findall(r"[A-Za-z]+\s<[A-Za-z][\w!+_.-]+@[a-z]+\.[a-z]{1,4}>",k)
    if x:
        print(*x)