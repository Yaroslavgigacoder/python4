N = int(input())
friends = []
age_list = []
for i in range (N):
    name = input()
    age = int(input())
    age_list.append(age)
    friends.append({'name': name,'age':age})

print(friends)
print(age_list)
midlle_age = sum(age_list)/N
print(midlle_age)
max_name = len(friends[0]['name'])
for i in friends:
    if max_name<len(i['name']):
        max_name = i['name']
print(max_name)