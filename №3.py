N = int(input())
friends = []
for i in range (N):
    name = input()
    age = int(input())
    friends.append({'name': name,'age':age})
print(friends)
min_age = friends[0]['age']
for some_friend in friends:
    if some_friend['age'] < min_age:
        min_age = some_friend['age']
for some_friend in friends:
    for key in some_friend.keys():
        if some_friend['age'] == min_age:
            print(some_friend['name'])
            break

