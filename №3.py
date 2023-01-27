N = int(input())
friend = {}
friends = []
list_age = []
for i in range (N):
    age = int(input())
    name = input()
    list_age.append(age)
    friend[age] = name
friends.append(friend)    
print(list_age)
print(friends)
young = min(list_age)
print(friend[young])