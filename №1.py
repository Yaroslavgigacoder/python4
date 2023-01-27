import random
n = int(input())
list = []
for i in range(n):
    list.append(random.randint(1,10))
print(list)
list = set(list)
print(list)
print(len(list))     