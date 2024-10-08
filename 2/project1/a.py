# # 1
# price = {'apples': 10, 'milk': 12, 'bread': 5}
# mylist = [('apples', 2), ('milk', 2)]
#
# res = [price[x[0]] * x[1] for x in mylist]
# print("1:", sum(res))
#
# # 2
# friends = [('andrew', 10), ('george', 20),
#            ('andrew', 5), ('ann', 10)]
# friends_set = {x[0] for x in friends}
# print(friends_set)
#
# # 3
# n = int(input())
# res = [x + 1 if n % 2 == 0 else (x + 1) ** 2 for x in range(n)]
# print(res)
#
# # 4
# s = input()
# n = int(input())
# new_dict = {x: s[x:] for x in range(n)}
# print(new_dict)
import a

# # 5
# def functie(s):
#     res = [chr(ord(x)+1) for x in s]
#     return ''.join(res)
#
# print(functie(input()))

#6
f = open('a.txt', "r")
s = f.read()
with open('b.txt', "a") as b_file:
    b_file.write(s.title() + '\n')
f.close()