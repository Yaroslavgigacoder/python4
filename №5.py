N = int(input())
translate_dict = {}
age_list = []
for i in range (N):
    eng = input()
    rus_list = eng.split(' - ')
    translate_dict[rus_list[0]] = rus_list[1].split(', ')
print(translate_dict)