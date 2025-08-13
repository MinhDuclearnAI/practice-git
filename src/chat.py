b = {'iphone': 500, 'samsung': 350, 'xiaomi': 300, "samsung version 2": 1000}
b = list(b.items())
b.sort(key = lambda x:x[1])
print(b)
while True:
    n = str(input('who is the most beautiful tonight'))
    if n == 'you':
        print('exactly')
        exit()
    else:
        print('again')