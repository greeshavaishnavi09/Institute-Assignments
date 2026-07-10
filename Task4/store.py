#Take 3 student names and marks as input and store them in a dictionary (name as key, mark as value).

dic = { }

for i in range(3):
    name = input("Enter a name:")
    marks = int(input("Enter a num:"))
    dic[name]=marks

print(dic)