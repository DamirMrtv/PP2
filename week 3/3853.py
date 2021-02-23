a = input().split()
a = list(map(int, input().split()))
x = int(input())
for i in len(a):
    k = len(a) - 1
    p = a[k]
    a.remove(p)
    a1 = a.insert(0 , p)
    print(a)


