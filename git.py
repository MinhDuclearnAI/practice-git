a = list(map(int, input('version 1 nhap list di:').split()))
n = int(input())
a = [x * n for x in a]
print(a)