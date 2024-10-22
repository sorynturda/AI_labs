def threeSameConsInts(a: list, b: list) -> bool:
    for i in range(len(a) - 3):
        for j in range(len(b) - 3):
            if a[i:i + 3] == b[j:j + 3]:
                return True
    return False


a = [1, 10, 9, 10, 8]
b = [10, 9, 10, 7, 6]
# b = [8, 10, 9, 7, 6]
print(threeSameConsInts(a, b))
