print('version 1')
#dem so phan tu khac nhau
a = list(map(int, input().split()))
b = a.copy()
a = set(a)
print(len(a))
b = b[:: -1]