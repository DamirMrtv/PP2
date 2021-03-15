import re
s = input()
x = re.search(r"([A-Za-z0-9])\1+",s)
if x:
    print(x.group(1))
else:
    print("-1")
