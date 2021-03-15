import re
s = '[qwrtypsdfghjklzxcbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s,input(), re.I)
if a:
    for sub in a:
        print(sub)
else:
    print(-1)