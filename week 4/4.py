import re
s = input()

x = re.findall(r"[ауоыиэяюёеАУОЫИЭЯЮЁЕ]",s)
print(len(x))