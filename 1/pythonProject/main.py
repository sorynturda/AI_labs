# 1
a = [1, 2, 5, 7, 8]
res = sum(a) / len(a)
print(res)

# 2
a = [-1, -5, -6, 1, 2, 10]
neg = [x for x in a if x < 0]
poz = [x for x in a if x >= 0]
print(neg)
print(poz)

# 3
a = [1, 2, 3, 4, 5, 6, 7, -7]
res = sum(a[:-2])
print(res)

# 4
l = a[1::2]
print(l)

# 5
res = a[1]
for i in a:
    if res > i:
        res = i
print(res)
