b = {'iphone': 500, 'samsung': 350, 'xiaomi': 300, 'samsung zfold': 1200, 'ip16': 1500}
b = list(b.items())
b.sort(key = lambda x:x[1])
print(b)