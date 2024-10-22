d = {}
with open('file.dat') as f:
    s = f.read()
    for c in s.split():
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

print(d)