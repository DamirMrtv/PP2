a = input().split()
min = 1000
for i in range(len(a)):
  f = int(a[i])
  if(f < min) and (f > 0):
      min = f

print(min)