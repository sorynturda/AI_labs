from math import exp

def softmax(a: list) -> list:
    res = [exp(x) / sum([exp(it) for it in a]) for x in a]
    return res

a = [-0.4, 0, 0.2, 0.2, 0.4]
print(softmax(a))