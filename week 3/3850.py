mylist = list(map(int,input().split()))
new_list = []
for i in mylist:
    if i != 0:
        print(i, end = ' ')
    else:
        new_list.append(i)
for i in new_list:
    print(i, end = ' ')