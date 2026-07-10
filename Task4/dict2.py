#Create a dictionary student with 4 key-value pairs. Then use update() to add another dictionary, remove the last item using popitem(),and finally print all items using items().

dict = {"name": "greesha", "age": 76, "class": 8, "gender": "female"}
dict.update({"marks": 76})
dict.popitem()
dict.items()
print(dict)