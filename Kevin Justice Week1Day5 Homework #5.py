table = []
for x in range(1,11):
    lst = []
    for y in range(1,11):
        lst.append(x*y)
    table.append(lst)
for x in range(0,10):
    print(table[x])
