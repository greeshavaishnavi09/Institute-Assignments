# Create a dictionary of 5 items, make a copy, clear the original dictionary, and show both.

dic = {}

for i in range(5):
    key = input("Enter a key:")
    value = input("Enter a value:")
    dic[key]= value
print(dic.copy())
dic.clear()
print(dic)

